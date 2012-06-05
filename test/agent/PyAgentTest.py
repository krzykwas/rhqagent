#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-06-2012
#

from agent.PyAgent import PyAgent
from settings.Settings import Settings
import unittest

class PyAgentTest(unittest.TestCase):
	"""
	TODO: add unit tests
	"""
	class SettingsMock(Settings):
		pass

	def setUp(self):
		self.__settigsMock = self.SettingsMock()
		self.__sut = PyAgent(self.__settigsMock)
