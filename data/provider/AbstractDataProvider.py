#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

from abc import ABCMeta, abstractmethod

class AbstractDataProvider(object):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def __init__(self, srcServer):
		self.__srcServer = srcServer

	@abstractmethod
	def authenticate(self):
		"""
		Authenticates with srcServer.
		"""
		pass
	
	@abstractmethod
	def connect(self):
		"""
		Opens a connection to srcServer.
		"""
		pass
	
	@abstractmethod
	def getData(self, mappedObject):
		pass

	def getSrcServer(self):
		return self.__srcServer
