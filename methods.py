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
from classes import *
from arguments import *

class MethItem(CMGrid):
	"""Yeah I have to admit here that I could just as easily be calling 
	this "MethodItem" but I think using the word "Meth" is funny
	"""
	def __init__(self, name, method, parent=None, *args, **kwargs):
		ItemGrid.__init__(self, name, method, parent, *args, **kwargs)

		args = inspect.getargspec(method)
		self.argnames = args[0]
		
	def construct(self):
		"""make the widgets for the args
		and put them into the appropriate collections
		"""

		#collections
		self.items = []
		self.args = Items()
		self.controls = {}

		#make the button
		self.btn = self.makeButton(self.name)	

		self.readArgs(self.item)
		self.constructArgs()

		self.layout()

	def layout(self):
		layouts.LayoutGrid("Bar")
	
