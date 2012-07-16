#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-06-2012
#

from threading import Thread
import logging

try:
	from queue import Empty #@UnresolvedImport
except:
	from Queue import Empty #@UnresolvedImport

class SendDataThread(Thread):
	
	def __init__(self, args):
		Thread.__init__(self, args=args)
		self.setDaemon(True)
		
		self.__pyAgent = args[0]
		
		self.__logger = logging.getLogger(__name__)
		self.__logger.debug("Starting sending data")

	def run(self):
		metricsDataQueue = self.__pyAgent.getMetricsDataQueue()
		
		while True:
			try:
				measurement = metricsDataQueue.get(True, 5)
				dstServer = measurement.getDstServerMapping().getDstServer()
				dataSender = self.__pyAgent.getDataSenders()[dstServer]
				dataSender.sendData(measurement)
			except Empty:
				pass
