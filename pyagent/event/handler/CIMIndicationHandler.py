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

from .CIMHandler import CIMHandler
from BaseHTTPServer import BaseHTTPRequestHandler
from lxml import etree
import logging
import pywbem

class CIMIndicationHandler(BaseHTTPRequestHandler, CIMHandler):
	"""
	Listens for messages sent by CIM over HTTP.
	"""

	protocol_version = 'HTTP/1.1'
	
	def __init__(self, request, clientAddress, server):
		self.__logger = logging.getLogger(__name__)
		CIMHandler.__init__(self)
		BaseHTTPRequestHandler.__init__(self, request, clientAddress, server)

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

	def __validateMessage(self, xml):
		ref = xml
		expectedElements = ["cim", "message", "simpleexpreq", "expmethodcall", "expparamvalue", "instance"]
			
		for expectedElement in expectedElements:
			ref = list(ref)[0]
			assert ref.tag == expectedElement

	def do_POST(self):
		try:
			contentLength = int(self.headers.get('Content-length'))
			content = self.rfile.read(contentLength)

			self.__logger.debug("Message received: {0}.".format(content))

			xml = etree.fromstring(content)
			self.__validateMessage(xml)
			
			messageId = xml.find("message")[0].attrib["id"]

			self.send_response(200, "OK")
			self.send_header('Content-type', 'application/xml; charset="utf-8"')
			self.send_header('CIMExport', 'MethodResponse')

			response = """
			<?xml version="1.0" encoding="utf-8"?>
			<cim cimversion="2.0" dtdversion="2.0">
				<message id="{0}" protocolversion="1.0">
					<simpleexprsp>
						<expmethodresponse name="ExportIndication">
							<ireturnvalue/>
						</expmethodresponse>
					</simpleexprsp>
				</message>
			</cim>""".format(messageId)
			
			self.__logger.debug("Response sent: {0}".format(response))
			
			self.send_header('Content-length', str(len(response)))
			self.end_headers()
			self.wfile.write(response)
			self.wfile.flush()
			self.wfile.close()

			instance = pywbem.tupleparse.xml_to_tupletree(content)
			self._fireEvent(instance)
		except Exception as e:
			self.__logger.error(e)
			self.send_error(500, "An error has occurred while processing a POST request.")
