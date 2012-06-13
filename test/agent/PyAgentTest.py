#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#

from agent.PyAgent import PyAgent
from settings.Settings import Settings
import unittest

class PyAgentTest(unittest.TestCase):
	class SettingsMock(Settings):
		pass

	def setUp(self):
		self.__settigsMock = self.SettingsMock()
		self.__sut = PyAgent(self.__settigsMock)

	def test_getDataProviders_IsDefined(self):
		objectFields = dir(self.__sut)		
		self.assertIn("getDataProviders", objectFields, "Method getDataProviders must be defined")
		
	def test_getSettings_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getSettings", objectFields, "Method getSettings must be defined")
	
	def test_getMetricsDataQueue_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMetricsDataQueue", objectFields, "Method getMetricsDataQueue must be defined")
		
	def test_beginWork_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("beginWork", objectFields, "Method beginWork must be defined")
		
	def test_getDataProviders_InvokedOnNewObject_ReturnsEmptyDict(self):
		self.assertEqual({}, self.__sut.getDataProviders(), "Empty dict is returned")
		
	def test_getSettings_InvokedOnNewObject_ReturnsCorrectValue(self):
		self.assertEqual(self.__settigsMock, self.__sut.getSettings(), "Proper value is returned")
		
	def test_getMetricsDataQueue_InvokedOnNewObject_ReturnsEmptyQueue(self):
		self.assertTrue(self.__sut.getMetricsDataQueue().empty(), "Initially the metrics queue must be empty")