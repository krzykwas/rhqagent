#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-10-2012
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

from BaseHTTPServer import BaseHTTPRequestHandler
import logging

class CIMRequestHandler(BaseHTTPRequestHandler):
	"""
	Listens for messages sent by CIM over HTTP.
	"""

	protocol_version = 'HTTP/1.1'
	
	#Holds registered callbacks
	__callbacks = []
	
	def __init__(self, request, client_address, server):
		BaseHTTPRequestHandler.__init__(self, request, client_address, server)
		
		self.__logger = logging.getLogger(__name__)	

	@staticmethod
	def fireEvent(indication):
		"""
		Executes all the registered callbacks when an event occurs.
		"""
		for callback in CIMRequestHandler.__callbacks:
			callback(indication)

	@staticmethod
	def register(callback):
		"""
		Registers a callback invoked when an event arrives.
		"""
		CIMRequestHandler.__callbacks.append(callback)

	@staticmethod
	def unregister(callback):
		"""
		Unregisters a registered callback. For unregistered ones nothing is done.
		"""
		try:
			CIMRequestHandler.__callbacks.remove(callback)
		except ValueError:
			pass
		
	def do_GET(self):
		try:
			response = """
			<!DOCTYPE html>
			<html>
				<head>
					<title>Who am I?</title>
				</head>
				<body>
					<h1>I'm a part of PyAgent. My task is to process CIM XML messages
					and handle received indications.</h1>
				</body>
			</html>
			""";
			
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.send_header("Content-length", len(response))
			self.end_headers()
			self.wfile.write(response)
		except IOError as e:
			self.send_error(500, "An error has occurred while processing a GET request.")
			self.__logger.error(e)

	def do_POST(self):
		pass
