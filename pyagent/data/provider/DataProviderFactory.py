#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 24-05-2012
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

from ...exception.ProtocolFormatException import ProtocolFormatException
import importlib
import pkgutil

class DataProviderFactory(object):

	def getDataProvider(self, srcServer):
		"""
		Basing on the protocol name finds a proper module which	name is composed
		of uppercase protocol name and a string <<DataProvider>>, like 
		WBEMDataProvider or HTTPDataProvider, or FTPDataProvider and so on.

		As a second step, imports a class called in the same manner as the module, 
		instantiates it and returns the created object.

		In case of any error None is returned instead of an expected data provider instance.
		"""
		try:
			name = self.getDataProviderClassName(srcServer.getProtocol())

			module = importlib.import_module(".implementation." + name, "pyagent.data.provider")
			dataProviderClassObject = getattr(module, name)

			dataProvider = dataProviderClassObject(srcServer)

			return dataProvider
		except ImportError:
			return None

	def getDataProviderClassName(self, protocol):
		if False in [char.isalpha() for char in protocol]:
			raise ProtocolFormatException("Invalid protocol name - only letters allowed")
		
		return protocol.upper() + "DataProvider"
	
	def getDataProviderNames(self):
		dataProviderNames = []
		
		module = importlib.import_module(".implementation", "pyagent.data.provider")
		for importer, modname, ispkg in pkgutil.iter_modules(module.__path__):
			if modname.endswith("DataProvider"):
				dataProviderNames.append(modname)
			
		return dataProviderNames
