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

	def test_getUsername_IsDefined(self):		
		self.assertIn("getUsername", dir(AbstractDataProvider), "Method getUsername must be defined")
		
	def test_getPassword_IsDefined(self):
		self.assertIn("getPassword", dir(AbstractDataProvider), "Method getPassword must be defined")
		
	def test_getUri_IsDefined(self):
		self.assertIn("getUri", dir(AbstractDataProvider), "Method getUri must be defined")