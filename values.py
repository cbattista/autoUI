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

class ValWidget(wx.GridBagSizer):
	def __init__(self, value, parent = None, *args, **kwargs):
		wx.GridBagSizer.__init__(self, *args, **kwargs)
		
		self.value = value
		self.parent = parent

		self.construct()
		self.controls = {}

	def addControl(self, ctrl)
		"""create a text ctrl, add it to children"""
		self.controls[str(ctrl.GetId())] = ctrl

	def construct(self):
		"""construct the widget with components indicated in the components table"""
		valtype = str(type(self.value)).split("'")[1]

		if constructors.has_key(valtype):
			components = constructors[valtype]
		else:
			components = constructors['instance']

		for c in components:
			if c.count("%s"):
				c = c % self.name

			item = eval(c)

			if isinstance(item, wx.Control):
				self.addControl(item)

			self.items.append(item)	
		
	def layout():
		"""layout the items in the sizer"""
		layouts.LayoutGrid(self)

	def read(self):
		"""return the value held in this ValWidget"""
		value = values[str(type(self.value)).split("'")[1]]
		value = eval(value)
		return value

