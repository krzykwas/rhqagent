#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#

from data.model.DstServer import DstServer
from data.sender.DataSenderFactory import DataSenderFactory
import unittest

class DataSenderFactoryTest(unittest.TestCase):

	def setUp(self):
		self.__sut = DataSenderFactory()

	def test_getDataSender_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDataSender", objectFields, "Method getDataSender not defined")

	def test_getDataSenderClassName_IsDefined(self):
		objectFields = dir(self.__sut)
		self.assertIn("getDataSenderClassName", objectFields, "Method getDataSenderClassName not defined")
		
	def test_getDataSenderClassName_InvokedWithCorrectProtocolName_ReturnsCorrectlyFormattedClassName(self):
		formattedClassName = self.__sut.getDataSenderClassName("abc")
		self.assertEqual("ABCDataSender", formattedClassName, "Class's name {0} is invalid".format(formattedClassName))

	def test_getDataSenderClassName_InvokedWithIncorrectProtocolName_RaisesValueError(self):
		self.assertRaises(ValueError, self.__sut.getDataSenderClassName, "invalid-name")
		
	def test_getDataSender_InvokedWithADstServerWithInvalidProtocol_ReturnsNone(self):
		dstServer = DstServer("name", "protocolthatdoesnotexist", "uri", "username", "password")
		self.assertIs(None, self.__sut.getDataSender(dstServer))
		
	def test_getDataSender_CanCreateAllExistingDataSenders(self):
		try:
			for dataSenderName in self.__sut.getDataSenderNames():
				protocolName = dataSenderName[:dataSenderName.find("DataSender")].lower()
				dstServer = DstServer("name", protocolName, "uri", "username", "password")
				self.__sut.getDataSender(dstServer)
		except Exception as e:
			self.fail("Exception {0} raised enexpectedly".format(e))

	def test_getDataSenderNames_DoesNotRaise(self):
		try:
			self.__sut.getDataSenderNames()
		except Exception as e:
			self.fail("Exception {0} raised unexpectedly".format(e))
