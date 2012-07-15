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
		self.assertIn("getDataProviders", objectFields, "Method getDataProviders not defined")
	
	def test_getDataSenders_IsDefined(self):
		objectFields = dir(self.__sut)		
		self.assertIn("getDataSenders", objectFields, "Method getDataSenders not defined")
		
	def test_getSettings_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getSettings", objectFields, "Method getSettings not defined")
	
	def test_getMetricsDataQueue_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMetricsDataQueue", objectFields, "Method getMetricsDataQueue not defined")
		
	def test_getPastMeasurementsManager_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getPastMeasurementsManager", objectFields, "Method getPastMeasurementsManager not defined")
		
	def test_beginWork_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("beginWork", objectFields, "Method beginWork not defined")
		
	def test_getDataProviders_InvokedOnNewObject_ReturnsEmptyDict(self):
		self.assertEqual({}, self.__sut.getDataProviders(), "Non-empty dict returned")
		
	def test_getDataSenders_InvokedOnNewObject_ReturnsEmptyDict(self):
		self.assertEqual({}, self.__sut.getDataSenders(), "Non-empty dict returned")
		
	def test_getSettings_InvokedOnNewObject_ReturnsCorrectObjectPassedInInit(self):
		self.assertEqual(self.__settigsMock, self.__sut.getSettings(), "Incorrect object returned")
		
	def test_getMetricsDataQueue_InvokedOnNewObject_ReturnsEmptyQueue(self):
		self.assertTrue(self.__sut.getMetricsDataQueue().empty(), "Initially the metrics queue is not empty")
