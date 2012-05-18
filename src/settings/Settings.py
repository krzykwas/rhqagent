# -*- coding: utf-8 -*-

import argparse

class Settings(object):
	"""
	Responsible for merging configuration for RHQAgent coming from different sources, like 
	command line arguments and configuration files. That in the future, for now only command 
	line options are supported.
	"""
	def __init__(self):
		#set default arguments in here
		pass

	def updateWithCommandLine(self, argv):
		parser = argparse.ArgumentParser(description="An agent passing metrics data to an RHQ server")
		pass
