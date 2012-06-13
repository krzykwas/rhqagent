#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 13-06-2012
#

class Measurement(object):
	"""
	Represents a single measurement taken at intervals specified by the user.
	Data is taken from a certain source server and sent to a destination server.
	"""

	def __init__(self, srcServer, mappedObject, dstServerMapping, value):
		"""
		@param srcServer: describes the source server that provides data  
		@param mappedObject: serves to locate the monitored object in the source server
		@param dstServerMapping: contains information on the destination server to which data is sent
		@param value: the value of the measurement
		"""
		
		self.__mappedObject = mappedObject
		self.__srcServer = srcServer
		self.__dstServerMapping = dstServerMapping
		self.__value = value

	def getMappedObject(self):
		return self.__mappedObject

	def getSrcServer(self):
		return self.__srcServer

	def getDstServerMapping(self):
		return self.__dstServerMapping

	def getValue(self):
		return self.__value	