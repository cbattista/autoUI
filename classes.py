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
		self.items = []
		self.controls = {}

		#get args and their default values
		args = inspect.getargspec(self.target.__init__)
		self.argnames = args[0]
		self.argnames.remove('self')

		self.defaults = ()
		self.defaults = self.args[3]

		if self.argnames:
			self.nondefaults = len(self.argnames) - len(self.defaults)
			while len(self.defaults) != len(self.argnames):
				d = list(self.defaults)
				d.insert(0, None)
				self.defaults = tuple(d)
		else:
			self.nondefaults = 0

		#collections...
		#list of arguments (which have their IDs searchable by .find())
		self.args = Items()
		self.methods = Items()
		#control items (buttons etc)
		self.controls = {}
		#all the items		
		self.items = []
		#init button
		self.init = wx.Button(self.parent, -1, 'Init')
		self.controls[str(self.init.GetId())] = self.init	

		#if this thing has a parent we need a 'return button'
		if self.parent:
			self.done = wx.Button(self.parent, -1, 'Return')
			self.controls[str(self.done.GetId())] = self.done

		#construct the args now
		self.constructArgs()	

		#and then the methods
		for f in inspect.getmembers(self.target):
			#if this is a user defined, public function, create a frame for its arguments
			if inspect.isbuiltin(f[0]) or f[0].startswith('_'):
				pass
			else:
				item = f[1]
				item = MethWidget(item)  #hehehe
				self.methods.append(item)


	def Return(self):
		pass

	
