#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#

from settings.Server import Server
import unittest

class ServerTest(unittest.TestCase):

	def setUp(self):
		self.__protocol = "protocol"
		self.__username = "username"
		self.__password = "password"
		self.__uri = "uri"
		
		self.__sut = Server(self.__protocol, self.__username, self.__password, self.__uri)

	def test_getProtocol_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getProtocol", objectFields, "Method getProtocol must be defined")

	def test_getUsername_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getUsername", objectFields, "Method getUsername must be defined")

	def test_getPassword_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getPassword", objectFields, "Method getPassword must be defined")

	def test_getUri_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getUri", objectFields, "Method getUri must be defined")
					
	def test_getProtocol_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__protocol, self.__sut.getProtocol(), "Values are different")
		
	def test_getUsername_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__username, self.__sut.getUsername(), "Values are different")
			
	def test_getPassword_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__password, self.__sut.getPassword(), "Values are different")	
	
	def test_getUri_ReturnsValuePassedInInitMethod(self):
		self.assertEqual(self.__uri, self.__sut.getUri(), "Values are different")