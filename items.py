import wx
import layouts
from arguments import *

class Item:
	def __init__(self, items = [], parent=None):
		self.items = items

	def append(self, item):
		self.items.append(item)

	def names(self):
		names = []
		for i in self.items:
			names.append(i.name)
		return names

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
		layouts.LayoutGrid(self)

	def bind(self, event, function):
		self.panel.Bind(event, function)

	def makeLabel(self, label):
		txt = wx.StaticText(self.parent, -1, label)
		self.items.add(txt)

	def makeButton(self, label):
		btn = wx.Button(self.parent, -1, label)
		self.items.add(btn)
		self.addControl(btn)

	def addControl(self, ctrl)
		"""create a ctrl, add it to children"""
		self.controls[str(ctrl.GetId())] = ctrl

	def makeTxtCtrl(self, label=""):
		txtctrl = wx.TextCtrl(self.parent, -1, label)
		self.items.add(txtctrl)
		self.addControl(btn)

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

	def constructArgs(self):
		self.args = []
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
		"""create an instance of the target class (as self.obj)	from values provided in the gui
		"""
		values = self.deconstruct()
		#now create an object from the values
		argString = "self.target("
		for a in self.argnames:
			argString += "%s=values[%s]," % (a, self.argnames.index(a))
		argString = argString.rstrip(",")
		argString += ")"
		
		self.obj = eval(argString)
