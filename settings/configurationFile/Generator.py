#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 18-07-2012
#

from data.model.DstServer import DstServer
from data.model.SrcServer import SrcServer
from data.provider.DataProviderFactory import DataProviderFactory
from data.sender.DataSenderFactory import DataSenderFactory
from settings.Settings import Settings
import logging

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
		
		self.__logger = logging.getLogger(__name__)
		
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
		
	def __getSrcServers(self):
		self.__logger.info("*** Configuring source servers")
		self.__logger.info("Define a new source server...")
		self.__tryAddNewSrcServer()
			
		#Show currently defined servers
		self.__logger.info("Defined source servers:")
		self.__printList(self.__generatedSettings.getSrcServers())
		
		while True:
			self.__logger.info("Define a new source server? [Y/n]")
			response = self.__input()
			
			if response.lower() == "n":
				break

			self.__tryAddNewSrcServer()
			
			#Show currently defined servers
			self.__logger.info("Defined source servers:")
			self.__printList(self.__generatedSettings.getSrcServers())
			
	def __tryAddNewSrcServer(self):
		#Ask for the details of a new server
		name = self.__getNonEmptyValue("New server name:")
		
		if name in self.__generatedSettings.getSrcServers():
			self.__logger.info("Choose a new name, this one has been already used")
		else:
			while True:
				protocols = self.__getExistingSrcProtocols()
				self.__logger.info("Protocol:")
				self.__logger.info("[{0}]".format(" ,".join(protocols)))
				protocol = self.__input()
				
				if protocol in protocols:
					break
				else:
					self.__logger.info("Choose a protocol from the list below")
			
			self.__logger.info("Server uri:")
			uri = self.__input()
			self.__logger.info("Username:")
			username = self.__input()
			self.__logger.info("Password:")
			password = self.__input()
			
			srcServer = SrcServer(name, protocol, uri, username, password)
			self.__generatedSettings.getSrcServers()[srcServer.getName()] = srcServer
					
	def __getDstServers(self):
		self.__logger.info("*** Configuring destination servers")
		self.__logger.info("Define a new destination server...")
		self.__tryAddNewDstServer()
		
		#Show currently defined servers
		self.__logger.info("Defined destination servers:")
		self.__printList(self.__generatedSettings.getDstServers())
			
		while True:
			self.__logger.info("Define a new destination server? [Y/n]")
			response = self.__input()
			
			if response.lower() == "n":
				break

			self.__tryAddNewDstServer()
			
			#Show currently defined servers
			self.__logger.info("Defined destination servers:")
			self.__printList(self.__generatedSettings.getDstServers())
	
	def __tryAddNewDstServer(self):
		#Ask for the details of a new server
		name = self.__getNonEmptyValue("New server name:")
		
		if name in self.__generatedSettings.getDstServers():
			self.__logger.info("Choose a new name, this one has been already used")
		else:
			while True:
				protocols = self.__getExistingDstProtocols()
				self.__logger.info("Protocol:")
				self.__logger.info("[{0}]".format(" ,".join(protocols)))
				protocol = self.__input()

				if protocol in protocols:
					break			
				else:
					self.__logger.info("Choose a protocol from the list below")

			self.__logger.info("Server uri:")
			uri = self.__input()
			self.__logger.info("Username:")
			username = self.__input()
			self.__logger.info("Password:")
			password = self.__input()
			
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
			
		while True:
			self.__logger.info("Define a new data mapping? [Y/n]")
			response = self.__input()
			
			if response.lower() == "n":
				break

			self.__tryAddNewDataMapping()
			
	def __tryAddNewDataMapping(self):
		pass
	
	def __getNonEmptyValue(self, message):
		while True:
			self.__logger.info(message)
			value = self.__input()
			
			if value != "":
				return value
			
	def __printList(self, elements):
		i = 1
		for element in elements:
			self.__logger.info("\t{0}) {1}".format(i, element))
			i += 1	
		self.__logger.info("")
