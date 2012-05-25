#-*- coding: utf-8 -*-

from ..AbstractConnection import AbstractConnection

class HTTPConnection(AbstractConnection):
	
	def __init__(self):
		print("HTTP connection created")
