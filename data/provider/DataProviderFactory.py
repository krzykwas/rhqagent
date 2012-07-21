#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

import importlib
import pkgutil

class DataProviderFactory(object):

	def getDataProvider(self, srcServer):
		"""
		Basing on the protocol name finds a proper module which	name is composed
		of uppercase protocol name and a string <<DataProvider>>, like 
		WBEMDataProvider or HTTPDataProvider, or FTPDataProvider and so on.

		As a second step, imports a class called in the same manner as the module, 
		instantiates it and returns the created object.

		In case of any error None is returned instead of an expected data provider instance.
		"""
		try:
			name = self.getDataProviderClassName(srcServer.getProtocol())

			module = importlib.import_module(".implementation." + name, "data.provider")
			dataProviderClassObject = getattr(module, name)

			dataProvider = dataProviderClassObject(srcServer)

			return dataProvider
		except ImportError:
			return None

	def getDataProviderClassName(self, protocol):
		if False in [char.isalpha() for char in protocol]:
			raise ValueError("Invalid protocol name - only letters allowed")
		
		return protocol.upper() + "DataProvider"
	
	def getDataProviderNames(self):
		try:
			dataProviderNames = []
			
			module = importlib.import_module(".implementation", "data.provider")
			for importer, modname, ispkg in pkgutil.iter_modules(module.__path__):
				if modname.endswith("DataProvider"):
					dataProviderNames.append(modname)
				
			return dataProviderNames
		except ImportError:
			return None
