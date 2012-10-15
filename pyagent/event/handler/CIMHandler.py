#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 15-10-2012
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

class CIMHandler(object):

	#Holds registered callbacks
	__callbacks = []
	
	@staticmethod
	def _fireEvent(indication):
		"""
		Executes all the registered callbacks when an event occurs.
		"""
		for callback in CIMHandler.__callbacks:
			callback(indication)

	@staticmethod
	def register(callback):
		"""
		Registers a callback invoked when an event arrives.
		"""
		CIMHandler.__callbacks.append(callback)

	@staticmethod
	def unregister(callback):
		"""
		Unregisters a registered callback. For unregistered ones nothing is done.
		"""
		try:
			CIMHandler.__callbacks.remove(callback)
		except ValueError:
			pass
