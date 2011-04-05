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
