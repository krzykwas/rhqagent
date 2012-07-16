#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-06-2012
#

from data.model.Measurement import Measurement
from threading import Thread
import time

class CollectDataThread(Thread):
	
	def __init__(self, args):
		Thread.__init__(self, args=args)
		self.setDaemon(True)
		
		self.__pyAgent = args[0]
		self.__dataProviders = self.__pyAgent.getDataProviders()
		self.__pastMeasurementsManager = self.__pyAgent.getPastMeasurementsManager()

	def run(self):
		settings = self.__pyAgent.getSettings()
		dataMappings = settings.getDataMappings()
		callbacks = settings.getCallbacks()
		
		while True:
			for dataMapping in dataMappings:
				self.__handleDataMapping(dataMapping)

			for callback in callbacks:
				self.__handleCallback(callback)
				
			time.sleep(1)
			
	def __handleDataMapping(self, dataMapping):
		srcServer = dataMapping.getSrcServer()
		mappedObject = dataMapping.getMappedObject()
		dataProvider = self.__dataProviders[srcServer]
		value = dataProvider.getData(mappedObject)
		timestamp = time.time()
				
		for dstServerMapping in dataMapping.getDstServersMappings():
			if dstServerMapping.isDue():
				measurement = Measurement(
					srcServer,
					mappedObject,
					dstServerMapping,
					value,
					timestamp
				)
				
				self.__pyAgent.getMetricsDataQueue().put(measurement)
				dstServerMapping.setLastAccessedNow()
				
				self.__pastMeasurementsManager.put(srcServer, mappedObject, measurement)
				
	def __handleCallback(self, callback):
		timestamp = time.time()
		
		for dstServerMapping in callback.getDstServersMappings():
			if dstServerMapping.isDue():
				params = []
				
				for param in callback.getParams():
					srcServer = param.getSrcServer()
					mappedObject = param.getMappedObject()
					dataProvider = self.__dataProviders[srcServer]
					value = dataProvider.getData(mappedObject)
			
					measurement = Measurement(
						srcServer,
						mappedObject,
						dstServerMapping,
						value,
						timestamp
					)

					self.__pastMeasurementsManager.put(srcServer, mappedObject, measurement)
					params.append(self.__pastMeasurementsManager.get(srcServer, mappedObject))
					
				result = callback(params)
				artificialMeasurement = Measurement(None, None, dstServerMapping, result, time.time())
				
				self.__pyAgent.getMetricsDataQueue().put(artificialMeasurement)
				dstServerMapping.setLastAccessedNow()
