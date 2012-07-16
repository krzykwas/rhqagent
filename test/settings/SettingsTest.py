#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#

from settings.Settings import Settings
import unittest

class SettingsTest(unittest.TestCase):

	def setUp(self):
		self.__sut = Settings()

	def test_getCallbacks_IsDefined(self):
		objectFields = dir(self.__sut)		
		self.assertIn("getCallbacks", objectFields, "Method getCallbacks not defined")

	def test_getSrcServers_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getSrcServers", objectFields, "Method getSrcServers not defined")

	def test_getDstServers_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDstServers", objectFields, "Method getDstServers not defined")

	def test_getDataMappings_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDataMappings", objectFields, "Method getDataMappings not defined")
	
	def test_getPastMeasurementsSize_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getPastMeasurementsSize", objectFields, "Method getPastMeasurementsSize not defined")
		
	def test_getDebugLevel_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDebugLevel", objectFields, "Method getDebugLevel not defined")	

	def test_updateWithCommandLine_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("updateWithCommandLine", objectFields, "Method updateWithCommandLine not defined")
				
	def test_getCallbacks_InvokedOnNewObject_ReturnsEmptyList(self):
		self.assertEqual([], self.__sut.getCallbacks(), "Non-empty list returned")
		
	def test_getSrcServers_InvokedOnNewObject_ReturnsEmptyDict(self):
		self.assertEqual({}, self.__sut.getSrcServers(), "Non-empty dict returned")
		
	def test_getDstServers_InvokedOnNewObject_ReturnsEmptyDict(self):
		self.assertEqual({}, self.__sut.getDstServers(), "Non-empty dict returned")
		
	def test_getDataMappings_InvokedOnNewObject_ReturnsEmptyList(self):
		self.assertEqual([], self.__sut.getDataMappings(), "Non-empty list returned")
		
	def test_getPastMeasurementsSize_InvokedOnNewObject_ReturnsNone(self):
		self.assertIs(None, self.__sut.getPastMeasurementsSize(), "None not returned")
		
	def test_getDebugLevel_InvokedOnNewObject_ReturnsNone(self):
		self.assertIs(None, self.__sut.getDebugLevel(), "None not returned")
