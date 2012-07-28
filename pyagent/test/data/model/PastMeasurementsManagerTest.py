#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 15-07-2012
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

from ....data.model.Measurement import Measurement
from ....data.model.PastMeasurementsManager import PastMeasurementsManager
import unittest

class PastMeasurementsManagerTest(unittest.TestCase):

	def setUp(self):
		self.__PERIOD = 3
		self.__sut = PastMeasurementsManager(self.__PERIOD)

	def test_get_InvokedOnEmptyManager_ReturnsAListOfCorrectLength(self):
		actual = len(self.__sut.get("srcServer", "mappedObject"))
		self.assertEqual(3, actual, "List of wrong length returned")

	def test_get_WhenOneMeasurementMissing_AFakeOneIsCreatedWithDataProperlyCopiedFromTheOldestOne(self):
		srcServer = "srcServer"
		mappedObject = "mappedObject"
		
		mapping1 = "dst-server-mapping-1"
		mapping2 = "dst-server-mapping-2"
		timestamp1 = "timestamp-1"
		timestamp2 = "timestamp-2"
		
		#This measurement is added first, so it's the oldest one!
		measurement1 = Measurement(srcServer, mappedObject, mapping1, 0, timestamp1)
		self.__sut.put(srcServer, mappedObject, measurement1)
		
		measurement2 = Measurement(srcServer, mappedObject, mapping2, 0, timestamp2)
		self.__sut.put(srcServer, mappedObject, measurement2)
		
		fakeMeasurement = self.__sut.get(srcServer, mappedObject)[-1]
		
		self.assertEqual(
			mapping1,
			fakeMeasurement.getDstServerMapping(),
			"dstServerMapping value: {0} incorrectly copied to fake measurement".format(fakeMeasurement.getDstServerMapping())
		)

		self.assertEqual(
			timestamp1,
			fakeMeasurement.getTimestamp(),
			"timestamp value: {0} incorrectly copied to fake measurement".format(fakeMeasurement.getTimestamp())
		)
		
	def test_put_WhenFirstMeasurementAddedForCertainSrcServerAndMappedObject_NoExceptionRaised(self):
		try:
			self.__sut.put("srcServer", "mappedObject", "measurement")
		except Exception as e:
			self.fail("Exception {0} raised unexpectedly".format(e))
			
	def test_put_WhenMoreThanPeriodMeasurementsAdded_OldestGetForgotten(self):
		srcServer = "srcServer"
		mappedObject = "mappedObject"
		
		#measurement1 is the oldest one!
		measurement1 = Measurement(srcServer, mappedObject, "dstServerMapping1", 1, "timestamp1")
		measurement2 = Measurement(srcServer, mappedObject, "dstServerMapping2", 2, "timestamp2")
		measurement3 = Measurement(srcServer, mappedObject, "dstServerMapping3", 3, "timestamp3")
		measurement4 = Measurement(srcServer, mappedObject, "dstServerMapping4", 4, "timestamp4")
		
		self.__sut.put(srcServer, mappedObject, measurement1)
		self.__sut.put(srcServer, mappedObject, measurement2)
		self.__sut.put(srcServer, mappedObject, measurement3)
		self.__sut.put(srcServer, mappedObject, measurement4)

		expected = [measurement4, measurement3, measurement2]
		actual = self.__sut.get(srcServer, mappedObject)
		
		self.assertListEqual(expected, actual, "Incorrect measurements returned")
