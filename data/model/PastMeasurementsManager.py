#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 15-07-2012
#

from data.model.Measurement import Measurement
import time

class PastMeasurementsManager(object):
	"""
	Manages historical measurements, i.e. maps both srcServer and mappedObject
	with a bounded list of appropriate measurements taken in the past
	"""

	def __init__(self, period=100):
		#The maximal number of past measurements stored for a given source server and mapped object 
		self.__PERIOD = period
		
		#A dict: (SrcServer, MappedObject) -> list of Measurement of at most self.__PERIOD size
		self.__pastMeasurements = {}

	def get(self, srcServer, mappedObject):
		"""
		Returns a list of self.__PERIOD most recent measurements taken for the pair
		(srcServer, mappedObject). If there are less than self.__PERIOD such measurements,
		the missing entries are filled with fake measurements with value equal to 0, timestamp
		and dstServerMapping equal to - respectively - the timestamp and the dstServerMapping
		of the oldest known measurement. 
		"""
		key = (srcServer, mappedObject,)
		
		try:
			measurements = self.__pastMeasurements[key]
		except:
			measurements = []

		"""
		Determine the timestamp and dstServerMapping of the oldest measurement (or take current
		timestamp and None as dstServerMapping, if no appropriate measurements taken so far)
		"""
		if len(measurements) > 0:
			timestamp = measurements[-1].getTimestamp()
			dstServerMapping = measurements[-1].getDstServerMapping()
		else:
			timestamp = time.time()
			dstServerMapping = None

		"""
		Adding fake measurements if needed
		"""
		missingCount = self.__PERIOD - len(measurements)
		
		for i in range(missingCount): #@UnusedVariable
			fakeMeasurement = Measurement(srcServer, mappedObject, dstServerMapping, 0, timestamp)
			measurements.append(fakeMeasurement)

		return measurements
	
	def put(self, srcServer, mappedObject, measurement):
		"""
		Inserts measurement at the first position of the list of measurements
		mapped to the tuple (srcServer, mappedObject). If the list gets longer than self.__PERIOD,
		the oldest measurement is removed. 
		"""
		key = (srcServer, mappedObject,)
		
		if key not in self.__pastMeasurements:
			self.__pastMeasurements[key] = []
		
		measurements = self.__pastMeasurements[key]	
		measurements.insert(0, measurement)
		
		if len(measurements) > self.__PERIOD:
			del measurements[self.__PERIOD]
