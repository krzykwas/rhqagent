#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-07-2012
#

class Param(object):
	"""
	Callback parameter - holds info about a server that should be queried for param value
	"""

	def __init__(self, srcServer, mappedObject):
		self.__srcServer = srcServer
		self.__mappedObject = mappedObject
		
	def getSrcServer(self):
		return self.__srcServer
	
	def getMappedObject(self):
		return self.__mappedObject
	
	def __str__(self):
		return "{0}.{1}.{2}@{3}".format(
			self.__mappedObject.getName(),
			self.__mappedObject.getIndex(),
			self.__mappedObject.getAttribute(),
			self.__srcServer.getName()
		)
