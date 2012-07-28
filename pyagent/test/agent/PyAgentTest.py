#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
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
