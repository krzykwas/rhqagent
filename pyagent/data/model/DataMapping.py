#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 09-06-2012
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

class DataMapping(object):
	"""
	Data mapping between two servers - one providing data and one receiving data
	"""

	def __init__(self, srcServer, mappedObject, dstServersMappings):
		self.__srcServer = srcServer
		self.__mappedObject = mappedObject
		self.__dstServersMappings = dstServersMappings

	def getSrcServer(self):
		return self.__srcServer

	def getMappedObject(self):
		return self.__mappedObject

	def getDstServersMappings(self):
		return self.__dstServersMappings
	
	def __str__(self):
		return "{0}.{1}.{2}@{3}".format(
			self.__mappedObject.getName(),
			self.__mappedObject.getIndex(),
			self.__mappedObject.getAttribute(),
			self.__srcServer.getName()
		)
