#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
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

from abc import ABCMeta
from abc import abstractmethod

class AbstractDataSender(object):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def __init__(self, dstServer):
		self.__dstServer = dstServer

	@abstractmethod
	def authenticate(self):
		"""
		Authenticates with dstServer.
		"""
		pass
	
	@abstractmethod
	def connect(self):
		"""
		Opens a connection to dstServer.
		"""
		pass
	
	@abstractmethod
	def sendAvailabilityState(self, state):
		"""
		Sends a message indicating that	either the agent is still alive
		(state == "UP") or the opposite when it is going offline (state == "DOWN").
		"""
		pass
	
	@abstractmethod
	def sendData(self, mappedObject):
		"""
		Sends metric data.
		"""
		pass

	def getDstServer(self):
		return self.__dstServer
