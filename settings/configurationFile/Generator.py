#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 18-07-2012
#

from data.model.DataMapping import DataMapping
from data.model.DstServer import DstServer
from data.model.DstServerMapping import DstServerMapping
from data.model.MappedObject import MappedObject
from data.model.SrcServer import SrcServer
from data.provider.DataProviderFactory import DataProviderFactory
from data.sender.DataSenderFactory import DataSenderFactory
from settings.Settings import Settings
import logging
import lxml.etree as etree

class Generator(object):
	"""
	Interactively generates a configuration file
	"""

	def __init__(self, settings):
		"""
		Real settings created on the basis of command line arguments given by the user
		"""
		self.__settings = settings
		
		"""
		Used to store user-input data before generating an xml file to save real settings
		object from pollution
		"""
		self.__generatedSettings = Settings()
		
		self.__configureLogger()
		
		#For compatibility between Python 2.x and 3.x
		try:
			self.__input = raw_input
		except:
			self.__input = input
		
	def generate(self):
		self.__logger.info("========= Generating a configuration file for PyAgent =========")
		self.__getSrcServers()
		self.__getDstServers()
		self.__getDataMappings()
		
		self.__createConfigurationFile()
		
	def __configureLogger(self):
		class GeneratorFormatter(logging.Formatter):
			def __init__(self):
				logging.Formatter.__init__(self, "[generator]  %(message)s", None)
		
		class GeneratorHandler(logging.StreamHandler):
			def __init__(self):
				logging.StreamHandler.__init__(self)
				self.setFormatter(GeneratorFormatter())
		
		self.__logger = logging.getLogger(__name__)
		self.__logger.addHandler(GeneratorHandler())
		self.__logger.propagate = False
		
	def __getSrcServers(self):
		self.__logger.info("*** Configuring source servers")
		self.__logger.info("Define a new source server...")
		self.__tryAddNewSrcServer()
			
		#Show currently defined servers
		self.__logger.info("Defined source servers:")
		self.__printList(self.__generatedSettings.getSrcServers())
		
		while self.__getValue("Define a new source server? [Y/n]").lower() != "n":
			self.__tryAddNewSrcServer()
			
			#Show currently defined servers
			self.__logger.info("Defined source servers:")
			self.__printList(self.__generatedSettings.getSrcServers())
			
	def __tryAddNewSrcServer(self):
		#Ask for the details of a new server
		name = self.__getNonEmptyValue("New server name:")
		
		if name in self.__generatedSettings.getSrcServers():
			self.__logger.info("Choose a new name, this one has been already used.")
		else:
			protocols = self.__getExistingSrcProtocols()
			protocol = self.__getValueFromList("Protocol:", protocols)
			uri, username, password = self.__getValues("Server uri:", "Username:", "Password:")
			
			srcServer = SrcServer(name, protocol, uri, username, password)
			self.__generatedSettings.getSrcServers()[srcServer.getName()] = srcServer
					
	def __getDstServers(self):
		self.__logger.info("*** Configuring destination servers")
		self.__logger.info("Define a new destination server...")
		self.__tryAddNewDstServer()
		
		#Show currently defined servers
		self.__logger.info("Defined destination servers:")
		self.__printList(self.__generatedSettings.getDstServers())
			
		while self.__getValue("Define a new destination server? [Y/n]").lower() != "n":
			self.__tryAddNewDstServer()
			
			#Show currently defined servers
			self.__logger.info("Defined destination servers:")
			self.__printList(self.__generatedSettings.getDstServers())
	
	def __tryAddNewDstServer(self):
		#Ask for the details of a new server
		name = self.__getNonEmptyValue("New server name:")
		
		if name in self.__generatedSettings.getDstServers():
			self.__logger.info("Choose a new name, this one has been already used.")
		else:
			protocols = self.__getExistingDstProtocols()
			protocol = self.__getValueFromList("Protocol:", protocols)
			uri, username, password = self.__getValues("Server uri:", "Username:", "Password:")
			
			dstServer = DstServer(name, protocol, uri, username, password)
			self.__generatedSettings.getDstServers()[dstServer.getName()] = dstServer
	
	def __getExistingDstProtocols(self):
		dataSenderFactory = DataSenderFactory();
		protocols = [
			name[:name.find("DataSender")].lower() for name in dataSenderFactory.getDataSenderNames()
		]
		return protocols
	
	def __getExistingSrcProtocols(self):
		dataProviderFactory = DataProviderFactory();
		protocols = [
			name[:name.find("DataProvider")].lower() for name in dataProviderFactory.getDataProviderNames()
		]
		return protocols
	
	def __getDataMappings(self):
		self.__logger.info("*** Configuring data mappings")
			
		while self.__getValue("Define a new data mapping? [Y/n]").lower() != "n":
			self.__tryAddNewDataMapping()
			
	def __tryAddNewDataMapping(self):
		srcServers = self.__generatedSettings.getSrcServers()
		srcServer = self.__getSourceServer(srcServers)
		
		mappedObject = self.__getMappedObject()

		self.__logger.info("*** Where to send the data provided by the source server?")
		self.__logger.info("Define a new destination server mapping...")
		dstServersMappings = []
		dstServers = self.__generatedSettings.getDstServers()
		
		while True:
			dstServer = self.__getDestinationServer(dstServers)
			mapTo = self.__getValue("Choose a property to which data should be bound.")
			
			while True:
				try:
					updateInterval = int(self.__getValue("How often to refresh the measurement (in seconds)?"))
					
					if updateInterval >= 0:
						break
				except ValueError:
					pass
				
				self.__logger.info("Enter a non-negative integer value.")
			
			dstServerMapping = DstServerMapping(dstServer, mapTo, updateInterval)
			dstServersMappings.append(dstServerMapping)
			
			self.__logger.info("*** Do you want to send the same data somewhere else as well?")
			if self.__getValue("Define a new destination server mapping? [Y/n]").lower() == "n":
				break
		
		dataMapping = DataMapping(srcServer, mappedObject, dstServersMappings)
		self.__generatedSettings.getDataMappings().append(dataMapping)
	
	def __getSourceServer(self, srcServers):
		self.__logger.info("*** Where to take the data from?")
		srcServerName = self.__getValueFromList("Source server:", srcServers)
				
		return srcServers[srcServerName]
	
	def __getDestinationServer(self, dstServers):
		dstServerName = self.__getValueFromList("Destination server:", dstServers)
		
		return dstServers[dstServerName]
		
	def __getMappedObject(self):
		self.__logger.info("*** How to select data from the server you have just chosen?")
		mappedObject = MappedObject(
			*self.__getValues("Namespace:", "Name:", "Index (instance number):", "Attribute:")
		)
		
		return mappedObject
	
	def __getValue(self, message):
		self.__logger.info(message)
		
		return self.__input()
	
	def __getValues(self, *messages):
		values = []
		
		for message in messages:
			values.append(self.__getValue(message))
			
		return values
		
	def __getValueFromList(self, message, values):
		self.__logger.info(message)
		
		while True:
			self.__logger.info("Select one of: [{0}]".format(", ".join(values)))
			value = self.__input()
		
			if value in values:
				return value
	
	def __getNonEmptyValue(self, message):
		while True:
			value = self.__getValue(message)
			
			if value != "":
				return value
			
	def __printList(self, elements):
		i = 1
		for element in elements:
			self.__logger.info("\t{0}) {1}".format(i, element))
			i += 1	
		self.__logger.info("")
		
	def __createConfigurationFile(self):
		root = etree.Element("settings")
		srcServersNode = etree.SubElement(root, "src-servers")
		
		for srcServer in self.__generatedSettings.getSrcServers().values():
			srcServerNode = etree.SubElement(srcServersNode, "src-server")
			etree.SubElement(srcServerNode, "name").text = srcServer.getName()
			etree.SubElement(srcServerNode, "protocol").text = srcServer.getProtocol()
			etree.SubElement(srcServerNode, "uri").text = srcServer.getUri()
			etree.SubElement(srcServerNode, "username").text = srcServer.getUsername()
			etree.SubElement(srcServerNode, "password").text = srcServer.getPassword()
			
		dstServersNode = etree.SubElement(root, "dst-servers")
		
		for dstServer in self.__generatedSettings.getDstServers().values():
			dstServerNode = etree.SubElement(dstServersNode, "dst-server")
			etree.SubElement(dstServerNode, "name").text = dstServer.getName()
			etree.SubElement(dstServerNode, "protocol").text = dstServer.getProtocol()
			etree.SubElement(dstServerNode, "uri").text = dstServer.getUri()
			etree.SubElement(dstServerNode, "username").text = dstServer.getUsername()
			etree.SubElement(dstServerNode, "password").text = dstServer.getPassword()
		
		dataMappingsNode = etree.SubElement(root, "data-mappings")
		
		for dataMapping in self.__generatedSettings.getDataMappings():
			dataMappingNode = etree.SubElement(dataMappingsNode, "data-mapping")
			srcServerRef = etree.SubElement(dataMappingNode, "src-server")
			etree.SubElement(srcServerRef, "name").text = dataMapping.getSrcServer().getName()
			
			mappedObjectNode = etree.SubElement(dataMappingNode, "mapped-object")
			etree.SubElement(mappedObjectNode, "namespace").text = dataMapping.getMappedObject().getNamespace()
			etree.SubElement(mappedObjectNode, "name").text = dataMapping.getMappedObject().getName()
			etree.SubElement(mappedObjectNode, "index").text = dataMapping.getMappedObject().getIndex()
			etree.SubElement(mappedObjectNode, "attribute").text = dataMapping.getMappedObject().getAttribute()
		
			dstServersMappingsNode = etree.SubElement(dataMappingNode, "dst-servers-mappings")
			
			for dstServerMapping in dataMapping.getDstServersMappings():
				dstServerMappingNode = etree.SubElement(dstServersMappingsNode, "dst-server-mapping")
				etree.SubElement(dstServerMappingNode, "name").text = dstServerMapping.getDstServer().getName()
				etree.SubElement(dstServerMappingNode, "map-to").text = dstServerMapping.getMapTo()
				etree.SubElement(dstServerMappingNode, "update-interval").text = str(int(dstServerMapping.getUpdateInterval().total_seconds()))
		
		etree.SubElement(root, "callbacks")
		
		etree.ElementTree(element=root).write(
			self.__settings.getConfigurationFile(),
			xml_declaration=True,
			encoding="utf-8",
			pretty_print=True
		)
