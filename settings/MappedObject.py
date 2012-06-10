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
		self.__namespace = namespace	#Namespace where a mapped object resides
		self.__name = name				#The name of mapped object (like an object representing a cpu)
		self.__index = index			#The index of the mapped object (like when there are 2 cpus)
		self.__attribute = attribute	#The attribute to pass (like a cpu load)

	def getNamespace(self):
		return self.__namespace

	def getName(self):
		return self.__name
		
	def getIndex(self):
		return self.__index

	def getAttribute(self):
		return self.__attribute
		