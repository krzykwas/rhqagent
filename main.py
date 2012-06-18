#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 19-05-2012
#

from agent.PyAgent import PyAgent
from settings.Settings import Settings
import logging

def getSettings():
	settings = Settings()
	settings.updateWithCommandLine()

	return settings

def configureLogging():
	logging.basicConfig()

def main():
	configureLogging()
	logger = logging.getLogger(__name__)
	
	try:
		settings = getSettings()
		agent = PyAgent(settings)
		agent.beginWork()
	except Exception as exception:
		logger.critical(exception.args)

if __name__ == "__main__":
	main()
