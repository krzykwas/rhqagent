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

from datetime import datetime, timedelta

class DstServerMapping(object):
	
	def __init__(self, dstServer, mapTo, updateInterval):
		"""
		@param dstServer: describes the server to which collected data is sent
		@param mapTo: an identifier of a dstServer's resource to which data is mapped,
			for instance for RHQ it wolud be a scheduleId
		@param updateInterval: how often to refresh the measurement
		"""
		
		self.__dstServer = dstServer
		self.__mapTo = mapTo
		self.__lastAccessed = datetime.min;
		self.setUpdateInterval(updateInterval)
		
	def getDstServer(self):
		return self.__dstServer
	
	def getMapTo(self):
		return self.__mapTo
	
	def getUpdateInterval(self):
		return self.__updateInterval
	
	def setUpdateInterval(self, updateInterval):
		self.__updateInterval = int(updateInterval)
	
	def isDue(self):
		return (self.__lastAccessed + timedelta(seconds=self.__updateInterval)) < datetime.now()
	
	def setLastAccessedNow(self):
		self.__lastAccessed = datetime.now()
