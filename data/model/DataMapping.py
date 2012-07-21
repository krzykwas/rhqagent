#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
#

class DataMapping(object):
	"""
	Data mapping between two servers - one providing data and one receiving data
	"""

	def __init__(self, srcServer, mappedObject, dstServersMappings):
		self.__srcServer = srcServer
		self.__mappedObject = mappedObject
		self.__dstServersMappings = dstServersMappings

	def getSrcServer(self):
		return self.__srcServer

	def getMappedObject(self):
		return self.__mappedObject

	def getDstServersMappings(self):
		return self.__dstServersMappings
	
	def __str__(self):
		return "{0}.{1}.{2}@{3}".format(
			self.__mappedObject.getName(),
			self.__mappedObject.getIndex(),
			self.__mappedObject.getAttribute(),
			self.__srcServer.getName()
		)
