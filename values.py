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

class ValItem(ItemGrid):
	def __init__(self, value, parent = None, *args, **kwargs):
		"""value = the value to be displayed/ctrl
		parent = the class that this value belongs to
		"""
		ItemGrid.__init__(self, "", value, parent, *args, **kwargs)
		
	def construct(self):
		self.items = []
		self.controls = {}

		"""construct the widget with components indicated in the components table"""
		self.valtype = str(type(self.item)).split("'")[1]

		if constructors.has_key(self.valtype):
			components = constructors[self.valtype]
		else:
			components = constructors['instance']

		for c in components:
			if c.count("%s"):
				c = c % self.name

			i = eval(c)

			if isinstance(i, wx.Control):
				self.addControl(i)

			self.items.append(i)	
		
	def read(self):
		"""return the value held in this ValItem"""
		value = values[self.valtype]
		value = eval(value)
		return value

