#wxmacros.py
import wx

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
