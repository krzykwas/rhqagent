#-*- coding: utf-8 -*-

import importlib

class DataProviderFactory(object):

	def getDataProvider(self, protocol, uri):
		"""
		Basing on the protocol name passed as a second argument finds a proper module which 
		name is composed of uppercase protocol name and a string <<DataProvider>>, like 
		WBEMConnection or HTTPConnection, or FTPConnection and so on.

		As a second step, imports a class called in the same manner as the module, 
		instantiates it and returns the created object.

		In case of any error None is returned instead of an expected dataProvider.
		"""
		try:
			name = protocol.upper() + "DataProvider"

			module = importlib.import_module(".implementation." + name, "data_provider")
			dataProviderClassObject = getattr(module, name)

			dataProvider = dataProviderClassObject(uri)

			return dataProvider
		except IOError:
			return None
