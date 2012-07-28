#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 13-06-2012
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
import unittest

class MeasurementTest(unittest.TestCase):

	def setUp(self):
		self.__srcServer = object()
		self.__mappedObject = object()
		self.__dstServerMapping = object()
		self.__value = 123
		self.__timestamp = 1e5
		
		self.__sut = Measurement(
			self.__srcServer,
			self.__mappedObject,
			self.__dstServerMapping,
			self.__value,
			self.__timestamp
		)
		
	def test_getSrcServer_IsDefined(self):
		objectFields = dir(self.__sut)		
		self.assertIn("getSrcServer", objectFields, "Method getSrcServer not defined")
		
	def test_getMappedObject_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMappedObject", objectFields, "Method getMappedObject not defined")
	
	def test_getDstServerMapping_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDstServerMapping", objectFields, "Method getDstServerMapping not defined")
		
	def test_getValue_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getValue", objectFields, "Method getValue not defined")
		
	def test_getTimestamp_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getTimestamp", objectFields, "Method getTimestamp not defined")
		
	def test_valueProperty_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("value", objectFields, "Property value not defined")
		
	def test_timestampProperty_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("timestamp", objectFields, "Property timestamp not defined")
		
	def test_getSrcServer_InvokedOnNewObject_ReturnsValuePassedInInit(self):
		self.assertEqual(self.__srcServer, self.__sut.getSrcServer(), "Incorrect value returned")
		
	def test_getMappedObject_InvokedOnNewObject_ReturnsValuePassedInInit(self):
		self.assertEqual(self.__mappedObject, self.__sut.getMappedObject(), "Incorrect value returned")
		
	def test_getDstServerMapping_InvokedOnNewObject_ReturnsValuePassedInInit(self):
		self.assertEqual(self.__dstServerMapping, self.__sut.getDstServerMapping(), "Incorrect value returned")
		
	def test_getValue_InvokedOnNewObject_ReturnsValuePassedInInit(self):
		self.assertEqual(self.__value, self.__sut.getValue(), "Incorrect value returned")

	def test_getTimestamp_InvokedOnNewObject_ReturnsValuePassedInInit(self):
		self.assertEqual(self.__timestamp, self.__sut.getTimestamp(), "Incorrect value returned")

	def test_valueProperty_ConsistentWith_getValue(self):
		self.assertEqual(self.__sut.value, self.__sut.getValue(), "Value property inconsistent with method getValue")
	
	def test_timestampProperty_ConsistentWith_getTimestamp(self):
		self.assertEqual(self.__sut.timestamp, self.__sut.getTimestamp(), "Timestamp property inconsistent with method getTimestamp")
