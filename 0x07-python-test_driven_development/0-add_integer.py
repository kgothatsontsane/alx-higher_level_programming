#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function that performs addition on integers"""

def add_integer(a, b=98):
	"""
	Returns the integer addition of a and b
	Float type arguments are type-casted to int before addition
	TypeError is raised if a or b are not integer or float
	"""

	if ((not isinstance(a, int)) and (not isinstance(a, float))):
		raise TypeError("a must be an integer")

	if ((not isinstance(b, int)) and (not isinstance(b, float))):
		raise TypeError("b must be an integer")
	
	return (int(a) + int(b))
