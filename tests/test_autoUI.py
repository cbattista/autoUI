#test_autoUI.py

import sys
import os
import unittest
import wx

sys.path.append(os.path.split(os.getcwd())[0])

import values
import arguments
import methods
import classes

class testObj:
	def __init__(self, a=1, b=2.0, c="3", d=[5,6,7]): #, e={'eight': 8, 'nine':9.0, 'ten':'ten', 'eleven': [1,1]}):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		#self.e = e

	def printVals(self):
		print self.a, self.b, self.c
		print self.d
		print self.e

def testFunc(x=1, y="1"):
	print x, y	

class TestItems(unittest.TestCase):

	def testValue(self, value="test", parent=None):
		self.tv = values.ValItem(value, parent)
		self.assertTrue(self.tv.read() == value)

	def testArgument(self, name="testArg", value="test", parent=None):
		self.arg = arguments.ArgItem(name, value, parent)
		hasName = self.arg.name == name
		hasValue = self.arg.read() == value
		self.assertTrue(hasName and hasValue)

	def testMethod(self, name="testMethod", method=testFunc, parent=None):
		self.method = methods.MethItem(name, method, parent)
		self.assertTrue(self.method.name == name)

	def testClass(self, Class=testObj):
		self.Class = classes.ClassItem(Class, parent=None)
		self.assertTrue(len(self.items))

class TestCMs(unittest.TestCase):
	pass

if __name__ == '__main__':
    unittest.main()

