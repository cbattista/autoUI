import wx
import layouts
from arguments import *

class Item:
	def __init__(self, items = [], parent=None):
		self.items = items
		self.current = 0

	def __iter__():	
		return self

	def append(self, item):
		self.items.append(item)

	def names(self):
		names = []
		for i in self.items:
			names.append(i.name)
		return names

	def next(self):
		if len(self.items) > self.current:
			return self.items[current]
		else:
			raise StopIteration

	def index(self.method):
		index = -1
		for m in self.methods:
			index += 1
			if name == m.name:
				return index
		return index

class ItemGrid(wx.GridBagSizer):
	"""Master class for all widgets"""

	def __init__(self, name, item, parent=None, *args, **kwargs):
		wx.GridBagSizer.__init__(self, *args, **kwargs)
		self.name = name
		self.item = item
		self.parent = parent
		
		self.panel = wx.Panel(parent, -1)
		self.construct()
		self.panel.SetSizerAndFit(self)

	def construct(self):
		self.items = []
		self.controls = {}

	def layout(self):
		r, c = layouts.LayoutGrid(self)
		return r, c

	def bind(self, event, function):
		self.panel.Bind(event, function)

	def makeLabel(self, label):
		txt = wx.StaticText(self.parent, -1, label)
		self.items.add(txt)
		return txt

	def makeButton(self, label):
		btn = wx.Button(self.parent, -1, label)
		self.items.add(btn)
		self.addControl(btn)
		return btn

	def addControl(self, ctrl)
		"""create a ctrl, add it to children"""
		self.controls[str(ctrl.GetId())] = ctrl

	def makeTxtCtrl(self, label=""):
		txtctrl = wx.TextCtrl(self.parent, -1, label)
		self.items.add(txtctrl)
		self.addControl(txtctrl)
		return txtctrl

	def onButton(self, event):
		ID = event.GetId()
		if self.controls.has_key(str(ID)):
			btn = self.controlstr(ID)]
			label = btn.GetLabel()
			exec(events[label])

	def onTextCtrl(self, event):
		#not really sure how many fields we really want to pay attention to
		exec(events['textctrl'])

class CMGrid(ItemGrid):
	def __init__(self, name, value, parent=None, *args, **kwargs):
		ItemGrid.__init__(self, name, method, parent, *args, **kwargs)
		self.argnames = []
		self.defaults = ()

	def setDefault(self, value, arg):
		"""sets a default value for a given arg"""
		index = self.args.index(arg)
		defaults = list(self.defaults)
		defaults[index] = value
		defaults = tuple(defaults)
		self.defaults = defaults

	def readArgs(self, function):
		args = inspect.getargspec(function)
		self.argnames = args[0]
		self.argnames.remove('self')

		self.defaults = ()
		self.defaults = self.args[3]

		if self.argnames:
			self.nondefaults = len(self.argnames) - len(self.defaults)
			while len(self.defaults) != len(self.argnames):
				d = list(self.defaults)
				d.insert(0, None)
				self.defaults = tuple(d)
		else:
			self.nondefaults = 0

	def constructArgs(self):
		self.args = Items
		for a, d in (self.argnames, self.defaults):
			item = ArgWidget(a, d, self.parent)
			self.args.append(item)
			self.items.append(item)
		
	def deconstruct(self):
		"""get the values for each of the fields"""
		values = []
		for item in self.args:
			value = item.read()
			value = value[1]
			#check if it's a string that wants to be a dict
			if type(value) == list:
				isDict = False
				v = value[0]
				if type(v) == list:
					if len(v) == 2:
						if v[0].startswith('{'):
							isDict = True

				if isDict:
					d = {}
					for v in value:
						key = v[0].lstrip('{')
						val = v[1]
						d[key] = val
					value = d 

			values.append(value)

		return values

	def run(self):
		"""run the function method (could be a class' init method)
		"""
		values = self.deconstruct()
		#now create an object from the values
		argString = "self.target("
		for a in self.argnames:
			argString += "%s=values[%s]," % (a, self.argnames.index(a))
		argString = argString.rstrip(",")
		argString += ")"
		
		self.result = eval(argString)
