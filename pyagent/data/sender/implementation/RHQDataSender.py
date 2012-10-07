#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 21-06-2012
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

from ..AbstractDataSender import AbstractDataSender
import json
import logging
import platform
import socket
import thread
import time
import urllib2

class RHQDataSender(AbstractDataSender):
	"""
	Sends data to an RHQ server.
	"""
	
	def __init__(self, dstServer):
		AbstractDataSender.__init__(self, dstServer)
		
		self.__platformId = None
		self.__platformName = socket.gethostname() + "-python"
		self.__platformType = "Python" if platform.system() == "" else platform.system()
		
		self.__schedules = None
		
		self.__restClient = self.__RestClient(self.getDstServer())
		self.__logger = logging.getLogger(__name__)
		
	def authenticate(self):
		pass
	
	def connect(self):
		try:
			self.__createPlatform()
			self.__getSchedules()
		except Exception as e:
			self.__logger.critical("Unexpected exception thrown while initiating a connection with RHQ: " + str(e))
			thread.interrupt_main()
	
	def sendAvailabilityState(self, state):
		uri = "resource/" + self.__platformId + "/availability"
		timestamp = self.getTimestamp()
		data = json.dumps({
			"type": state,
			"resourceId": self.__platformId,
			"since": timestamp,
			"until": timestamp + 3600,
		})
		self.__restClient.request(uri, data, "PUT")
	
	def sendData(self, measurement):
		timestamp = self.getTimestamp()
		mapping = measurement.getDstServerMapping()
		schedule = self.__getSchedule(mapping.getMapTo())
		
		if not schedule["enabled"]:
			self.__logger.warning("Schedule named {0} disabled".format(mapping.getMapTo()))
			return
		
		try:
			mapping.setUpdateInterval(schedule["collectionInterval"])
			self.__logger.debug(
				"Update interval for schedule named {0} overriden with {1}".format(
					mapping.getMapTo(),
					schedule["collectionInterval"]
				)
			)
		except KeyError:
			self.__logger.warning("Update interval not defined for schedule {0}".format(mapping.getMapTo()))
		
		scheduleId = schedule["scheduleId"]
		scheduleType = schedule["type"].lower()
		value = measurement.getValue()

		if scheduleType == "measurement":
			self.__sendMeasurement(scheduleId, timestamp, value)
		elif scheduleType == "trait":
			self.__sendTrait(scheduleId, value)
	
	def getTimestamp(self):
		"""
		Returns current timestamp converted to integer. 
		"""
		return int(time.time())
	
	def __createPlatform(self):
		uri = "resource/platform/" + self.__platformName
		data = json.dumps({"value" : self.__platformType})
		
		responseJson = self.__restClient.request(uri, data)
		response = json.loads(responseJson)
		self.__platformId = response["resourceId"]
		
		self.__logger.debug("Platform with id {0} created".format(self.__platformId))
	
	def __getSchedule(self, scheduleName):
		for schedule in self.__schedules:
			if schedule["scheduleName"] == scheduleName:
				return schedule
			
		raise KeyError("No schedule named {0} found".format(scheduleName))
	
	def __getSchedules(self):
		uri = "resource/{0}/schedules".format(self.__platformId)
		self.__schedules = json.loads(self.__restClient.request(uri))
		
		self.__logger.debug("Following schedules found:\n{0}".format(json.dumps(self.__schedules, indent=3)))
		
	def __sendMeasurement(self, scheduleId, timestamp, value):
		uri = "metric/data/{0}/raw/{1}".format(scheduleId, timestamp)
		params = json.dumps({
			"timeStamp" : timestamp,
			"value" : value,
			"scheduleId" : scheduleId
		})
		
		self.__restClient.request(uri, params, "PUT")

	def __sendTrait(self, scheduleId, value):
		uri = "metric/data/{0}/trait".format(scheduleId)
		self.__restClient.request(uri, json.dumps({"value": value}), "PUT")

	class __RestClient(object):
		
		def __init__(self, dstServer):
			self.__baseUri = dstServer.getUri() + "/rest/1/"
			self.__username = dstServer.getUsername()
			self.__password = dstServer.getPassword()

		def request(self, resource, params=None, method=None):
			uri = self.__baseUri + resource
				
			passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
			passman.add_password(None, uri, self.__username, self.__password)
			authhandler = urllib2.HTTPBasicAuthHandler(passman)
			opener = urllib2.build_opener(authhandler)
			#opener = urllib2.build_opener(authhandler, urllib2.HTTPHandler(debuglevel=1))

			headers = {
				"accept": "application/json",
				"content-type": "application/json"
			}
			
			request = urllib2.Request(uri, data=params, headers=headers)
			
			if method is not None:
				request.get_method = lambda: method
			
			return opener.open(request).read()
