#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 10-06-2012
#

from data.model.DstServerMapping import DstServerMapping
from datetime import timedelta
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
		
	def test_getUpdateInterval_IsDefined(self):
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
		
	def test_init_WithNonEmptyStringAsUpdateInterval_RaisesValueError(self):
		self.assertRaises(ValueError, lambda: DstServerMapping(object(), "mapTo", "a-string"))
		
	def test_init_WithNoneAsUpdateInterval_RaisesTypeError(self):
		self.assertRaises(TypeError, lambda: DstServerMapping(object(), "mapTo", None))
		
	def test_setUpdateInterval_WithNonEmptyString_RaisesValueError(self):
		self.assertRaises(ValueError, lambda: self.__sut.setUpdateInterval("a-string"))
		
	def test_setUpdateInterval_WithNone_RaisesTypeError(self):
		self.assertRaises(TypeError, lambda: self.__sut.setUpdateInterval(None))
		
	def test_setUpdateInterval_WithTimedelta_ProperlyAssignsValue(self):
		expected = timedelta(3)
		self.__sut.setUpdateInterval(expected)
		self.assertEqual(expected, self.__sut.getUpdateInterval(), "Incorrect value returned")
		
	def test_setUpdateInterval_WithInt_ProperlyAssignsValue(self):
		expected = 5
		self.__sut.setUpdateInterval(timedelta(seconds=expected))
		self.assertEqual(expected, self.__sut.getUpdateInterval().total_seconds(), "Incorrect value returned")
		
	def test_setUpdateInterval_ProperlyChangesInternalObjectState(self):
		updateInterval = 6
		self.__sut.setUpdateInterval(updateInterval)
		self.assertEqual(timedelta(seconds=updateInterval), self.__sut.getUpdateInterval(), "Incorrect value returned by getUpdateInterval")
