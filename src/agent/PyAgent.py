#-*- coding: utf-8 -*-

from data_provider.DataProviderFactory import DataProviderFactory #@UnresolvedImport

class PyAgent(object):
	"""
	Responsible for gathering metrics data and passing it to an RHQ server.
	"""

	def __init__(self, settings):
		self.__settings = settings
		self.__dataProviderFactory = DataProviderFactory()

	def openConnections(self):
		servers = self.__settings.getServers()
		
		for server in servers:
			protocol = server.getProtocol()
			uri = server.getUri()
			dataProvider = self.__dataProviderFactory.getDataProvider(protocol, uri)
