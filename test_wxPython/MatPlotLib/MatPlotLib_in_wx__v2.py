import wx
from matplotlib.figure import Figure as Fig
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar

from collections import deque
#import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mlp
import numpy as np
import random

# Class that inherits wx.Panel. The purpose is to embed it into
# a wxPython App. That part can be seen in main()
class Serial_Plot(wx.Panel):
    def __init__(self, parent, strPort, id=-1, dpi=None, **kwargs):
        super().__init__(parent, id=id, **kwargs)
        self.figure  = plt.figure(figsize=(20,20))
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 50))
        self.plot_data, = self.ax.plot([], [])
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
#
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
#