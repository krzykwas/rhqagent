#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 10-06-2012
#

from data.model.DstServerMapping import DstServerMapping
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
		self.assertEqual(self.__dstServer, self.__sut.getDstServer(), "{0} expected, instead {1} returned".format(self.__dstServer, self.__sut.getDstServer()))
		
	def test_getMapTo_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__mapTo, self.__sut.getMapTo(), "{0} expected, instead {1} returned".format(self.__mapTo, self.__sut.getMapTo()))
		
	def test_getUpdateInterval_InvokedOnNewObject_ReturnsCorrectValue(self):
		expected = self.__updateInterval
		actual = self.__sut.getUpdateInterval()
		self.assertEqual(expected, actual, "{0} expected, instead {1} returned".format(expected, actual))

	def test_isDue_OnNewlyCreatedInstance_WithZeroUpdateInterval_ReturnsTrue(self):
		newInstance = DstServerMapping(None, None, 0)
		self.assertTrue(newInstance.isDue())
		
	def test_setLastAccessNow_ChangesDueStateToFalse(self):
		sut = DstServerMapping(None, None, 1000)
		sut.setLastAccessedNow()
		self.assertFalse(sut.isDue())
		
	def test_init_WithNonEmptyStringAsUpdateInterval_RaisesValueError(self):
		self.assertRaises(ValueError, DstServerMapping, object(), "mapTo", "a-string")
		
	def test_init_WithNoneAsUpdateInterval_RaisesTypeError(self):
		self.assertRaises(TypeError, DstServerMapping, object(), "mapTo", None)
		
	def test_setUpdateInterval_WithNonEmptyString_RaisesValueError(self):
		self.assertRaises(ValueError, self.__sut.setUpdateInterval, "a-string")
		
	def test_setUpdateInterval_WithNone_RaisesTypeError(self):
		self.assertRaises(TypeError, self.__sut.setUpdateInterval, None)
		
	def test_setUpdateInterval_WithInt_ProperlyAssignsValue(self):
		expected = 123
		self.__sut.setUpdateInterval(expected)
		actual = self.__sut.getUpdateInterval()
		self.assertEqual(expected, actual, "{0} expected, instead {1} returned".format(expected, actual))
		
	def test_setUpdateInterval_ProperlyChangesInternalObjectState(self):
		expected = 234
		self.__sut.setUpdateInterval(expected)
		actual = self.__sut.getUpdateInterval()
		self.assertEqual(expected, actual, "{0} expected, instead {1} returned".format(expected, actual))
