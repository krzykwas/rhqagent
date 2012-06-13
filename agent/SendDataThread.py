#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-06-2012
#

from threading import Thread

try:
	from queue import Empty #@UnresolvedImport
except:
	from Queue import Empty #@UnresolvedImport

class SendDataThread(Thread):
	
	def __init__(self, args):
		Thread.__init__(self, args=args)
		
		self.__stopped = False
		self.__pyAgent = args[0]

	def run(self):
		metricsDataQueue = self.__pyAgent.getMetricsDataQueue()
		
		while not self.__stopped:
			try:
				measurement = metricsDataQueue.get(True, 5)
				print(measurement.getSrcServer().getName() + ": " + str(measurement.getValue()))
			except Empty:
				pass
			
	def stop(self):
		self.__stopped = True