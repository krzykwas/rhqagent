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

from .....data.model.DstServer import DstServer
from .....data.sender.implementation.RHQDataSender import RHQDataSender
import unittest

class RHQDataSenderTest(unittest.TestCase):

	class DstServerMock(DstServer):
		def __init__(self):
			DstServer.__init__(self, "", "", "", "", "")

	def setUp(self):
		self.__dstServer = self.DstServerMock()
		self.__sut = RHQDataSender(self.__dstServer)

	def test_getDstServer_IsDefined(self):
		self.assertIn("getDstServer", dir(self.__sut), "Method getDstServer not defined")
		
	def test_authenticate_IsDefined(self):
		self.assertIn("authenticate", dir(self.__sut), "Method authenticate not defined")
		
	def test_connect_IsDefined(self):
		self.assertIn("connect", dir(self.__sut), "Method connect not defined")
		
	def test_update_IsDefined(self):
		self.assertIn("update", dir(self.__sut), "Method update not defined")
		
	def test_sendAvailabilityState_IsDefined(self):	
		self.assertIn("sendAvailabilityState", dir(self.__sut), "Method sendAvailabilityState not defined")
		
	def test_sendData_IsDefined(self):	
		self.assertIn("sendData", dir(self.__sut), "Method sendData not defined")
		
	def test_getDstServer_ReturnsCorrectObjectPassedInInit(self):
		self.assertEqual(self.__dstServer, self.__sut.getDstServer(), "Incorrect object returned")
		
	def test_authenticate_DoesNotRaiseAnyException(self):
		try:
			self.__sut.authenticate()
		except Exception as e:
			self.fail("Exception {0} raised unexpectedly".format(e))