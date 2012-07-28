#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 21-07-2012
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

from agent.CollectDataThread import CollectDataThread
from agent.PyAgent import PyAgent
from data.model.DataMapping import DataMapping
from data.model.callback.Param import Param
from settings.Settings import Settings
import unittest

class CollectDataThreadTest(unittest.TestCase):

	class __PropertyMock(object):
		def __getattr__(self, *args, **kwargs):
			return lambda: ""

	class __DstServerMappingMock(__PropertyMock):
		def __init__(self, isDue):
			self.__isDue = isDue
		
		def isDue(self):
			return self.__isDue
		
	class __DataProviderMock(object):
		def getData(self, *args, **kwargs):
			return 1
		
	class __SettingsMock(Settings):
		def getPastMeasurementsSize(self):
			return 3
		
	class __CallbackMock(object):
		def __init__(self):
			self.__dstServersMappings = []
			self.__params = []
	
		def __call__(self, *args, **kwargs):
			return ""
	
		def getDstServersMappings(self):
			return self.__dstServersMappings
		
		def getParams(self):
			return self.__params

	def setUp(self):
		self.__settings = self.__SettingsMock()
		self.__pyAgent = PyAgent(self.__settings)
		self.__sut = CollectDataThread([self.__pyAgent])
		
	def test_handleDataMapping_InvokedWithDueDstServerMapping_PutsAMeasurementIntoMetricsDataQueue(self):
		srcServer = self.__PropertyMock()
		self.__pyAgent.getDataProviders()[srcServer] = self.__DataProviderMock()
		
		dstServerMapping = self.__DstServerMappingMock(isDue=True)
		dataMapping = DataMapping(
			srcServer=srcServer,
			mappedObject=self.__PropertyMock(),
			dstServersMappings=[dstServerMapping])
		
		self.__sut.handleDataMapping(dataMapping)
		
		expected = 1
		actual = self.__pyAgent.getMetricsDataQueue().qsize()
		self.assertEqual(expected, actual, "The queue was expected to contain {0} instead of {1} elements".format(expected, actual))

	def test_handleCallback_InvokedWithDueDstServerMapping_PutsAMeasurementIntoMetricsDataQueue(self):
		srcServer = self.__PropertyMock()
		self.__pyAgent.getDataProviders()[srcServer] = self.__DataProviderMock()
		
		callback = self.__CallbackMock()
		dstServerMapping = self.__DstServerMappingMock(isDue=True)
		callback.getDstServersMappings().append(dstServerMapping)
		param = Param(srcServer, self.__PropertyMock())
		callback.getParams().append(param)
		
		self.__sut.handleCallback(callback)
		
		expected = 1
		actual = self.__pyAgent.getMetricsDataQueue().qsize()
		self.assertEqual(expected, actual, "The queue was expected to contain {0} instead of {1} elements".format(expected, actual))
