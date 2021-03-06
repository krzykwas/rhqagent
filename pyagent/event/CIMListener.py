#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 13-10-2012
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

from ..exception.CIMListenerException import CIMListenerException
from BaseHTTPServer import HTTPServer
import logging

class CIMListener(object):
	"""
	This is a CIM XML listener implemented as a simple HTTP server
	bound to a local port on this computer. A subscription to a CIMOM
	instance must be made so that this listener received CIM messages.
	"""
	
	def __init__(self, cimHandlerClass):
		self.__logger = logging.getLogger(__name__)
		self.__cimHandlerClass = cimHandlerClass

	def register(self, callback):
		"""
		Registers a callback invoked when an event arrives.
		"""
		self.__cimHandlerClass.register(callback)

	def unregister(self, callback):
		"""
		Unregisters a registered callback. For unregistered ones nothing is done.
		"""
		self.__cimHandlerClass.unregister(callback)
	
	def run(self, port):
		try:
			httpServer = HTTPServer(('', port), self.__cimHandlerClass)
			self.__logger.debug("CIM listener started on port {0}.".format(port))
			httpServer.serve_forever()
		except Exception as e:
			self.__logger.error(e)
			raise CIMListenerException("Initialization failed. The chosen port may be busy. Try again?")
