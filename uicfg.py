#uicfg.py

constructors = {}
constructors['str'] = ["wx.TextCtrl(self, -1, %s)"]
constructors['int'] = ["wx.SpinCtrl(self, -1, str(%s))"]
constructors['float'] = ["wx.FloatCtrl(self, -1, %s)"]
constructors['list'] = ["ListItems(self, %s)"]
constructors['bool'] = ["wx.Checkbox(self, -1).SetValue(%s)" ]
constructors['dict'] = ["DictItems(self, %s)"]

constructors['NoneType'] = ["wx.TextCtrl(self.parent, -1)", 
							"wx.Button(self.parent, -1, 'Set Type').Disable()", 
							"wx.Button(self.parent, -1, 'Run').Disable()"]

constructors['instance'] = ["ClassItems(%s)"] 

readers = {}
readers['str'] = "items[0].GetValue()"
readers['int'] = "int(items[0].GetValue())"
readers['float'] = "items[0].GetFloat()"
readers['list'] = "ReadList(items)"
readers['bool'] = "items[0].GetValue()"
readers['dict'] = "ReadDict(items)"
readers['NoneType'] = "ReadCode(items[0])"
readers['instance'] = "ReadClassItems(items[0], items[1])"

events = {}
events['Initialize'] = "self.run()"
events['Return'] = "self.rtrn()"
events['Class Edit'] = "self.edit()"
events['Eval'] = ""
events['Exec'] = ""
events['ListEdit'] = ""
events['DictEdit'] = ""
