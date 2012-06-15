#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 19-05-2012
#

from DstServer import DstServer
from SrcServer import SrcServer
from settings.DataMapping import DataMapping
from settings.DstServerMapping import DstServerMapping
from settings.MappedObject import MappedObject
from xml.etree import ElementTree
import argparse

class Settings(object):
	"""
	Responsible for merging configuration for PyAgent coming from different sources - like 
	command line arguments and configuration files. That in the future, for now only command 
	line options are supported.
	"""

	def __init__(self):
		"""
		Set default arguments in here
		"""

		self.__configurationFile = ""	#Configuration file
		self.__srcServers = {}			#Servers providing data
		self.__dstServers = {}			#Servers accepting data
		self.__dataMappings = []		#Mappings between resources in srcServers and dstServers

	def getSrcServers(self):
		return self.__srcServers
	
	def getDstServers(self):
		return self.__dstServers
	
	def getDataMappings(self):
		return self.__dataMappings
	
	def updateWithCommandLine(self):
		parser = argparse.ArgumentParser(
			description="An agent passing metrics data to an RHQ server"
		)
		parser.add_argument(
			"--configuration-file",
			required=True,
			help="""Configuration file"""
		)
		
		args = parser.parse_args()

		self.__configurationFile = args.configuration_file
		self.__parseConfigurationFile()

	def __parseConfigurationFile(self):
		xml = ElementTree.parse(self.__configurationFile)
		root = xml.getroot()
		
		self.__parseSrcServers(root.find("src-servers"))
		self.__parseDstServers(root.find("dst-servers"))
		self.__parseDataMappings(root.find("data-mappings"))
			
	def __parseSrcServers(self, node):
		for serverNode in node.findall("src-server"):
			name = serverNode.find("name").text
			protocol = serverNode.find("protocol").text
			uri = serverNode.find("uri").text
			username = serverNode.find("username").text
			password = serverNode.find("password").text
			
			srcServer = SrcServer(name, protocol, uri, username, password)
			self.__srcServers[name] = srcServer
			
	def __parseDstServers(self, node):
		for serverNode in node.findall("dst-server"):
			name = serverNode.find("name").text
			protocol = serverNode.find("protocol").text
			uri = serverNode.find("uri").text
			username = serverNode.find("username").text
			password = serverNode.find("password").text
			
			dstServer = DstServer(name, protocol, uri, username, password)
			self.__dstServers[name] = dstServer
			
	def __parseDataMappings(self, node):
		for dataMappingNode in node.findall("data-mapping"):
			srcServerName = dataMappingNode.find("src-server").find("name").text
			srcServer = self.__srcServers[srcServerName]
			
			mappedObject = self.__parseMappedObject(dataMappingNode.find("mapped-object"))
			dstServersMappings = self.__parseDstServersMappings(dataMappingNode.find("dst-servers-mappings"))
			
			dataMapping = DataMapping(srcServer, mappedObject, dstServersMappings)
			self.__dataMappings.append(dataMapping)
			
	def __parseMappedObject(self, node):
		namespace = node.find("namespace").text
		name = node.find("name").text
		index = node.find("index").text
		attribute = node.find("attribute").text
		
		return MappedObject(namespace, name, index, attribute)
	
	def __parseDstServersMappings(self, node):
		dstServersMappings = []

		for dstServerMappingNode in node.findall("dst-server-mapping"):
			name = dstServerMappingNode.find("name").text
			mapTo = dstServerMappingNode.find("map-to").text
			updateInterval = dstServerMappingNode.find("update-interval").text
				
			dstServer = self.__dstServers[name]
			dstServerMapping = DstServerMapping(dstServer, mapTo, updateInterval)
			dstServersMappings.append(dstServerMapping)
				
		return dstServersMappings