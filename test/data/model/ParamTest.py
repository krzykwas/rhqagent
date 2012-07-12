#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-07-2012
#

from data.model.Param import Param
import unittest

class ParamTest(unittest.TestCase):

	def setUp(self):
		self.__srcServer = object()
		self.__mappedObject = object()
		self.__sut = Param(self.__srcServer, self.__mappedObject)
		
	def test_getSrcServer_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getSrcServer", objectFields, "Method getSrcServer not defined")
		
	def test_getMappedObject_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getMappedObject", objectFields, "Method getMappedObject not defined")

	def test_getSrcServer_ReturnsObjectPassedInInit(self):
		self.assertIs(self.__srcServer, self.__sut.getSrcServer())
		
	def test_getMappedObject_ReturnsObjectPassedInInit(self):
		self.assertIs(self.__mappedObject, self.__sut.getMappedObject())
