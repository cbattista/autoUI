"""
autoUI by Christian Battista

autoUI is a collection of python modules that are used to create wx apps from classes.  autogenerates a user interface which can be used to manipulate class arguments and functions.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

def GoldenRatio(items):
	numitems = len(items)

	#get the ratio of the golden ratio 
	c = numitems / 1.61803399
	c = int(c)
	r = numitems / c
	return r, c

def Bar(items):
	return 1, len(items)

def Pole(items):
	return len(items), 1

def LayoutGrid(sizer, posFunc="GoldenRatio"):
	rows, cols = eval("%s(sizer.items)" % posFunc)

	sizer.SetRows(rows)
	sizer.SetCols(cols)

	index = 0
	for r in range(0, rows):
		for c in range(0, cols):
			item = sizer.items[index] 
			if item:
				sizer.Add(item, [r,c])
			index+=1

	return rows, cols

def AddBar(sizer, items):
	r = sizer.GetRows()
	c = sizer.GetCols()

	for i in items:
		r+= 1
		sizer.SetRows(r)
		sizer.Add(i, [r, 0], span=[1, c])

