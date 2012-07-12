#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#

from data.model.DstServer import DstServer
import unittest

class ServerTest(unittest.TestCase):

	def setUp(self):
		self.__name = "name"
		self.__protocol = "protocol"
		self.__uri = "uri"
		self.__username = "username"
		self.__password = "password"
		
		self.__sut = DstServer(self.__name, self.__protocol, self.__uri, self.__username, self.__password)

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