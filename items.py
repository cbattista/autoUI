import wx
import layouts
import inspect

class Items:
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

	def index(self, name):
		index = -1
		for m in self.methods:
			index += 1
			if name == m.name:
				return index
		return index

class Item(wx.Window):
	"""Master class for all widgets"""

	def __init__(self, name, item, parent=None, *args, **kwargs):

		if parent:
			wx.Window.__init__(self, parent, -1)
		else:
			try:
				wx.Window.__init__(self, wx.Frame(None, -1), -1)
			except:
				self.app = wx.App(None)
				wx.Window.__init__(self, wx.Frame(None, -1), -1)

		self.sizer = wx.GridBagSizer()

		self.name = name
		self.item = item
		self.parent = parent
		
		#self.panel = wx.Panel(parent, -1)
		self.construct()
		#self.panel.SetSizerAndFit(self)

	def construct(self):
		self.items = []
		self.controls = {}

	def layout(self):
		r, c = layouts.LayoutGrid(self.sizer, self.items)
		return r, c

	def bind(self, event, function):
		self.Bind(event, function)

	def makeLabel(self, label):
		txt = wx.StaticText(self.parent, -1, label)
		self.items.append(txt)
		return txt

	def makeButton(self, label):
		btn = wx.Button(self.parent, -1, label)
		self.items.append(btn)
		self.addControl(btn)
		return btn

	def addControl(self, ctrl):
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
			btn = self.controls[str(ID)]
			label = btn.GetLabel()
			exec(events[label])

	def onTextCtrl(self, event):
		#not really sure how many fields we really want to pay attention to
		exec(events['textctrl'])

