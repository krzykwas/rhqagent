#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
#

class DstServerMapping(object):
	
	def __init__(self, dstServer, mapTo, updatePeriod):
		"""
		@param dstServer: describes the server to which collected data is sent
		@param mapTo: an identifier of a dstServer's resource to which data is mapped,
			for instance for RHQ it wolud be a scheduleId
		@param updatePeriod: how often to refresh the measurement
		"""
		
		self.__dstServer = dstServer
		self.__mapTo = mapTo
		self.__updatePeriod = updatePeriod
		
	def getDstServer(self):
		return self.__dstServer
	
	def getMapTo(self):
		return self.__mapTo
	
	def getUpdatePeriod(self):
		return self.__updatePeriod