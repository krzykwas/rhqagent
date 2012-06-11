#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
#

class DstServerMapping(object):
	
	def __init__(self, dstServer, mapTo, updatePeriod):
		self.__dstServer = dstServer
		self.__mapTo = mapTo
		self.__updatePeriod = updatePeriod
		
	def getDstServer(self):
		return self.__dstServer
	
	def getMapTo(self):
		return self.__mapTo
	
	def getUpdatePeriod(self):
		return self.__updatePeriod