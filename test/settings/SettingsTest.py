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

	def test_getSrcServers_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getSrcServers", objectFields, "Method getSrcServers must be defined")

	def test_getDstServers_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDstServers", objectFields, "Method getDstServers must be defined")

	def test_getDataMappings_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDataMappings", objectFields, "Method getDataMappings must be defined")

	def test_updateWithCommandLine_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("updateWithCommandLine", objectFields, "Method updateWithCommandLine must be defined")
		
	def test_getSrcServers_InvokedOnNewObject_ReturnsEmptyDict(self):
		self.assertEqual({}, self.__sut.getSrcServers(), "Just after creation the dictionary of source servers is empty")
		
	def test_getDstServers_InvokedOnNewObject_ReturnsEmptyDict(self):
		self.assertEqual({}, self.__sut.getDstServers(), "Just after creation the dictionary of destination servers is empty")
		
	def test_getDataMappings_InvokedOnNewObject_ReturnsEmptyList(self):
		self.assertEqual([], self.__sut.getDataMappings(), "Just after creation the list of data mappings is empty")