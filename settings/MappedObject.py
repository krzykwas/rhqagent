#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
#

class MappedObject(object):
	"""
	Resource received by PyAgent and passed to a monitoring server
	"""

	def __init__(self, namespace, name, index, attribute):
		"""
		@param namespace: Namespace where a mapped object resides
		@param name: The name of a mapped object
			(for instance Linux_Processor for a CIM object representing a cpu)
		@param index: The index of the mapped object (when there are 2 cpus, which one to choose?)
		@param attribute: The attribute to pass
			(for instance LoadPercentage for a Linux_Processor to select cpu load value)
		"""
		
		self.__namespace = namespace
		self.__name = name
		self.__index = index
		self.__attribute = attribute

	def getNamespace(self):
		return self.__namespace

	def getName(self):
		return self.__name
		
	def getIndex(self):
		return self.__index

	def getAttribute(self):
		return self.__attribute
		