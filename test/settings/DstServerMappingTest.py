#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 10-06-2012
#

from settings.DstServerMapping import DstServerMapping
import unittest

class DstServerMappingTest(unittest.TestCase):

	def setUp(self):
		self.__dstServer = object()
		self.__mapTo = 12
		
		self.__sut = DstServerMapping(self.__dstServer, self.__mapTo)

	def test_getDstServer_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDstServer", objectFields, "Method getDstServer must be defined")
		
	def test_getMapTo_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMapTo", objectFields, "Method getMapTo must be defined")
				
	def test_getDstServer_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__dstServer, self.__sut.getDstServer(), "Proper value is returned")
		
	def test_getMapTo_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__mapTo, self.__sut.getMapTo(), "Proper value is returned")
