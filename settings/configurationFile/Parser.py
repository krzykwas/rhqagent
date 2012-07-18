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
from data.model.callback.Callback import Callback
from data.model.callback.Param import Param
import lxml.etree
import xml.etree.ElementTree

class Parser(object):
	"""
	Parses an xml settings file - checks it for validity against schema,
	reads its contents and fills a Settings object with obtained data.
	"""

	def __init__(self, settings, configurationFile, schemaPath):
		self.__settings = settings
		self.__configurationFile = configurationFile
		self.__schemaPath = schemaPath

	def parse(self):
		config = xml.etree.ElementTree.parse(self.__configurationFile)
		self.__validateAgainstSchema()
		
		root = config.getroot()
		
		self.__parseSrcServers(root.find("src-servers"))
		self.__parseDstServers(root.find("dst-servers"))
		self.__parseDataMappings(root.find("data-mappings"))
		self.__parseCallbacks(root.find("callbacks"))
				
	def __validateAgainstSchema(self):
		schema_doc = lxml.etree.parse(self.__schemaPath)
		schema = lxml.etree.XMLSchema(schema_doc)
		xml = lxml.etree.parse(self.__configurationFile)
		
		valid = schema.validate(xml)
		
		if not valid:
			raise ValueError("Configuration file invalid", schema.error_log)
	
	def __parseSrcServers(self, node):
		for serverNode in node.findall("src-server"):
			name = serverNode.find("name").text
			protocol = serverNode.find("protocol").text
			uri = serverNode.find("uri").text
			username = serverNode.find("username").text
			password = serverNode.find("password").text
			
			srcServer = SrcServer(name, protocol, uri, username, password)
			self.__settings.getSrcServers()[name] = srcServer
			
	def __parseDstServers(self, node):
		for serverNode in node.findall("dst-server"):
			name = serverNode.find("name").text
			protocol = serverNode.find("protocol").text
			uri = serverNode.find("uri").text
			username = serverNode.find("username").text
			password = serverNode.find("password").text
			
			dstServer = DstServer(name, protocol, uri, username, password)
			self.__settings.getDstServers()[name] = dstServer
			
	def __parseDataMappings(self, node):
		for dataMappingNode in node.findall("data-mapping"):
			srcServerName = dataMappingNode.find("src-server").find("name").text
			
			try:
				srcServer = self.__settings.getSrcServers()[srcServerName]
			except KeyError:
				raise ValueError("Unknown source server {0} in data-mapping.".format(srcServerName))

			mappedObject = self.__parseMappedObject(dataMappingNode.find("mapped-object"))
			dstServersMappings = self.__parseDstServersMappings(dataMappingNode.find("dst-servers-mappings"))
			
			dataMapping = DataMapping(srcServer, mappedObject, dstServersMappings)
			self.__settings.getDataMappings().append(dataMapping)
			
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
				dstServer = self.__settings.getDstServers()[name]
			except KeyError:
				raise ValueError("Unknown destination server {0} in data-mapping.".format(name))
			
			dstServerMapping = DstServerMapping(dstServer, mapTo, updateInterval)
			dstServersMappings.append(dstServerMapping)
				
		return dstServersMappings
	
	def __parseCallbacks(self, node):
		for callbackNode in node.findall("callback"):
			functionCode = callbackNode.find("function").text
			params = self.__parseParams(callbackNode.find("params"))
			dstServersMappings = self.__parseDstServersMappings(callbackNode.find("dst-servers-mappings"))
			
			callback = Callback(functionCode, params, dstServersMappings)
			self.__settings.getCallbacks().append(callback)
	
	def __parseParams(self, node):
		params = []
		
		for paramNode in node.findall("param"):
			srcServerName = paramNode.find("src-server").find("name").text
			
			try:
				srcServer = self.__settings.getSrcServers()[srcServerName]
			except KeyError:
				raise ValueError("Unknown source server {0} in data-mapping.".format(srcServerName))

			mappedObject = self.__parseMappedObject(paramNode.find("mapped-object"))
			
			param = Param(srcServer, mappedObject)
			params.append(param)
			
		return params
