"""
autoUI by Christian Battista

autoUI is a collection of python modules that are used to create wx apps from classes.  autogenerates a user interface which can be used to manipulate class arguments and functions.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class NestedObj:
	def __init__(self, a, b=2, c=3):
		self.a = a
		self.b = b
		self.c = c

	def __str__(self):
		return "%s %s %s" % (self.a, self.b, self.c)

class TestObj:
	def __init__(self, items, number = 1.23, chong={'wee' : 'nis', 'pen' : 15}, a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, testobj=NestedObj, testobj2=NestedObj):
		self.items = items
		self.number = number
		self.chong = chong
		self.testobj = testobj
		self.testobj2 = testobj2

	def testFunc(self, testarg=False):
		print testarg
		print self.testobj
		print self.items


	def testFunc2(self, testarg=True):
		print testarg
		print self.testobj2

	def __privateFunc(self, privateArg = 6):
		pass

