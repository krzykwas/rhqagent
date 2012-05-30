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
	def __init__(self, username, password, uri):
		self.__username = username
		self.__password = password
		self.__uri = uri

	def getUsername(self):
		return self.__username

	def getPassword(self):
		return self.__password

	def getUri(self):
		return self.__uri
