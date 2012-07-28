#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 04-07-2012
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

from data.provider.implementation.WBEMDataProvider import WBEMDataProvider
from data.model.SrcServer import SrcServer
import unittest

class WBEMDataProviderTest(unittest.TestCase):

	class SrcServerMock(SrcServer):
		def __init__(self):
			SrcServer.__init__(self, "", "", "", "", "")

	def setUp(self):
		self.__srcServer = self.SrcServerMock()
		self.__sut = WBEMDataProvider(self.__srcServer)

	def test_getSrcServer_IsDefined(self):		
		self.assertIn("getSrcServer", dir(self.__sut), "Method getSrcServer not defined")
		
	def test_authenticate_IsDefined(self):
		self.assertIn("authenticate", dir(self.__sut), "Method authenticate not defined")
		
	def test_connect_IsDefined(self):
		self.assertIn("connect", dir(self.__sut), "Method connect not defined")
		
	def test_getData_IsDefined(self):	
		self.assertIn("getData", dir(self.__sut), "Method getData not defined")

	def test_connect_DoesNotRaiseAnyException(self):
		try:
			self.__sut.connect()
		except Exception as e:
			self.fail("Exception {0} raised unexpectedly".format(e))
					
	def test_getSrcServer_ReturnsCorrectObjectPassedInInit(self):
		self.assertEqual(self.__srcServer, self.__sut.getSrcServer(), "Incorrect object returned")
