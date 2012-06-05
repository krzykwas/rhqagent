#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

import importlib

class DataProviderFactory(object):

	def getDataProvider(self, protocol, username, password, uri):
		"""
		Basing on the protocol name passed as a second argument finds a proper module which 
		name is composed of uppercase protocol name and a string <<DataProvider>>, like 
		WBEMDataProvider or HTTPDataProvider, or FTPDataProvider and so on.

		As a second step, imports a class called in the same manner as the module, 
		instantiates it and returns the created object.

		In case of any error None is returned instead of an expected data provider instance.
		"""
		try:
			name = self.getDataProviderClassName(protocol)

			module = importlib.import_module(".implementation." + name, "data_provider")
			dataProviderClassObject = getattr(module, name)

			dataProvider = dataProviderClassObject(username, password, uri)

			return dataProvider
		except IOError:
			return None

	def getDataProviderClassName(self, protocol):
		if False in [char.isalpha() for char in protocol]:
			raise ValueError("Invalid protocol name - only letters allowed")
		
		return protocol.upper() + "DataProvider"
