#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 18-07-2012
#

from data.model.SrcServer import SrcServer
from data.provider.DataProviderFactory import DataProviderFactory
import logging

class Generator(object):
	"""
	Interactively generates a configuration file
	"""

	def __init__(self, settings):
		self.__settings = settings
		self.__logger = logging.getLogger(__name__)
		
		#For compatibility between Python 2.x and 3.x
		try:
			self.__input = raw_input
		except:
			self.__input = input
		
	def generate(self):
		self.__logger.info("========= Generating a configuration file for PyAgent =========")
		srcServers = self.__getSrcServers()
		self.__settings.getSrcServers().update(srcServers)
		
	def __getSrcServers(self):
		srcServers = {}
		
		while True:
			self.__logger.info("Define a new source server? [Y/n]")
			response = self.__input()
			
			if response.lower() == "n":
				break

			#Ask for the details of a new server
			while True:
				self.__logger.info("New server name:")
				name = self.__input()
				
				if name != "":
					break
			
			if name in srcServers:
				self.__logger.info("Choose a new name, this one has been already used")
			else:
				protocols = self.__getExistingSrcProtocols()
				self.__logger.info("Protocol:")
				self.__logger.info("[{0}]".format(" ,".join(protocols)))
				protocol = self.__input()
				
				if protocol not in protocols:
					self.__logger.info("Choose a protocol from the list above")
				else:
					self.__logger.info("Server uri:")
					uri = self.__input()
					self.__logger.info("Username:")
					username = self.__input()
					self.__logger.info("Password:")
					password = self.__input()
					
					srcServer = SrcServer(name, protocol, uri, username, password)
					srcServers[srcServer.getName()] = srcServer
				
			#Show currently defined servers
			self.__logger.info("Defined source servers:")
			self.__printList(srcServers)
		
		return srcServers
	
	def __getExistingSrcProtocols(self):
		dataProviderFactory = DataProviderFactory();
		protocols = [
			name[:name.find("DataProvider")].lower() for name in dataProviderFactory.getDataProviderNames()
		]
		return protocols
	
	def __printList(self, elements):
		i = 1
		for element in elements:
			self.__logger.info("\t{0}) {1}".format(i, element))
			i += 1	
		self.__logger.info("")
