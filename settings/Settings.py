#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 19-05-2012
#

from settings.configurationFile.Parser import Parser
import argparse
import logging

class Settings(object):
	"""
	Responsible for merging configuration for PyAgent coming from different sources - like 
	command line arguments and configuration files.
	"""

	def __init__(self):
		self.__configurationFile = ""	#Configuration file
		self.__srcServers = {}			#Servers providing data
		self.__dstServers = {}			#Servers accepting data
		self.__dataMappings = []		#Mappings between resources in srcServers and dstServers
		self.__callbacks = []			#User-defined callbacks allowing for calculation of artificial metrics
		self.__pastMeasurementsSize = None	#The number of past measurements stored for each metric
		self.__debugLevel = None		#The higher value, the more info printed
		self.__setup = False			#Generate a configuration file?
		
		self.__schemaPath = "settings/settings.xsd"

	def getCallbacks(self):
		return self.__callbacks

	def getDebugLevel(self):
		return self.__debugLevel

	def getSrcServers(self):
		return self.__srcServers
	
	def getDstServers(self):
		return self.__dstServers
	
	def getDataMappings(self):
		return self.__dataMappings
	
	def getPastMeasurementsSize(self):
		return self.__pastMeasurementsSize

	def getSetup(self):
		return self.__setup
	
	def updateWithCommandLine(self):
		debugLevels = {
			"CRITICAL"	: logging.CRITICAL,
			"ERROR"		: logging.ERROR,
			"WARNING"	: logging.WARNING,
			"INFO"		: logging.INFO,
			"DEBUG"		: logging.DEBUG,
		}
		
		parser = self.__createParser(debugLevels)
		args = parser.parse_args()

		self.__configurationFile = args.configuration_file
		self.__pastMeasurementsSize = args.past_measurements_size
		self.__debugLevel = debugLevels[args.debug_level]
		self.__setup = args.setup
		
		if not self.__setup:
			configurationFileParser = Parser(
				self,
				self.__configurationFile,
				self.__schemaPath
			)
			configurationFileParser.parse()

	def __createParser(self, debugLevels):
		parser = argparse.ArgumentParser(
			description="An agent passing metrics data from CIM to RHQ servers",
		)
		
		parser.add_argument(
			"--configuration-file",
			help="""Configuration file""",
			required=True,
		)
		parser.add_argument(
			"--debug-level",
			choices=debugLevels.keys(),
			default="INFO",
			help="""The higher, the more info printed""",
		)
		parser.add_argument(
			"--past-measurements-size",
			default=100,
			help="""The number of past measurements stored for each metric""",
			type=int,
		)
		parser.add_argument(
			"--setup",
			action="store_true",
			help="""Generate a new configuration file""",
		)
		
		return parser
