#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 25-05-2012
#

from ..AbstractDataProvider import AbstractDataProvider

class WBEMDataProvider(AbstractDataProvider):
	
	def __init__(self, srcServer):
		AbstractDataProvider.__init__(self, srcServer)
		
		print("WBEM connection created")
