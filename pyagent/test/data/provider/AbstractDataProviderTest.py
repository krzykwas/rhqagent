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

from data.provider.AbstractDataProvider import AbstractDataProvider
import unittest

class AbstractDataProviderTest(unittest.TestCase):

	def test_WhenInitMethodInvoked_TypeErrorIsRaised(self):
		"""
		Checks whether AbstractDataProvider is abstract, i.e. cannot be directly 
		instatiated.
		"""
		self.assertRaises(TypeError, AbstractDataProvider, object())

	def test_getSrcServer_IsDefined(self):		
		self.assertIn("getSrcServer", dir(AbstractDataProvider), "Method getSrcServer not defined")
		
	def test_authenticate_IsDefined(self):
		self.assertIn("authenticate", dir(AbstractDataProvider), "Method authenticate not defined")
		
	def test_connect_IsDefined(self):
		self.assertIn("connect", dir(AbstractDataProvider), "Method connect not defined")
		
	def test_getData_IsDefined(self):	
		self.assertIn("getData", dir(AbstractDataProvider), "Method getData not defined")
