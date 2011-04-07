class NestedObj:
	def __init__(self, a, b=2, c=3):
		self.a = a
		self.b = b
		self.c = c

	def __str__(self):
		return "%s %s %s" % (self.a, self.b, self.c)

class TestObj:
	def __init__(self, items, number = 1.23, chong={'wee' : 'nis', 'pen' : 15}, a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, testobj=NestedObj, testobj2=NestedObj):
		self.items = items
		self.number = number
		self.chong = chong
		self.testobj = testobj
		self.testobj2 = testobj2

	def testFunc(self, testarg=False):
		print testarg
		print self.testobj
		print self.items


	def testFunc2(self, testarg=True):
		print testarg
		print self.testobj2

	def __privateFunc(self, privateArg = 6):
		pass

