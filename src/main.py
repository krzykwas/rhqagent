# -*- coding: utf-8 -*-

from agent.PyAgent import PyAgent
from settings.Settings import Settings

def getSettings():
	settings = Settings()
	settings.updateWithCommandLine()

	return settings

def main():
	settings = getSettings()
	agent = PyAgent(settings)

	agent.openConnections()

if __name__ == "__main__":
	main()
