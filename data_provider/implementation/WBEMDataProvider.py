#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 25-05-2012
#

from ..AbstractDataProvider import AbstractDataProvider
import pywbem

class WBEMDataProvider(AbstractDataProvider):
	
	def __init__(self, srcServer):
		AbstractDataProvider.__init__(self, srcServer)
		
		self.__connection = None
	
	def authenticate(self):
		"""
		Prepares a connection to a CIM server.
		"""
		srcServer = self.getSrcServer()
		uri = srcServer.getUri()
		username = srcServer.getUsername()
		password = srcServer.getPassword()
		
		self.__connection = pywbem.WBEMConnection(uri, (username, password))
	
	def connect(self):
		"""
		Doesn't do anything as all the work is done in authenticate().
		"""
		pass
	
	def getData(self, mappedObject):
		name = mappedObject.getName()
		namespace = mappedObject.getNamespace()
		index = int(mappedObject.getIndex())
		attribute = mappedObject.getAttribute()
		
		instances = self.__connection.EnumerateInstances(name, namespace)
		instance = instances[index]
		
		return instance[attribute]