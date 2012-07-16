#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-07-2012
#

from data.model.callback.Callback import Callback
import unittest

class CallbackTest(unittest.TestCase):

	def setUp(self):
		self.__functionCode = ""
		self.__params = []
		self.__dstServersMappings = []
		self.__sut = Callback(
			functionCode=self.__functionCode,
			params=self.__params,
			dstServersMappings=self.__dstServersMappings
		)

	def test_getDstServersMappings_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDstServersMappings", objectFields, "Method getDstServersMappings not defined")
		
	def test_getParams_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getParams", objectFields, "Method getParams not defined")
		
	def test_wrapWithFunction_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("wrapWithFunction", objectFields, "Method wrapWithFunction not defined")

	def test_getDstServersMappings_ReturnsObjectPassedInInit(self):
		self.assertIs(self.__dstServersMappings, self.__sut.getDstServersMappings())
		
	def test_getParams_ReturnsObjectPassedInInit(self):
		self.assertIs(self.__params, self.__sut.getParams())
		
	def test_call_CorrectlyExecutesSimpleFunction_Returning1(self):
		sut = Callback(
			"""
return 1
			""",
			[], []
		)
		
		self.assertEqual(sut([]), 1)
		
	def test_call_DoesNotRaise_WhenCallbackInitialized_WithEmptyFunctionCode(self):
		sut = Callback("", [], [])
		
		try:
			sut([])
		except Exception as e:
			self.fail("Unexpected {0} raised unexpectedly".format(e))
