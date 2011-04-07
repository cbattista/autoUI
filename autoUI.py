"""
autoUI by Christian Battista

autoUI is a collection of python modules that are used to create wx apps from classes.  autogenerates a user interface which can be used to manipulate class arguments and functions.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import wx
from classes import *
import testobj
import inspect

class autoUI:
	def __init__(self, target, parent = None):
		self.app = wx.App(False)

		frame = wx.Frame(None)
		if inspect.isclass(target):
			sizer = ClassItem(target, None)
		elif inspect.ismethod(target) or inspect.isfunction(target):
			sizer = MethItem("", target)
		elif isinstance(target):
			sizer = ClassItem(target.__class__, None)
			#hm yeah gotta do something about the 'instance' variables

		self.frame.SetSizerAndFit(sizer)
		frame.Show()

	def go(self):
		self.app.MainLoop()


def main():
	auto = autoUI(testobj.TestObj)
	auto.go()

if __name__ == '__main__':
	main()
