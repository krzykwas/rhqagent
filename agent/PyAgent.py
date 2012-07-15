#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

from agent.CollectDataThread import CollectDataThread
from agent.SendDataThread import SendDataThread
from data.model.PastMeasurementsManager import PastMeasurementsManager
from data.provider.DataProviderFactory import DataProviderFactory
from data.sender.DataSenderFactory import DataSenderFactory
import sys
import time

try:
	from queue import Queue #@UnresolvedImport
except:
	from Queue import Queue #@UnresolvedImport

class PyAgent(object):
	"""
	Responsible for gathering metrics data and passing it to an RHQ server.
	"""

	def __init__(self, settings):
		self.__settings = settings
		self.__dataProviderFactory = DataProviderFactory()
		self.__dataSenderFactory = DataSenderFactory()
		
		self.__dataProviders = {}
		self.__dataSenders = {}
		self.__metricsDataQueue = Queue()
		self.__pastMeasurementsManager = PastMeasurementsManager()
		
		#threads
		self.__collectDataThread = CollectDataThread(args=(self,))
		self.__sendDataThread = SendDataThread(args=(self,))
		
		#data providers, data senders
		self.__initializeDataProviders()
		self.__initializeDataSenders()
	
	def getDataProviders(self):
		return self.__dataProviders
	
	def getDataSenders(self):
		return self.__dataSenders
	
	def getSettings(self):
		return self.__settings
	
	def getMetricsDataQueue(self):
		return self.__metricsDataQueue
	
	def getPastMeasurementsManager(self):
		return self.__pastMeasurementsManager
			
	def beginWork(self):
		self.__collectDataThread.start()
		self.__sendDataThread.start()
		
		try:
			while True:
				for dataSender in self.__dataSenders.values():
					dataSender.sendAvailabilityState("UP")
					
				time.sleep(60)
		except KeyboardInterrupt:
			for dataSender in self.__dataSenders.values():
				dataSender.sendAvailabilityState("DOWN")

			sys.exit(0)

	def __initializeDataProviders(self):
		for srcServer in self.__settings.getSrcServers().values():
			dataProvider = self.__dataProviderFactory.getDataProvider(srcServer)
			dataProvider.connect()
			dataProvider.authenticate()
			
			self.__dataProviders[srcServer] = dataProvider
			
	def __initializeDataSenders(self):
		for dstServer in self.__settings.getDstServers().values():
			dataSender = self.__dataSenderFactory.getDataSender(dstServer)
			dataSender.connect()
			dataSender.authenticate()
			
			self.__dataSenders[dstServer] = dataSender
