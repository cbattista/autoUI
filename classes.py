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

class ClassWidget(wx.GridBagSizer):
	def __init__(self, target, parent=None, *args, **kwargs):
		wx.GridBagSizer.__init__(self, *args, **kwargs)
		self.parent = parent

		self.target = target

		self.instance = None 

		self.args = inspect.getargspec(self.target.__init__)

		self.argnames = self.args=[0]

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


		self.construct()

	def construct(self):
		"""create the widgets and put them in 
		the appropriate collection"""

		#list of arguments (which have their IDs searchable by .find())
		self.args = Arguments()
		self.methods = Methods()

		#control items (buttons etc)
		self.controls = {}
		#all the items		
		self.items = []


		#init button
		self.init = wx.Button(self.parent, -1, 'Init')
		self.controls[str(self.init.GetId())] = self.init	

		#create the arguments
		for a, d in (self.argnames, self.defaults):
			item = ArgWidget(a, d, self.parent)
			self.args.append(item)
			self.items.append(item)

		self.items.append(self.init)	

		#also need methods
		for f in inspect.getmembers(self.target):
			#if this is a user defined, public function, create a frame for its arguments
			if inspect.isbuiltin(f[0]) or f[0].startswith('_'):
				pass
			else:
				b_id += 1
				self.functions.append(f[1])
				button = wx.Button(self.parent, b_id, f[0])
				button.Disable()
				self.buttons.append(button)
				functionFrame = objSizer(self.parent, f[1], recurse=False)
				self.items['methods'].append(functionFrame)
		
	def setDefault(self, value, arg):
		"""sets a default value for a given arg"""
		index = self.args.index(arg)
		defaults = list(self.defaults)
		defaults[index] = value
		defaults = tuple(defaults)
		self.defaults = defaults

	def layout(self):
		"""layout the items in the sizer"""
		layouts.LayoutGrid(self)

	def onButton(self):
		for
