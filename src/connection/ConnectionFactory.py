#-*- coding: utf-8 -*-

import importlib

class ConnectionFactory(object):

	def getConnection(self, protocol):
		"""
		Basing on the protocol name passed as a second argument finds a proper module which 
		name is composed of uppercase protocol name and a string <<Connection>>, like 
		WBEMConnection or HTTPConnection, or FTPConnection and so on.

		As a second step, imports a class called in the same manner as the module, 
		instantiates it and returns the created object.

		In case of any error None is returned instead of an expected connection.
		"""
		try:
			name = protocol.upper() + "Connection"

			module = importlib.import_module(".implementation." + name, "connection")
			connectionClassObject = getattr(module, name)

			connection = connectionClassObject()

			return connection
		except:
			return None
