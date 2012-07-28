#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 13-06-2012
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

class Measurement(object):
	"""
	Represents a single measurement taken at intervals specified by the user.
	Data is taken from a certain source server and sent to a destination server.
	"""

	def __init__(self, srcServer, mappedObject, dstServerMapping, value, timestamp):
		"""
		@param srcServer: describes the source server that provides data  
		@param mappedObject: serves to locate the monitored object in the source server
		@param dstServerMapping: contains information on the destination server to which data is sent
		@param value: the value of the measurement
		"""
		
		self.__mappedObject = mappedObject
		self.__srcServer = srcServer
		self.__dstServerMapping = dstServerMapping
		self.__value = value
		self.__timestamp = timestamp

	def getMappedObject(self):
		return self.__mappedObject

	def getSrcServer(self):
		return self.__srcServer

	def getDstServerMapping(self):
		return self.__dstServerMapping

	def getValue(self):
		return self.__value	

	def getTimestamp(self):
		return self.__timestamp
	
	@property
	def value(self):
		return self.getValue()

	@property
	def timestamp(self):
		return self.getTimestamp()
