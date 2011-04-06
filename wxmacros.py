"""
autoUI by Christian Battista

autoUI is a collection of python modules that are used to create wx apps from classes.  autogenerates a user interface which can be used to manipulate class arguments and functions.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import wx
from values import ValWidget

def ClassItems(value):
	"""code constructor for a class/instance"""
	if str(type(value)) == "<type 'instance'>":
		c = value.__class__
		i = value
	else:
		c = value
		i = None

	items = []

	items.append("wx.StaticText(self.parent, -1, str(%s)" % c)
	items.append("wx.StaticText(self.parent, -1, str(%s)" % i)
	items.append("wx.Button(self.parent, -1, 'Class Edit')")

	return items


def ReadClassItems(c, i):
	#get the value of the text ctrls of class and instance
	c = c.GetValue()
	i = i.GetValue()

	#evaluate the values (i.e., generate class and instance)
	c = eval(c)
	i = eval(i)

	#if there is an instance, use that, otherwise use the class obj	
	if i:
		return i
	else:
		return c

def ListItems(the_list):
	items = []

	for l in the_list:
		item = ValWidget(l)
		items.append(item)

	items.append("wx.Button(self.parent, -1, 'List Edit')")

def ReadList(items):
	values = []
	for i in items:
		if hasattr(i, "read"):
			v = i.read()
			values.append(v)

	return values
