#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

from agent.CollectDataThread import CollectDataThread
from agent.SendDataThread import SendDataThread
from data_provider.DataProviderFactory import DataProviderFactory
import time
import sys

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
		self.__dataProviders = {}
		self.__metricsDataQueue = Queue()
		
		#threads
		self.__collectDataThread = CollectDataThread(args=(self,))
		self.__sendDataThread = SendDataThread(args=(self,))
		
		for srcServerName, srcServer in self.__settings.getSrcServers().items():
			dataProvider = self.__dataProviderFactory.getDataProvider(srcServer)
			dataProvider.connect()
			dataProvider.authenticate()
			
			self.__dataProviders[srcServerName] = dataProvider
	
	def getDataProviders(self):
		return self.__dataProviders
	
	def getSettings(self):
		return self.__settings
	
	def getMetricsDataQueue(self):
		return self.__metricsDataQueue
			
	def beginWork(self):
		self.__collectDataThread.start()
		self.__sendDataThread.start()
		
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			sys.exit(0)
