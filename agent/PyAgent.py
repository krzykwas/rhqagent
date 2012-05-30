#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
#

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
			username = server.getUsername()
			password = server.getPassword()
			uri = server.getUri()

			dataProvider = self.__dataProviderFactory.getDataProvider(protocol, 
			username, password, uri)
