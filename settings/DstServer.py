#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
#

class DstServer(object):
	"""
	Represents a server receiving data, so far it will be always an RHQ server.
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