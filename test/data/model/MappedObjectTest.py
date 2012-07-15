#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 10-06-2012
#

from data.model.MappedObject import MappedObject
import unittest
import collections

class MappedObjectTest(unittest.TestCase):

	def setUp(self):
		self.__namespace = "namespace"
		self.__name = "name"
		self.__index = 3
		self.__attribute = "attribute"
		
		self.__sut = MappedObject(self.__namespace, self.__name, self.__index, self.__attribute)
		
	def test_getNamespace_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getNamespace", objectFields, "Method getNamespace not defined")
		
	def test_getName_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getName", objectFields, "Method getName not defined")
		
	def test_getIndex_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getIndex", objectFields, "Method getIndex not defined")
		
	def test_getAttribute_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getAttribute", objectFields, "Method getAttribute not defined")
		
	def test_getNamespace_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__namespace, self.__sut.getNamespace(), "Incorrect value returned")
		
	def test_getName_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__name, self.__sut.getName(), "Incorrect value returned")
		
	def test_getIndex_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__index, self.__sut.getIndex(), "Incorrect value returned")
		
	def test_getAttribute_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__attribute, self.__sut.getAttribute(), "Incorrect value returned")
		
	def test_mappedObject_IsEqualToAnObjectWithSameFields(self):
		other = MappedObject(self.__namespace, self.__name, self.__index, self.__attribute)
		self.assertEqual(self.__sut, other, "Objects not considered equal")
		
	def test_srcServer_IsNotEqualToAnObjectWithDifferentFields(self):
		other = MappedObject("different-namespace", self.__name, self.__index, self.__attribute)
		self.assertNotEqual(self.__sut, other, "Objects considered equal")
		
	def test_srcServer_IsHashable(self):
		self.assertTrue(isinstance(self.__sut, collections.Hashable), "MappedObject is hashable")
		
	def test_srcServer_CanBeCorrectlyPutIntoADictionaryAndRetrievedBack(self):
		d = {self.__sut : 123}
		self.assertIn(self.__sut, d, "MappedObject not present in the dict, although expected there")
