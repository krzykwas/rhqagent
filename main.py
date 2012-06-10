#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 19-05-2012
#

from agent.PyAgent import PyAgent
from settings.Settings import Settings

def getSettings():
	settings = Settings()
	settings.updateWithCommandLine()

	return settings

def main():
	settings = getSettings()
	agent = PyAgent(settings)

if __name__ == "__main__":
	main()
