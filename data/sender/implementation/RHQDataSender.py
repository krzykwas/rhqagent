#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 21-06-2012
#

from data.sender.AbstractDataSender import AbstractDataSender

class RHQDataSender(AbstractDataSender):
	"""
	Sends data to an RHQ server.
	"""
	
	def __init__(self, dstServer):
		AbstractDataSender.__init__(self, dstServer)
		
		self.__dstServer = dstServer
		
	def authenticate(self):
		pass
	
	def connect(self):
		pass
	
	def sendData(self, measurement):
		print(measurement.getSrcServer().getName() + ": " + str(measurement.getValue()))
