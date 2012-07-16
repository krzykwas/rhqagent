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

def main():
	settings = getSettings()
	
	try:
		logging.basicConfig(level=settings.getDebugLevel())
		logger = logging.getLogger(__name__)
		
		agent = PyAgent(settings)
		agent.beginWork()
	except Exception as exception:
		logger.critical(exception.args)
		logging.shutdown()

if __name__ == "__main__":
	main()
