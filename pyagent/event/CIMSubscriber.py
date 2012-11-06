# -*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 05-11-2012
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

import logging
import pywbem
import socket
import time

class CIMSubscriber(object):
	"""
	Subscribes or unsubscribes a CIMListener to a CIM server to receive indications
	for a certain CIM class.
	"""

	def __init__(self, uri, username, password, namespace="root/cimv2"):
		"""
		@param uri: CIM server uri, for instance: https://localhost:5988
		@param username, password: CIM server credentials
		"""
		
		self.__FILTER_CREATION_CLASS_NAME = "CIM_IndicationFilter"
		self.__HANDLER_CREATION_CLASS_NAME = "CIM_IndicationHandlerCIMXML"
		
		self.__logger__ = logging.getLogger(__name__)
		
		self.__uri = uri
		self.__username = username
		self.__password = password
		self.__namespace = namespace
		
		self.__client = pywbem.WBEMConnection(self.__uri, (self.__username, self.__password), self.__namespace)

	def subscribe(self, cimClassName, listenerPort, listenerHost=socket.gethostname()):
		"""
		Re-registers with a CIM server.
		"""
		self.unsubscribe(cimClassName, listenerHost)
		
		self.__logger__.debug("Registering a new subscription.")
		
		handlerName = self.__createHandler(listenerHost)
		filterName = self.__createFilter(listenerHost, cimClassName)
		self.__createSubscription(listenerHost, handlerName, filterName)
	
	def unsubscribe(self, cimClassName, listenerHost=socket.gethostname()):
		"""
		Cleans up old registrations.
		"""
		
		self.__logger__.debug("Cleaning up old registrations.")
		
		subscriptionName = self.__getSubscriptionName(listenerHost)
		handlerName = self.__getCIMInstanceName(listenerHost, self.__HANDLER_CREATION_CLASS_NAME)
		filterName = self.__getCIMInstanceName(listenerHost, self.__FILTER_CREATION_CLASS_NAME)

		for name in subscriptionName, filterName, handlerName:
			try:
				self.__client.DeleteInstance(name)
			except Exception as e:
				self.__logger__.error(e)
			finally:
				time.sleep(1)
	

	def __getBindings(self, listenerHost, creationClassName):
		return {
			"SystemCreationClassName": "OMC_UnitaryComputerSystem",
			"SystemName": listenerHost,
			"Name": "PyIndication",
			"CreationClassName": creationClassName
		}

	def __getCIMInstanceName(self, listenerHost, creationClassName, host=None):
		return pywbem.CIMInstanceName(
			creationClassName,
			keybindings=self.__getBindings(listenerHost, creationClassName),
			namespace="root/interop",
			host=host
		)
	
	def __getSubscriptionBindings(self, listenerHost):
		return {
			"Filter": self.__getCIMInstanceName(listenerHost, self.__FILTER_CREATION_CLASS_NAME, self.__uri),
			"Handler": self.__getCIMInstanceName(listenerHost, self.__HANDLER_CREATION_CLASS_NAME, self.__uri)
		}
	
	def __getSubscriptionName(self, listenerHost):
		return pywbem.CIMInstanceName(
			"SFCB_IndicationSubscription",
			keybindings=self.__getSubscriptionBindings(listenerHost),
			namespace="root/interop"
		)
	
	def __createHandler(self, listenerHost):
		"""
		@return: new handler instance's name
		"""
		
		handlerInstance = pywbem.CIMInstance(
			self.__HANDLER_CREATION_CLASS_NAME,
			properties=self.__getBindings(listenerHost, self.__HANDLER_CREATION_CLASS_NAME),
			path=self.__getCIMInstanceName(listenerHost, self.__HANDLER_CREATION_CLASS_NAME)
		)
		handlerInstance["Destination"] = self.__uri
		
		return self.__client.CreateInstance(handlerInstance)
	
	def __createFilter(self, listenerHost, cimClassName):
		"""
		@return: new filter instance's name
		"""
		
		filterInstance = pywbem.CIMInstance(
			self.__FILTER_CREATION_CLASS_NAME,
			properties=self.__getBindings(listenerHost, self.__FILTER_CREATION_CLASS_NAME),
			path=self.__getCIMInstanceName(listenerHost, self.__FILTER_CREATION_CLASS_NAME)
		)
		filterInstance["SourceNamespace"] = "root/cimv2"
		filterInstance["Query"] = "SELECT * FROM {0}".format(cimClassName)
		filterInstance["QueryLanguage"] = "WQL"
		
		return self.__client.CreateInstance(filterInstance)
	
	def __createSubscription(self, listenerHost, handlerName, filterName):
		subscriptionInstance = pywbem.CIMInstance(
			"CIM_IndicationSubscription",
			path=self.__getSubscriptionName(listenerHost)
		)
		subscriptionInstance["Filter"] = filterName
		subscriptionInstance["Handler"] = handlerName
		
		try:
			self.__client.CreateInstance(subscriptionInstance)
		except:
			pass
