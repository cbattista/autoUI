"""
autoUI by Christian Battista

autoUI is a collection of python modules that are used to create wx apps from classes.  autogenerates a user interface which can be used to manipulate class arguments and functions.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import wx
import layouts
from items import *
from values import *
from uicfg import *
from wxmacros import *



class ArgItem(ItemGrid):
	def __init__(self, name, value, parent = None, *args, **kwargs):
		"""name = name of the argument
		value = value, if any (otherwise None)
		parent = the class that this arg belongs to
		"""
		ItemGrid.__init__(self, name, value, parent, *args, **kwargs)

	def construct(self):
		self.items = []
		self.controls = {}
		"""build argwidget contents"""
		self.makeLabel(self.name)
		val_item = ValItem(self.parent, self.item)
		self.value = val_item
		self.items.append(val_item)
		self.controls = dict(self.controls, **val_item.controls)
		self.layout()
		self.panel.Bind(wx.EVT_BUTTON, self.onButton)
		
	def read(self):
		"""return the name and value of this argument"""
		value = self.value.read()
		return name, value

	def edit(self):
		frame = wx.Frame(self.parent, -1)
		classItem = ClassItem(self.item)
		frame.SetSizerAndFit(classItem)
