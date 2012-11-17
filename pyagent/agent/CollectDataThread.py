# -*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-06-2012
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from ..data.model.Measurement import Measurement
from threading import Thread
import logging
import time

class CollectDataThread(Thread):
	
	def __init__(self, args):
		Thread.__init__(self, args=args)
		self.setDaemon(True)
		
		self.__pyAgent = args[0]
		self.__dataProviders = self.__pyAgent.getDataProviders()
		self.__pastMeasurementsManager = self.__pyAgent.getPastMeasurementsManager()
		
		self.__logger = logging.getLogger(__name__)	
		self.__logger.debug("Starting collecting data")

	def run(self):
		settings = self.__pyAgent.getSettings()
		dataMappings = settings.getDataMappings()
		callbacks = settings.getCallbacks()
		
		while True:
			for dataMapping in dataMappings:
				self.handleDataMapping(dataMapping)

			for callback in callbacks:
				self.handleCallback(callback)
			
			time.sleep(1)	
			
	def handleDataMapping(self, dataMapping):
		srcServer = dataMapping.getSrcServer()
		mappedObject = dataMapping.getMappedObject()
		dataProvider = self.__dataProviders[srcServer]
		value = dataProvider.getData(mappedObject)
		timestamp = time.time()
		
		if value is None:
			return
				
		for dstServerMapping in dataMapping.getDstServersMappings():
			if dstServerMapping.isDue():
				measurement = Measurement(srcServer, mappedObject, dstServerMapping, value, timestamp)
				
				self.__logger.debug("Metric for {0} takes value {1}".format(dataMapping, value))
				
				self.__pyAgent.getMetricsDataQueue().put(measurement)
				dstServerMapping.setLastAccessedNow()
				
				self.__pastMeasurementsManager.put(srcServer, mappedObject, measurement)
				
	def handleCallback(self, callback):
		timestamp = time.time()
		
		for dstServerMapping in callback.getDstServersMappings():
			if dstServerMapping.isDue():
				params = []
				
				for param in callback.getParams():
					srcServer = param.getSrcServer()
					mappedObject = param.getMappedObject()
					dataProvider = self.__dataProviders[srcServer]
					value = dataProvider.getData(mappedObject)
			
					measurement = Measurement(srcServer, mappedObject, dstServerMapping, value, timestamp)

					self.__pastMeasurementsManager.put(srcServer, mappedObject, measurement)
					params.append(self.__pastMeasurementsManager.get(srcServer, mappedObject))
					
				try:
					result = callback(params)

					temp = ", ".join([str(param) for param in callback.getParams()])
					self.__logger.debug("Artificial metric for {0} takes value {1}".format(temp, result))
				
					artificialMeasurement = Measurement(None, None, dstServerMapping, result, time.time())
				
					self.__pyAgent.getMetricsDataQueue().put(artificialMeasurement)
				except Exception as e:
					self.__logger.error("Callback error: {0}".format(e))
				finally:
					dstServerMapping.setLastAccessedNow()
