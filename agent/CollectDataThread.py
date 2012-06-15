#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-06-2012
#

from agent.Measurement import Measurement
from threading import Thread
import time

class CollectDataThread(Thread):
	
	def __init__(self, args):
		Thread.__init__(self, args=args)
		
		self.__stopped = False
		self.__pyAgent = args[0]

	def run(self):
		dataMappings = self.__pyAgent.getSettings().getDataMappings()
		
		while not self.__stopped:
			for dataMapping in dataMappings:
				self.__handleDataMapping(dataMapping)
				
			time.sleep(1)
			
	def __handleDataMapping(self, dataMapping):
		srcServer = dataMapping.getSrcServer()
		mappedObject = dataMapping.getMappedObject()
		dataProvider = self.__pyAgent.getDataProviders()[srcServer.getName()]
		value = dataProvider.getData(mappedObject)
				
		for dstServerMapping in dataMapping.getDstServersMappings():
			if dstServerMapping.isDue():
				measurement = Measurement(srcServer, mappedObject, dstServerMapping, value)
				self.__pyAgent.getMetricsDataQueue().put(measurement)
				
				dstServerMapping.setLastAccessedNow()
			
	def stop(self):
		self.__stopped = True