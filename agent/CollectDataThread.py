#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-06-2012
#

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
				mappedObject = dataMapping.getMappedObject()
				srcServer = dataMapping.getSrcServer()
				dataProviders = self.__pyAgent.getDataProviders()
				dataProvider = dataProviders[srcServer.getName()]
				
				print(dataProvider.getData(mappedObject))
				
			time.sleep(5)
			
	def stop(self):
		self.__stopped = True