#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 12-06-2012
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

from threading import Thread
import logging

try:
	from queue import Empty #@UnresolvedImport
except:
	from Queue import Empty #@UnresolvedImport

class SendDataThread(Thread):
	
	def __init__(self, args):
		Thread.__init__(self, args=args)
		self.setDaemon(True)
		
		self.__pyAgent = args[0]
		
		self.__logger = logging.getLogger(__name__)
		self.__logger.debug("Starting sending data")

	def run(self):
		metricsDataQueue = self.__pyAgent.getMetricsDataQueue()
		
		while True:
			try:
				measurement = metricsDataQueue.get(True, 5)
				dstServer = measurement.getDstServerMapping().getDstServer()
				dataSender = self.__pyAgent.getDataSenders()[dstServer]
				dataSender.sendData(measurement)
			except Empty:
				pass
			except Exception as e:
				self.__logger.error(e)
