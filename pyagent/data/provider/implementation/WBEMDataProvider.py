# -*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 25-05-2012
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

from ..AbstractDataProvider import AbstractDataProvider
from pywbem.cim_http import AuthError
from pywbem.cim_operations import CIMError
import logging
import pywbem
import thread

class WBEMDataProvider(AbstractDataProvider):
	
	def __init__(self, srcServer):
		AbstractDataProvider.__init__(self, srcServer)
		
		self.__connection = None
		self.__logger = logging.getLogger(__name__)
	
	def authenticate(self):
		"""
		Prepares a connection to a CIM server.
		"""
		srcServer = self.getSrcServer()
		uri = srcServer.getUri()
		username = srcServer.getUsername()
		password = srcServer.getPassword()
		
		self.__connection = pywbem.WBEMConnection(uri, (username, password))
	
	def connect(self):
		"""
		Doesn't do anything as all the work is done in authenticate().
		"""
		pass
	
	def getData(self, mappedObject):
		name = mappedObject.getName()
		namespace = mappedObject.getNamespace()
		index = int(mappedObject.getIndex())
		attribute = mappedObject.getAttribute()
		
		try:
			instances = self.__connection.EnumerateInstances(name, namespace)
			instance = instances[index]
		
			return instance[attribute]
		except AuthError:
			self.__logger.critical("Wrong authentication credentials for {0}.".format(self.getSrcServer().getName()))
			thread.interrupt_main()
		except CIMError as e:
			self.__logger.error("CIM exception for {0}: {1}".format(self.getSrcServer().getName(), e.args))
		except IndexError as e:
			self.__logger.error("In namespace {0} there is no instance #{1} of object {2} with attribute {3}.".format(namespace, index, name, attribute))
