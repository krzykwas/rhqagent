#-*- coding: utf-8 -*-

from connection.ConnectionFactory import ConnectionFactory

class PyAgent(object):
	"""
	Responsible for gathering metrics data and passing it to an RHQ server.
	"""

	def __init__(self, settings):
		self.__settings = settings
		self.__connectionFactory = ConnectionFactory()

	def openConnections(self):
		uris = self.__settings.getServersUris()
		
		for uri in uris:
			protocol = uri[:uri.find(":")]
			connection = self.__connectionFactory.getConnection(protocol)
