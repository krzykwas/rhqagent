#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 25-05-2012
#

from ..AbstractDataProvider import AbstractDataProvider
from pywbem.cim_http import AuthError
from pywbem.cim_operations import CIMError
import logging
import pywbem
import thread

class WBEMDataProvider(AbstractDataProvider):
	
	def __init__(self, srcServer):
		AbstractDataProvider.__init__(self, srcServer)
		
		self.__connection = None
		self.__logger = logging.getLogger(__name__)
	
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
		
		try:
			instances = self.__connection.EnumerateInstances(name, namespace)
			instance = instances[index]
		
			return instance[attribute]
		except AuthError:
			self.__logger.critical("Wrong authentication credentials for {0}.".format(self.getSrcServer().getName()))
			thread.interrupt_main()
		except CIMError as e:
			self.__logger.error("CIM exception for {0}: {1}".format(self.getSrcServer().getName(), e.args))
