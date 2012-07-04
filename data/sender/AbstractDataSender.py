#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

from abc import ABCMeta
from abc import abstractmethod

class AbstractDataSender(object):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def __init__(self, dstServer):
		self.__dstServer = dstServer

	@abstractmethod
	def authenticate(self):
		"""
		Authenticates with dstServer.
		"""
		pass
	
	@abstractmethod
	def connect(self):
		"""
		Opens a connection to dstServer.
		"""
		pass
	
	@abstractmethod
	def sendAvailabilityState(self, state):
		"""
		Sends a periodical message indicating that
		either the agent is still alive or the opposite when it is going offline.
		"""
		pass
	
	@abstractmethod
	def sendData(self, mappedObject):
		"""
		Sends metric data.
		"""
		pass

	def getDstServer(self):
		return self.__dstServer
