#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 30-05-2012
#

class Server(object):
	"""
	Represents a server that provides metric data to be passed to an RHQ server.
	"""

	def __init__(self, protocol, username, password, uri):
		self.__protocol = protocol
		self.__username = username
		self.__password = password
		self.__uri = uri
	
	def getProtocol(self):
		return self.__protocol

	def getUsername(self):
		return self.__username
	
	def getPassword(self):
		return self.__password
	
	def getUri(self):
		return self.__uri