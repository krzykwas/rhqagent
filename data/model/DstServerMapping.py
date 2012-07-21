#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
#

from datetime import datetime
from datetime import timedelta

class DstServerMapping(object):
	
	def __init__(self, dstServer, mapTo, updateInterval):
		"""
		@param dstServer: describes the server to which collected data is sent
		@param mapTo: an identifier of a dstServer's resource to which data is mapped,
			for instance for RHQ it wolud be a scheduleId
		@param updateInterval: how often to refresh the measurement
		"""
		
		self.__dstServer = dstServer
		self.__mapTo = mapTo
		self.__lastAccessed = datetime.min;
		
		self.setUpdateInterval(updateInterval)
		
	def getDstServer(self):
		return self.__dstServer
	
	def getMapTo(self):
		return self.__mapTo
	
	def getUpdateInterval(self):
		return self.__updateInterval
	
	def setUpdateInterval(self, updateInterval):
		if isinstance(updateInterval, timedelta):
			self.__updateInterval = updateInterval
		else:
			self.__updateInterval = timedelta(seconds=int(updateInterval))
	
	def isDue(self):
		return (self.__lastAccessed + self.__updateInterval) < datetime.now()
	
	def setLastAccessedNow(self):
		self.__lastAccessed = datetime.now()
