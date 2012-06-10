#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

from data_provider.DataProviderFactory import DataProviderFactory

class PyAgent(object):
	"""
	Responsible for gathering metrics data and passing it to an RHQ server.
	"""

	def __init__(self, settings):
		self.__settings = settings
		self.__dataProviderFactory = DataProviderFactory()
		self.__dataProviders = {}
		
		for srcServerName, srcServer in self.__settings.getSrcServers().items():
			dataProvider = self.__dataProviderFactory.getDataProvider(srcServer)
			self.__dataProviders[srcServerName] = dataProvider
