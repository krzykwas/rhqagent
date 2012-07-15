#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
#

class MappedObject(object):
	"""
	Resource received by PyAgent and passed to a monitoring server.
	Two MappedObject instances are equal, if they have equal fields.
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
		
	def __eq__(self, other):
		return self.__namespace == other.getNamespace()\
			and self.__name == other.getName()\
			and self.__index == other.getIndex()\
			and self.__attribute == other.getAttribute()
			
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		prime = 13
		result = 1
		result = prime * result + self.__namespace.__hash__()
		result = prime * result + self.__name.__hash__()
		result = prime * result + self.__index.__hash__()
		result = prime * result + self.__attribute.__hash__()
		
		return result

	def getNamespace(self):
		return self.__namespace

	def getName(self):
		return self.__name
		
	def getIndex(self):
		return self.__index

	def getAttribute(self):
		return self.__attribute
		
