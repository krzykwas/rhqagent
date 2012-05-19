# -*- coding: utf-8 -*-

from settings.Settings import Settings

def main():
	settings = Settings()
	settings.updateWithCommandLine()

if __name__ == "__main__":
	main()
