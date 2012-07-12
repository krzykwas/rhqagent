#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-07-2012
#

import ast

class Callback(object):
	"""
	User-defined callback to support artificial metrics
	"""

	def __init__(self, functionCode, params, dstServersMappings):
		self.__function = self.prepareFunction(functionCode)
		self.__params = params
		self.__dstServersMappings = dstServersMappings
		
	def prepareFunction(self, functionCode):
		function = "def fun(*args):\n"
		
		for statement in functionCode.split("\n"):
			function += "\t" + statement + "\n"
			
		return function
	
	def getParams(self):
		return self.__params
	
	def getDstServersMappings(self):
		return self.__dstServersMappings
	
	def __call__(self, *args, **kwargs):
		tree = ast.parse(self.__function)
		wrapped = ast.Interactive(body=[tree.body[0]])
		compiled = compile(wrapped, '<string>', 'single')
		namespace = {}
		exec compiled in namespace
		
		return namespace["fun"](args)
