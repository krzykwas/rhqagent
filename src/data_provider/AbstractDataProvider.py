#-*- coding: utf-8 -*-

from abc import ABCMeta

class AbstractDataProvider(object):
	__metaclass__ = ABCMeta
	
	def __init__(self, uri):
		self.__uri = uri
