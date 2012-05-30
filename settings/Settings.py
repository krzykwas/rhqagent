#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 19-05-2012
#

from Server import Server
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

		"Servers delivering metrics data"
		self.__servers = []

	def getServers(self):
		return self.__servers

	def updateWithCommandLine(self):
		parser = argparse.ArgumentParser(
			description="An agent passing metrics data to an RHQ server"
		)
		parser.add_argument(
			"--servers",
			nargs="*",
			default=[],
			metavar="server",
			help="""Servers providing metrics data, for each one type 
		protocol:username:password:uri, for instance: wbem:root:toor:https://localhost"""
		)
		
		args = parser.parse_args()
		
		for server in args.servers:
			protocol, username, password, uri = server.split(":", 3)
			self.__servers.append(Server(protocol, username, password, uri))
