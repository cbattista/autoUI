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
values['str'] = "items[0].GetValue()"
values['int'] = "int(items[0].GetValue())"
values['float'] = "items[0].GetFloat()"
values['list'] = "ReadList(items)"
values['bool'] = "items[0].GetValue()"
values['dict'] = "ReadDict(items)"
values['NoneType'] = "ReadCode(items[0])"
values['instance'] = "ReadClassItems(items[0], items[1])"

events['Initialize'] = "self.run()"
events['Return'] = "self.rtrn()"
events['Edit'] = ""
events['Eval'] = ""
events['Exec'] = ""
events['ListEdit'] = ""
events['DictEdit'] = ""
