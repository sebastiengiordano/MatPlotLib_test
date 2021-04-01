import wx
"""The icon's type is icon.ico"""
app = wx.App()
frame = wx.Frame(None, -1, title='2', pos=(0, 0), size=(200, 200))
frame.Show(True)
frame.SetIcon(wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO))
app.SetTopWindow(frame)
app.MainLoop()