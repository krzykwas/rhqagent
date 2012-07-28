#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 19-05-2012
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from agent.PyAgent import PyAgent
from settings.Settings import Settings
from settings.configurationFile.Generator import Generator
import logging

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
