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

class ArgWidget(ItemGrid):
	def __init__(self, name, value, parent = None, *args, **kwargs):
		"""name = name of the argument
		value = value, if any (otherwise None)
		parent = the class that this arg belongs to
		"""

		ItemGrid.__init__(self, name, value, parent, *args, **kwargs)

		#controls = dictionary of the ids of different control components
		self.controls = {}
		#items that the sizer will be sizing in list form
		self.items = []		
		self.construct()

	def construct(self):
		self.items = []
		self.controls = {}

		"""build argwidget contents"""
		self.makeLabel()
		item = ValWidget(self.parent, value)
		self.items.append(item)
		self.controls = dict(self.controls, **item.controls)
		
	def read(self):
		"""return the name and value of this argument"""
		value = self.value.read()
		return name, value
