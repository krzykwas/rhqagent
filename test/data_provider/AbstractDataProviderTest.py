#-*- coding: utf-8 -*-

from data_provider.AbstractDataProvider import AbstractDataProvider
import unittest

class AbstractDataProviderTest(unittest.TestCase):

	def test_WhenInitMethodInvoked_TypeErrorIsThrown(self):
		"""
		Checks whether AbstractDataProvider is abstract, i.e. cannot be directly 
		instatiated.
		"""

		self.assertRaises(TypeError, lambda classObject: classObject(), AbstractDataProvider)

	def test_getSrcServer_IsDefined(self):		
		self.assertIn("getSrcServer", dir(AbstractDataProvider), "Method getSrcServer must be defined")