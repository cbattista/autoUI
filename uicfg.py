#uicfg.py

constructors = {}
constructors['str'] = ["wx.TextCtrl(self.parent, -1, %s)"]
constructors['int'] = ["wx.SpintCtrl(self.parent, -1, str(%s))"]
constructors['float'] = ["wx.FloatCtrl(self.parent, -1, %s)"]
constructors['list'] = ["ListItems(self.parent, %s)"]
constructors['bool'] = ["wx.Checkbox(self.parent, -1).SetValue(%s)" ]
constructors['dict'] = ["DictItems(self.parent, %s)"]

constructors['NoneType'] = ["wx.TextCtrl(self.parent, -1)", 
							"wx.Button(self.parent, -1, 'Set Type').Disable()", 
							"wx.Button(self.parent, -1, 'Run').Disable()"]

constructors['instance'] = ["ClassItems(%s)"] 

values = {}
values['str'] = "items[1].GetValue()"
values['int'] = "int(items[1].GetValue())"
values['float'] = "items[1].GetFloat()"
values['list'] = "ReadList(items[1:-1])"
values['bool'] = "items[1].GetValue()"
values['dict'] = "ReadDict(items[1:-1])"
values['NoneType'] = "ReadCode(items[1])"
values['instance'] = "ReadClassItems(items[1], items[2])"

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
	items.append("wx.Button(self.parent, -1, 'Edit')")

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
