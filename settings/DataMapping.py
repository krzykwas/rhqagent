#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
#

class DataMapping(object):
	"""
	Data mapping between two servers - one providing data and one receiving data
	"""

	def __init__(self, srcServer, mappedObject, updatePeriod, dstServersMappings):
		self.__srcServer = srcServer
		self.__mappedObject = mappedObject
		self.__updatePeriod = updatePeriod
		self.__dstServersMappings = dstServersMappings

	def getSrcServer(self):
		return self.__srcServer

	def getMappedObject(self):
		return self.__mappedObject

	def getUpdatePeriod(self):
		return self.__updatePeriod

	def getDstServersMappings(self):
		return self.__dstServersMappings