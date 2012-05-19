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

		"URIs of WBEM servers delivering metrics data"
		self.wbemServersUris = []

	def updateWithCommandLine(self):
		parser = argparse.ArgumentParser(
			description="An agent passing metrics data to an RHQ server"
		)
		parser.add_argument(
			"-ws",
			"--wbemServers",
			nargs="*",
			default=[],
			metavar="server",
			help="URIs of WBEM servers delivering metrics data"
		)
		
		args = parser.parse_args()
		
		self.wbemServersUris.extend(args.wbemServers)
