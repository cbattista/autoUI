"""
autoUI by Christian Battista

autoUI is a collection of python modules that are used to create wx apps from classes.  autogenerates a user interface which can be used to manipulate class arguments and functions.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import wx
import layouts
from uicfg import *
from wxmacros import *
from items import *
from arguments import *
from values import *

class CMGrid(ItemGrid):
	def __init__(self, name, value, parent=None, *args, **kwargs):
		ItemGrid.__init__(self, name, value, parent, *args, **kwargs)
		self.argnames = []
		self.defaults = ()

	def setDefault(self, value, arg):
		"""sets a default value for a given arg"""
		index = self.args.index(arg)
		defaults = list(self.defaults)
		defaults[index] = value
		defaults = tuple(defaults)
		self.defaults = defaults

	def readArgs(self, function):
		args = inspect.getargspec(function)
		self.argnames = args[0]
		self.argnames.remove('self')

		self.defaults = ()
		self.defaults = args[3]

		if self.argnames:
			self.nondefaults = len(self.argnames) - len(self.defaults)
			while len(self.defaults) != len(self.argnames):
				d = list(self.defaults)
				d.insert(0, None)
				self.defaults = tuple(d)
		else:
			self.nondefaults = 0

	def constructArgs(self):
		self.args = Items()
		for a, d in zip(self.argnames, self.defaults):
			item = ArgItem(a, d, self.parent)
			self.args.append(item)
			self.items.append(item)
		
	def deconstruct(self):
		"""get the values for each of the fields"""
		values = []
		for item in self.args:
			value = item.read()
			value = value[1]
			#check if it's a string that wants to be a dict
			if type(value) == list:
				isDict = False
				v = value[0]
				if type(v) == list:
					if len(v) == 2:
						if v[0].startswith('{'):
							isDict = True

				if isDict:
					d = {}
					for v in value:
						key = v[0].lstrip('{')
						val = v[1]
						d[key] = val
					value = d 

			values.append(value)

		return values

	def run(self):
		"""run the function method (could be a class' init method)
		"""
		values = self.deconstruct()
		#now create an object from the values
		argString = "self.target("
		for a in self.argnames:
			argString += "%s=values[%s]," % (a, self.argnames.index(a))
		argString = argString.rstrip(",")
		argString += ")"
		
		self.result = eval(argString)

class ClassItem(CMGrid):
	def __init__(self, target, parent=None, *args, **kwargs):
		CMGrid.__init__(self, "", target, parent, *args, **kwargs)

	def construct(self):
		"""create the widgets and put them in 
		the appropriate collection"""

		self.items = [] # items for the sizer
		self.controls = {} # control items

		#make an init button
		self.init = self.makeButton('Init')

		#if this thing has a parent we need a 'return button'
		if self.parent:
			self.rtrn = self.makeButton('Return')

		#get args and their default values
		self.readArgs(self.item.__init__)

		#construct the args
		self.constructArgs()	

		#before we move on, let's toss what we have into a nice rectangle
		self.layout()

		self.methods = Items() #ItemList of methods

		#and then the methods
		for f in inspect.getmembers(self.target):
			#if this is a user defined, public function, create a frame for its arguments
			if inspect.isbuiltin(f[0]) or f[0].startswith('_'):
				pass
			else:
				item = f[1]
				item = MethItem(item)  #hehehe
				self.buttons.append(item.btn)
				self.methods.append(item)

		#add the methods to the sizer
		layouts.AddBar(self, self.methods)


	def initialize(self):
		self.run()
		for b in self.buttons:
			b.Enable()
		
	def rtrn(self):
		#return a class instance 
		s = self.parent.Parent.GetSizer()
		s.init.Enable()
		#self obj is the value of the initialized thing
		s.setDefault(self.obj, self.name)
		s.Clear(1)
		s.construct()				
		self.parent.Parent.Layout()
		s.initialize()
		self.parent.Destroy()	
		
	
