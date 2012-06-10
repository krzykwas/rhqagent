#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 10-06-2012
#

from settings.MappedObject import MappedObject
import unittest

class MappedObjectTest(unittest.TestCase):

	def setUp(self):
		self.__namespace = "namespace"
		self.__name = "name"
		self.__index = 3
		self.__attribute = "attribute"
		
		self.__sut = MappedObject(self.__namespace, self.__name, self.__index, self.__attribute)
		
	def test_getNamespace_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getNamespace", objectFields, "Method getNamespace must be defined")
		
	def test_getName_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getName", objectFields, "Method getName must be defined")
		
	def test_getIndex_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getIndex", objectFields, "Method getIndex must be defined")
		
	def test_getAttribute_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getAttribute", objectFields, "Method getAttribute must be defined")
		
	def test_getNamespace_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__namespace, self.__sut.getNamespace(), "Correct value has to be returned")
		
	def test_getName_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__name, self.__sut.getName(), "Correct value has to be returned")
		
	def test_getIndex_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__index, self.__sut.getIndex(), "Correct value has to be returned")
		
	def test_getAttribute_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__attribute, self.__sut.getAttribute(), "Correct value has to be returned")