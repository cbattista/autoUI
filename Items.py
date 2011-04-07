import wx
import layouts

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


	def setDefault(self, value, arg):
		"""sets a default value for a given arg"""
		index = self.args.index(arg)
		defaults = list(self.defaults)
		defaults[index] = value
		defaults = tuple(defaults)
		self.defaults = defaults
		
