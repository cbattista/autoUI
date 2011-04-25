#test_autoUI.py

import sys
import os
import unittest
import wx

sys.path.append(os.path.split(os.getcwd())[0])

import values
import arguments

class TestItems(unittest.TestCase):

	def testValue(self, value="test", parent=None):
		self.tv = values.ValItem(value, parent)
		self.assertTrue(self.tv.read() == value)

	def testArgument(self, name="testArg", value="test", parent=None):
		self.arg = arguments.ArgItem(name, value, parent)
		hasName = self.arg.name == name
		hasValue = self.arg.read() == value
		self.assertTrue(hasName and hasValue)

class TestCMs(unittest.TestCase):
	pass

if __name__ == '__main__':
    unittest.main()

