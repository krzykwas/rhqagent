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

class DstServer(object):
	"""
	Represents a server receiving data, so far it will be always an RHQ server.
	"""

	def __init__(self, name, protocol, uri, username, password):
		self.__name = name
		self.__protocol = protocol
		self.__uri = uri
		self.__username = username
		self.__password = password
	
	def getName(self):
		return self.__name
	
	def getProtocol(self):
		return self.__protocol
	
	def getUri(self):
		return self.__uri
	
	def getUsername(self):
		return self.__username
	
	def getPassword(self):
		return self.__password
