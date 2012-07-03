#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 21-06-2012
#

from data.sender.AbstractDataSender import AbstractDataSender
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
		
		self.__restClient = self.__RestClient(
			self.getDstServer().getUri(),
			self.getDstServer().getUsername(),
			self.getDstServer().getPassword()
		)
		
		self.__logger = logging.getLogger(__name__)
		
	def authenticate(self):
		pass
	
	def connect(self):
		try:
			self.__createPlatform()
			self.__getSchedules()
		except Exception as e:
			self.__logger.critical("Unexpected exception thrown while initiating connection with RHQ: " + str(e))
			thread.interrupt_main()
	
	def sendData(self, measurement):
		timestamp = int(time.time())
		mapping = measurement.getDstServerMapping()
		schedule = self.__getSchedule(mapping.getMapTo())
		
		try:
			mapping.setUpdateInterval(schedule["collectionInterval"])
		except KeyError:
			self.__logger.warning("Update interval not defined for schedule {0}".format(mapping.getMapTo()))
		
		scheduleId = schedule["scheduleId"]
		value = measurement.getValue()
		
		if schedule["type"].lower() == "measurement":
			self.__sendMeasurement(scheduleId, timestamp, value)
		else:
			self.__sendTrait(scheduleId, value)
		
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

	def __createPlatform(self):
		uri = "resource/platform/" + self.__platformName
		data = json.dumps({"value" : self.__platformType})
		
		responseJson = self.__restClient.request(uri, data)
		response = json.loads(responseJson)
		self.__platformId = response["resourceId"]
		
	def __getSchedules(self):
		uri = "resource/{0}/schedules".format(self.__platformId)
		self.__schedules = json.loads(self.__restClient.request(uri))
		
	def __getSchedule(self, scheduleName):
		for schedule in self.__schedules:
			if schedule["scheduleName"] == scheduleName:
				return schedule
			
		raise ValueError("No schedule named {0} found".format(scheduleName))
	
	class __RestClient(object):
		
		def __init__(self, baseUri, username, password):
			self.__baseUri = baseUri + "/rest/1/"
			self.__username = username
			self.__password = password

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
