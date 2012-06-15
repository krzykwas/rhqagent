#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#

from data_provider.DataProviderFactory import DataProviderFactory
import unittest

class DataProviderFactoryTest(unittest.TestCase):

	def setUp(self):
		self.__sut = DataProviderFactory()

	def test_getDataProvider_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDataProvider", objectFields, "Method getDataProvider not defined")

	def test_getDataProviderClassName_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDataProviderClassName", objectFields, "Method getDataProviderClassName not defined")
		
	def test_getDataProviderClassName_InvokedWithCorrectProtocolName_ReturnsCorrectlyFormattedClassName(self):
		formattedClassName = self.__sut.getDataProviderClassName("abc")
		self.assertEqual("ABCDataProvider", formattedClassName, "Class's name {0} is invalid".format(formattedClassName))

	def test_getDataProviderClassName_InvokedWithIncorrectProtocolName_RaisesValueError(self):
		self.assertRaises(ValueError, self.__sut.getDataProviderClassName, "invalid-name")