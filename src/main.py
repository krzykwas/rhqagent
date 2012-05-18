# -*- coding: utf-8 -*-

from settings.Settings import Settings

import sys

def main():
	settings = Settings()
	settings.updateWithCommandLine(sys.argv)

if __name__ == "__main__":
	main()
