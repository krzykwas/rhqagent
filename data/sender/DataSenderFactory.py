#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

import importlib

class DataSenderFactory(object):

	def getDataSender(self, dstServer):
		"""
		Basing on the protocol name finds a proper module which	name is composed
		of uppercase protocol name and a string <<DataProvider>>, like 
		WBEMDataProvider or HTTPDataProvider, or FTPDataProvider and so on.

		As a second step, imports a class called in the same manner as the module, 
		instantiates it and returns the created object.

		In case of any error None is returned instead of an expected data provider instance.
		"""
		try:
			name = self.getDataSenderClassName(dstServer.getProtocol())

			module = importlib.import_module(".implementation." + name, "data.sender")
			dataSenderClassObject = getattr(module, name)

			dataSender = dataSenderClassObject(dstServer)

			return dataSender
		except IOError:
			return None

	def getDataSenderClassName(self, protocol):
		if False in [char.isalpha() for char in protocol]:
			raise ValueError("Invalid protocol name - only letters allowed")
		
		return protocol.upper() + "DataSender"
