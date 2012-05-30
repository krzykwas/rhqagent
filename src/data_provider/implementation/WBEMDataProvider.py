#-*- coding: utf-8 -*-

from ..AbstractDataProvider import AbstractDataProvider

class WBEMDataProvider(AbstractDataProvider):
	
	def __init__(self, uri):
		AbstractDataProvider.__init__(self, uri)
		
		print("WBEM connection created")
