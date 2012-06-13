#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 13-06-2012
#

from agent.Measurement import Measurement
import unittest

class MeasurementTest(unittest.TestCase):

	def setUp(self):
		self.__srcServer = object()
		self.__mappedObject = object()
		self.__dstServerMapping = object()
		self.__value = 123
		
		self.__sut = Measurement(self.__srcServer, self.__mappedObject, self.__dstServerMapping, self.__value)
		
	def test_getSrcServer_IsDefined(self):
		objectFields = dir(self.__sut)		
		self.assertIn("getSrcServer", objectFields, "Method getSrcServer must be defined")
		
	def test_getMappedObject_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMappedObject", objectFields, "Method getMappedObject must be defined")
	
	def test_getDstServerMapping_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDstServerMapping", objectFields, "Method getDstServerMapping must be defined")
		
	def test_getValue_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getValue", objectFields, "Method getValue must be defined")
		
	def test_getSrcServer_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__srcServer, self.__sut.getSrcServer(), "Proper value is returned")
		
	def test_getMappedObject_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__mappedObject, self.__sut.getMappedObject(), "Proper value is returned")
		
	def test_getDstServerMapping_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__dstServerMapping, self.__sut.getDstServerMapping(), "Proper value is returned")
		
	def test_getValue_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__value, self.__sut.getValue(), "Proper value is returned")