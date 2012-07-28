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

class Param(object):
	"""
	Callback parameter - holds info about a server that should be queried for param value
	"""

	def __init__(self, srcServer, mappedObject):
		self.__srcServer = srcServer
		self.__mappedObject = mappedObject
		
	def getSrcServer(self):
		return self.__srcServer
	
	def getMappedObject(self):
		return self.__mappedObject
	
	def __str__(self):
		return "{0}.{1}.{2}@{3}".format(
			self.__mappedObject.getName(),
			self.__mappedObject.getIndex(),
			self.__mappedObject.getAttribute(),
			self.__srcServer.getName()
		)
