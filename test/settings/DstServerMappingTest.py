#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 10-06-2012
#

from datetime import timedelta
from settings.DstServerMapping import DstServerMapping
import unittest

class DstServerMappingTest(unittest.TestCase):

	def setUp(self):
		self.__dstServer = object()
		self.__mapTo = 12
		self.__updateInterval = 10
		
		self.__sut = DstServerMapping(self.__dstServer, self.__mapTo, self.__updateInterval)

	def test_getDstServer_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDstServer", objectFields, "Method getDstServer not defined")
		
	def test_getMapTo_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMapTo", objectFields, "Method getMapTo not defined")
		
	def test_getUpdatePeriod_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getUpdateInterval", objectFields, "Method getUpdateInterval not defined")
				
	def test_getDstServer_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__dstServer, self.__sut.getDstServer(), "Incorrect value returned")
		
	def test_getMapTo_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__mapTo, self.__sut.getMapTo(), "Incorrect value returned")
		
	def test_getUpdateInterval_InvokedOnNewObject_ReturnsCorrectValue(self):
		expected = timedelta(seconds=self.__updateInterval)
		self.assertEqual(expected, self.__sut.getUpdateInterval(), "Incorrect value returned")

	def test_isDue_OnNewlyCreatedInstance_WithZeroUpdateInterval_ReturnsTrue(self):
		newInstance = DstServerMapping(None, None, 0)
		self.assertTrue(newInstance.isDue())
		
	def test_setLastAccessNow_ChangesDueStateToFalse(self):
		newInstance = DstServerMapping(None, None, 1000)
		newInstance.setLastAccessedNow()
		self.assertFalse(newInstance.isDue())