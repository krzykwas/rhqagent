#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

from abc import ABCMeta
from abc import abstractmethod

class AbstractDataProvider(object):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def __init__(self, srcServer):
		self.__srcServer = srcServer

	def getSrcServer(self):
		return self.__srcServer
