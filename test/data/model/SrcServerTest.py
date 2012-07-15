#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#

from data.model.SrcServer import SrcServer
import collections
import unittest

class SrcServerTest(unittest.TestCase):

	def setUp(self):
		self.__name = "name"
		self.__protocol = "protocol"
		self.__uri = "uri"
		self.__username = "username"
		self.__password = "password"
		
		self.__sut = SrcServer(self.__name, self.__protocol, self.__uri, self.__username, self.__password)

	def test_getName_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getName", objectFields, "Method getName not defined")

	def test_getProtocol_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getProtocol", objectFields, "Method getProtocol not defined")

	def test_getUri_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getUri", objectFields, "Method getUri not defined")
		
	def test_getUsername_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getUsername", objectFields, "Method getUsername not defined")

	def test_getPassword_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getPassword", objectFields, "Method getPassword not defined")

	def test_getName_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__name, self.__sut.getName(), "Values are different")
		
	def test_getProtocol_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__protocol, self.__sut.getProtocol(), "Values are different")
	
	def test_getUri_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__uri, self.__sut.getUri(), "Values are different")		
		
	def test_getUsername_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__username, self.__sut.getUsername(), "Values are different")
			
	def test_getPassword_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__password, self.__sut.getPassword(), "Values are different")
		
	def test_srcServer_IsEqualToAnObjectWithSameFields(self):
		other = SrcServer(self.__name, self.__protocol, self.__uri, self.__username, self.__password)
		self.assertEqual(self.__sut, other, "Objects not considered equal")
		
	def test_srcServer_IsNotEqualToAnObjectWithDifferentFields(self):
		other = SrcServer("different-name", self.__protocol, self.__uri, self.__username, self.__password)
		self.assertNotEqual(self.__sut, other, "Objects considered equal")
		
	def test_srcServer_IsHashable(self):
		self.assertTrue(isinstance(self.__sut, collections.Hashable), "SrcServer is hashable")
		
	def test_srcServer_CanBeCorrectlyPutIntoADictionaryAndRetrievedBack(self):
		d = {self.__sut : 123}
		self.assertIn(self.__sut, d, "SrcServer not present in the dict, although expected there")
