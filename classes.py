"""
autoUI by Christian Battista

autoUI is a collection of python modules that are used to create wx apps from classes.  autogenerates a user interface which can be used to manipulate class arguments and functions.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import wx
import layouts
from values import *
from uicfg import *
from wxmacros import *

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
		self.readArgs(self.target.__init__)

		#construct the args
		self.constructArgs()	

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
		
	
