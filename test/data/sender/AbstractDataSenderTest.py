#-*- coding: utf-8 -*-

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
