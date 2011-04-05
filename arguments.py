import wx
import layouts

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

class Arguments:
	"""group of arguments that could belong to a function or class
	argwidgets - list of ArgWidget objects
	parent - parent function or class
	"""
	def __init__(self, argwidgets = [], parent=None):
		self.parent = None
		self.argwidgets = argwidgets
	
	def add(self, argwidget):
		self.argwidgets.append(argwidget)

	def find(self, ID):
		for w in self.widgets:
			if str(ID) in w.children.keys():
				return w.children[str(ID)]
		
		return None
				

class ArgWidget(wx.GridBagSizer):
	"""p
	name = name of the argument
	value = value, if any (otherwise None)
	parent = the class that this arg belongs to
	"""
	def __init__(self, name, value, expected_type = None, ids= {}, parent = None, *args, **kwargs):

		wx.GridBagSizer.__init__(self, *args, **kwargs)

		self.name = name
		self.value = value
		self.parent = parent
		self.expected_type = expected_type

		#controls = dictionary of the ids of different control components
		self.controls = {}
		#items that the sizer will be sizing in list form
		self._items = []
		
		self.makeLabel()
		self.construct()

	def addControl(self, ctrl)
		"""create a text ctrl, add it to children"""
		self.controls[str(ctrl.GetId())] = ctrl

	def makeLabel(self)
		text = wx.StaticText(self.parent, -1, "%s = " % self.name)
		self.items.append(text)

	def construct(self):
		"""construct the widget with components indicated in the components table"""
		text = wx.StaticText(self.parent, -1, "%s = " % self.name)

		valtype = str(type(self.value)).split("'")[1]

		if constructors.has_key(valtype):
			components = constructors[valtype]
		else:
			components = constructors['instance']

		for c in components:
			#there is a special tagging for btns and other ctrls
			if c.count("%s"):
				c = c % self.name

			item = eval(c)

			if isinstance(item, wx.Control):
				self.addControl(item)

			self.items.append(item)	
		
	def layout():
		layouts.LayoutGrid(self)

	def read(self):
		"""get the value of the argument according to the GUI components"""
		value = values[str(type(self.value)).split("'")[1]]
		value = eval(value)
		return value
