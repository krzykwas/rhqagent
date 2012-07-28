#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-07-2012
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

from data.model.MappedObject import MappedObject
from data.model.SrcServer import SrcServer
from data.model.callback.Param import Param
import unittest

class ParamTest(unittest.TestCase):

	def setUp(self):
		self.__srcServer = object()
		self.__mappedObject = object()
		self.__sut = Param(self.__srcServer, self.__mappedObject)
		
	def test_getSrcServer_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getSrcServer", objectFields, "Method getSrcServer not defined")
		
	def test_getMappedObject_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMappedObject", objectFields, "Method getMappedObject not defined")

	def test_getSrcServer_ReturnsObjectPassedInInit(self):
		self.assertIs(self.__srcServer, self.__sut.getSrcServer())
		
	def test_getMappedObject_ReturnsObjectPassedInInit(self):
		self.assertIs(self.__mappedObject, self.__sut.getMappedObject())
		
	def test_str_ReturnsProperlyFormattedString(self):
		srcServer = SrcServer("name", "protocol", "uri", "username", "password")
		mappedObject = MappedObject("namespace", "index", "name", "attribute")
		sut = Param(srcServer=srcServer, mappedObject=mappedObject)
		expected = "index.name.attribute@name"
		actual = str(sut)
		self.assertEqual(expected, actual, "Returned value {0} does not match the expected {1}".format(actual, expected))
