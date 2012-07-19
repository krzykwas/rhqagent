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
		self.__function = self.wrapWithFunction(functionCode)
		self.__params = params
		self.__dstServersMappings = dstServersMappings
			
	def __call__(self, params, *args, **kwargs):
		tree = ast.parse(self.__function)
		wrapped = ast.Interactive(body=[tree.body[0]])
		compiled = compile(wrapped, '<string>', 'single')
		namespace = {}
		exec(compiled, namespace)

		return namespace["fun"](params)
			
	def getDstServersMappings(self):
		return self.__dstServersMappings
	
	def getParams(self):
		return self.__params

	def wrapWithFunction(self, functionCode):
		function = "def fun(params):\n"
		
		for statement in functionCode.split("\n"):
			function += "\t" + statement + "\n"
			
		function += "\tpass\n"
			
		return function
