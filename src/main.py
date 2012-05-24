# -*- coding: utf-8 -*-

from settings.Settings import Settings

def getSettings():
	settings = Settings()
	settings.updateWithCommandLine()

	return settings

def main():
	settings = getSettings()

if __name__ == "__main__":
	main()
