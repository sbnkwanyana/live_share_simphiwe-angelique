#!/usr/bin/python3
"""
Air BnB clone dummy project
"""

class AirBnB():
	"""
	Class documentation for project
	"""

	__counter = 0

	def __init__(self, id=None):
		if id == None:
			__counter += 1
	
	def aFunction(self):
		"""
		"""
		print("hi")

	@property
	def Name(self):
		return "Name"