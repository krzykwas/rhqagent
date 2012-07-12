#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 19-05-2012
#

from data.model.Callback import Callback
from data.model.DataMapping import DataMapping
from data.model.DstServer import DstServer
from data.model.DstServerMapping import DstServerMapping
from data.model.MappedObject import MappedObject
from data.model.Param import Param
from data.model.SrcServer import SrcServer
import argparse
import logging
import lxml.etree
import xml.etree.ElementTree

class Settings(object):
	"""
	Responsible for merging configuration for PyAgent coming from different sources - like 
	command line arguments and configuration files.
	"""

	def __init__(self):
		self.__configurationFile = ""	#Configuration file
		self.__srcServers = {}			#Servers providing data
		self.__dstServers = {}			#Servers accepting data
		self.__dataMappings = []		#Mappings between resources in srcServers and dstServers
		self.__callbacks = []			#User-defined callbacks allowing for calculation of artificial metrics
		
		self.__logger = logging.getLogger(__name__)
		self.__schemaPath = "settings/settings.xsd"

	def getCallbacks(self):
		return self.__callbacks

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

	def __validateAgainstSchema(self):
		schema_doc = lxml.etree.parse(self.__schemaPath)
		schema = lxml.etree.XMLSchema(schema_doc)
		xml = lxml.etree.parse(self.__configurationFile)
		
		valid = schema.validate(xml)
		
		if not valid:
			raise ValueError("Configuration file invalid", schema.error_log)

	def __parseConfigurationFile(self):
		config = xml.etree.ElementTree.parse(self.__configurationFile)
		self.__validateAgainstSchema()
		
		root = config.getroot()
		
		self.__parseSrcServers(root.find("src-servers"))
		self.__parseDstServers(root.find("dst-servers"))
		self.__parseDataMappings(root.find("data-mappings"))
		self.__parseCallbacks(root.find("callbacks"))
			
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
			
			try:
				srcServer = self.__srcServers[srcServerName]
			except KeyError:
				raise ValueError("Unknown source server {0} in data-mapping.".format(srcServerName))

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

			try:
				dstServer = self.__dstServers[name]
			except KeyError:
				raise ValueError("Unknown destination server {0} in data-mapping.".format(name))
			
			dstServerMapping = DstServerMapping(dstServer, mapTo, updateInterval)
			dstServersMappings.append(dstServerMapping)
				
		return dstServersMappings
	
	def __parseCallbacks(self, node):
		callbacks = []
		
		for callbackNode in node.findall("callback"):
			functionCode = callbackNode.find("function").text
			params = self.__parseParams(callbackNode.find("params"))
			dstServersMappings = self.__parseDstServersMappings(callbackNode.find("dst-servers-mappings"))
			
			callback = Callback(functionCode, params, dstServersMappings)
			callbacks.append(callback)
		
		return callbacks
	
	def __parseParams(self, node):
		params = []
		
		for paramNode in node.findall("param"):
			srcServerName = paramNode.find("src-server").find("name").text
			
			try:
				srcServer = self.__srcServers[srcServerName]
			except KeyError:
				raise ValueError("Unknown source server {0} in data-mapping.".format(srcServerName))

			mappedObject = self.__parseMappedObject(paramNode.find("mapped-object"))
			
			param = Param(srcServer, mappedObject)
			params.append(param)
			
		return params
