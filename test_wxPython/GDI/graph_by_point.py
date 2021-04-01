#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This program draws various shapes on
the window.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

import wx
import os
import csv

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle('Graph by lines')
        self.Center()

    def OnPaint(self, e):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, "./models/Log.csv")
        w, h = self.GetSize()
        w_max, h_max = 0, 0

        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen('RED'))
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if (row[0]).isnumeric():
                    x, y, z = int(row[0]), int(row[1]), int(row[5])
                    if x > w_max:
                        w_max = x
                    if y > h_max:
                        h_max = y
                    if z > h_max:
                        h_max = z

        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if (row[0]).isnumeric():
                    x, y, z = int(int(row[0])/w_max*w), int(int(row[1])/h_max*h), int(int(row[5])/h_max*h)
                    dc.DrawPoint(x, y)
                    dc.DrawPoint(x, z)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
