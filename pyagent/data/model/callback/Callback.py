#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-07-2012
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
