#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 30-05-2012
#

class SrcServer(object):
	"""
	Represents a server that provides metric data to be passed to an RHQ server.
	"""

	def __init__(self, name, protocol, uri, username, password):
		self.__name = name
		self.__protocol = protocol
		self.__uri = uri
		self.__username = username
		self.__password = password
	
	def getName(self):
		return self.__name
	
	def getProtocol(self):
		return self.__protocol
	
	def getUri(self):
		return self.__uri
	
	def getUsername(self):
		return self.__username
	
	def getPassword(self):
		return self.__password