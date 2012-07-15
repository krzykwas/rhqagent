#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 30-05-2012
#

class SrcServer(object):
	"""
	Represents a server that provides metric data to be passed to an RHQ server.
	Two SrcServer instances are equal, if they have equal fields.
	"""

	def __init__(self, name, protocol, uri, username, password):
		self.__name = name
		self.__protocol = protocol
		self.__uri = uri
		self.__username = username
		self.__password = password
		
	def __eq__(self, other):
		return self.__name == other.getName()\
			and self.__protocol == other.getProtocol()\
			and self.__uri == other.getUri()\
			and self.__username == other.getUsername()\
			and self.__password == other.getPassword()
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		prime = 13
		result = 1
		result = prime * result + self.__name.__hash__()
		result = prime * result + self.__protocol.__hash__()
		result = prime * result + self.__uri.__hash__()
		result = prime * result + self.__username.__hash__()
		result = prime * result + self.__password.__hash__()
		
		return result
	
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
