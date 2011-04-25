#test_autoUI.py

import sys
import os
import unittest
import wx

sys.path.append(os.path.split(os.getcwd())[0])

import values
import arguments
import methods

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

class TestCMs(unittest.TestCase):
	pass

if __name__ == '__main__':
    unittest.main()

