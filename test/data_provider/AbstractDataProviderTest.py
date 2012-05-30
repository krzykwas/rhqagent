#-*- coding: utf-8 -*-

from data_provider.AbstractDataProvider import AbstractDataProvider
import unittest

class AbstractDataProviderTest(unittest.TestCase):

	def test_WhenInitMethodInvoked_TypeErrorIsThrown(self):
		"""
		Checks whether AbstractDataProvider is abstract, i.e. cannot be directly 
		instatiated.
		"""

		self.assertRaises(TypeError, lambda : AbstractDataProvider())
