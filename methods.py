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

class Methods:
	def __init__(self, methods = [], parent=None):
		self.methods = methods

	def append(self, method):
		self.methods.append(method)

	def names(self):
		names = []
		for m in self.methods:
			self.methods.append(m.name)
		return names

	def index(self, method):
		index = -1
		for m in self.methods:
			index += 1
			if name == m.name:
				return index

		return index

class MethWidget(wx.GridBagSizer):
	"""Yeah I have to admit here that I could just as easily be calling 
	this "MethodWidget" but I think using the word "Meth" is funny
	"""
	wx.GridBagSizer.__init__(self, *args, **kwargs)
