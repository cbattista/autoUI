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

class Arguments:
	"""group of arguments that could belong to a function or class
	argwidgets - list of ArgWidget objects
	parent - parent function or class
	"""
	def __init__(self, widgets = [], parent=None):
		self.parent = parent
		self.widgets = widgets
	
	def append(self, widget):
		self.widgets.append(widget)

	def find(self, ID):
		for w in self.widgets:
			if str(ID) in w.children.keys():
				return w.children[str(ID)]

		return None
		
	def names(self):
		names = []
		for w in self.widgets:
			names.append(w.name)
		return names

	def index(self, name):
		index = -1
		for w in self.widgets:
			index += 1
			if name == w.name:
				return index

		return index

class ArgWidget(wx.GridBagSizer):
	def __init__(self, name, value, parent = None, *args, **kwargs):
		"""name = name of the argument
		value = value, if any (otherwise None)
		parent = the class that this arg belongs to
		"""

		wx.GridBagSizer.__init__(self, *args, **kwargs)

		self.name = name
		self.value = value
		self.parent = parent

		#controls = dictionary of the ids of different control components
		self.controls = {}
		#items that the sizer will be sizing in list form
		self.items = []		
		self.construct()

	def makeLabel(self):
		"""make a label with the argument's name"""
		text = wx.StaticText(self.parent, -1, "%s = " % self.name)
		self.items.append(text)

	def construct(self):
		"""build argwidget contents"""
		self.makeLabel()
		item = ValWidget(self.parent, value)
		self.items.append(item)
		self.controls = dict(self.controls, **item.controls)
		
	def layout():
		"""layout the items in the sizer"""
		layouts.LayoutGrid(self)

	def read(self):
		"""return the name and value of this argument"""
		value = self.value.read()
		return name, value
