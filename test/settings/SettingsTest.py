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

	def test_getServers_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getServers", objectFields, "Method getServers must be defined")

	def test_updateWithCommandLine_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("updateWithCommandLine", objectFields, "Method updateWithCommandLine must be defined")
		
	def test_getServers_InvokedOnNewSettingsObject_ReturnsEmptyList(self):
		self.assertEqual([], self.__sut.getServers(), "Just after creation the list of servers is empty")