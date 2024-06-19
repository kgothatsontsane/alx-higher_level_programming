#0-add_integer.txt

==============================
HOW TO USE 0-add_integer.py
==============================
This module defines an integer addition function: add_integer(a, b=98).

Usage
=====
add_integer(a, b) returns the addition of two argumens: a and b
a and b must be numbers or else an error will be raised.
::
>>> add_integer = __import__('0-add_integer').add_integer
>>> add_integer(2,5)
7

::
>>> add_integer(2, -3)
-1


::
>>> add_integer(4.0, 9.0)
13


Float type arguments for a and b are type-casted to int
::
>>> add_integer(-4.5, 1.2)
-3

::
>>> add_integer(4.5, -1.2)
3

You can add float and non-float numbers together
::
>>> add_integer(4.7, 2)
6

The second argument is optional and it is initialised to 98 by default
::
>>> add_integer(2)
100