import wx
from classes import *

class autoUI:
	def __init__(self, target, parent = None):
		self.app = wx.App(False):

		frame = wx.Frame(None)
		if inspect.isclass(target):
			sizer = ClassItem(target, None)

		self.frame.SetSizerAndFit(sizer)
		frame.Show()

	def go(self):
		self.app.MainLoop()


def main():
	auto = autoUI()
	auto.go()

if __name__ == '__main__':
	main()
