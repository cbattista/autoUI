#layouts.py

def GoldenRatio(items):
	numitems = len(items)

	get the ratio of the golden ratio 
	c = 1.61803399 * numitems
	r = numitems - c
	return r, c

def LayoutGrid(sizer, posFunc=GoldenRatio):
	r, c = posFunc(sizer.items)

	sizer.SetRows(r)
	sizer.SetCols(c)

	index = 0
	for r in range(0, rows):
		for c in range(0, cols):
			item = items[index] 
			sizer.Add(item, [r,c])
			index+=1

	return r, c

def AddBar(sizer, items):
	r = sizer.GetRows()
	c = sizer.GetCols()

	for i in items:
		r+= 1
		sizer.SetRows(r)
		sizer.Add(i, [r, 0], span=[1, c])

