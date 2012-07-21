#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 19-05-2012
#

from agent.PyAgent import PyAgent
from settings.Settings import Settings
import logging
from settings.configurationFile.Generator import Generator

def getSettings():
	settings = Settings()
	settings.updateWithCommandLine()

	return settings

def generateConfigurationFile(settings):
	configurationFileGenerator = Generator(settings)
	configurationFileGenerator.generate()

def startPyAgent(settings):
	agent = PyAgent(settings)
	agent.beginWork()

def main():
	settings = getSettings()
	
	try:
		logging.basicConfig(level=settings.getDebugLevel())
		logger = logging.getLogger(__name__)
		
		if settings.getSetup():
			generateConfigurationFile(settings)
		else:
			startPyAgent(settings)
	except KeyboardInterrupt:
		pass
	except Exception as exception:
		logger.critical(exception.args)
		logging.shutdown()

if __name__ == "__main__":
	main()
