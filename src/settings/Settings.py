# -*- coding: utf-8 -*-

import argparse

class Settings(object):
	"""
	Responsible for merging configuration for PyAgent coming from different sources - like 
	command line arguments and configuration files. That in the future, for now only command 
	line options are supported.
	"""

	def __init__(self):
		"""
		Set default arguments in here
		"""

		"URIs of servers delivering metrics data"
		self.__serversUris = []

	def getServersUris(self):
		return self.__serversUris

	def updateWithCommandLine(self):
		parser = argparse.ArgumentParser(
			description="An agent passing metrics data to an RHQ server"
		)
		parser.add_argument(
			"--servers",
			nargs="*",
			default=[],
			metavar="server",
			help="URIs of servers delivering metrics data"
		)
		
		args = parser.parse_args()
		
		self.__serversUris.extend(args.servers)
