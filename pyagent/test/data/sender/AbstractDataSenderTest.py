#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 28-07-2012
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

from data.sender.AbstractDataSender import AbstractDataSender
import unittest

class AbstractDataSenderTest(unittest.TestCase):

	def test_WhenInitMethodInvoked_TypeErrorIsThrown(self):
		"""
		Checks whether AbstractDataSender is abstract, i.e. cannot be directly 
		instatiated.
		"""
		self.assertRaises(TypeError, AbstractDataSender, object())

	def test_getDstServer_IsDefined(self):		
		self.assertIn("getDstServer", dir(AbstractDataSender), "Method getDstServer not defined")
		
	def test_authenticate_IsDefined(self):
		self.assertIn("authenticate", dir(AbstractDataSender), "Method authenticate not defined")
		
	def test_connect_IsDefined(self):
		self.assertIn("connect", dir(AbstractDataSender), "Method connect not defined")
	
	def test_sendAvailabilityState_IsDefined(self):	
		self.assertIn("sendAvailabilityState", dir(AbstractDataSender), "Method sendAvailabilityState not defined")
		
	def test_sendData_IsDefined(self):	
		self.assertIn("sendData", dir(AbstractDataSender), "Method sendData not defined")
