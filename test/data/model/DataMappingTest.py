#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 10-06-2012
#

from data.model.DataMapping import DataMapping
from data.model.MappedObject import MappedObject
from data.model.SrcServer import SrcServer
import unittest

class DataMappingTest(unittest.TestCase):

	def setUp(self):
		self.__srcServer = object()
		self.__mappedObject = object()
		self.__dstServersMappings = []
		
		self.__sut = DataMapping(self.__srcServer, self.__mappedObject, self.__dstServersMappings)

	def test_getSrcServer_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getSrcServer", objectFields, "Method getSrcServer not defined")

	def test_getMappedObject_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMappedObject", objectFields, "Method getMappedObject not defined")
		
	def test_getDstServersMappings_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDstServersMappings", objectFields, "Method getDstServersMappings not defined")

	def test_getSrcServer_ReturnsValuePassedInInitMethod(self):
		self.assertIs(self.__srcServer, self.__sut.getSrcServer(), "Values are different")
		
	def test_getMappedObject_ReturnsValuePassedInInitMethod(self):
		self.assertIs(self.__mappedObject, self.__sut.getMappedObject(), "Values are different")	
		
	def test_getDstServersMappings_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__dstServersMappings, self.__sut.getDstServersMappings(), "Values are different")	

	def test_str_ReturnsProperlyFormattedString(self):
		srcServer = SrcServer("name", "protocol", "uri", "username", "password")
		mappedObject = MappedObject("namespace", "index", "name", "attribute")
		sut = DataMapping(srcServer=srcServer, mappedObject=mappedObject, dstServersMappings=[])
		expected = "index.name.attribute@name"
		actual = str(sut)
		self.assertEqual(expected, actual, "Returned value {0} does not match the expected {1}".format(actual, expected))
