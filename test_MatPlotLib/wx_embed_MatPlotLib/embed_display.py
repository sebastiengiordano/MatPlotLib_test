import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import (
    FigureCanvasWxAgg as FigureCanvas,
    NavigationToolbar2WxAgg as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.colors as mcolors

import pandas as pd

import wx
import wx.lib.mixins.inspection as WIT

from sys import maxsize as int_max_value
import time

import utils


class CanvasFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))
        plt.ioff()

        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.axes.set_xlim(0, 10)
        self.axes.xaxis.set_major_locator(plt.MaxNLocator(6))
        self.axes.yaxis.set_major_locator(plt.MaxNLocator(10))

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

        self.y_min = int_max_value
        self.y_max = - int_max_value

        self.time = time.time()

        # self.add_toolbar()  # comment this out for no toolbar


# alternatively you could use
#class App(wx.App):
class App(WIT.InspectableApp):
    def OnInit(self):
        """Create the main window and insert the custom frame."""
        self.Init()
        frame = CanvasFrame()
        frame.Show(True)

        return True

    def add(self, data):
        if (len(data) == len(self.df.columns)) or (len(self.df.columns) == 0):
            self.df = self.df.append([data.values])
        self.set_boundary()

    def display(self):
        time_now = time.time()
        if time_now - self.time > 0.1:
            self.time = time_now
            plt.ylim(self.y_min, self.y_max)
            self.update_draw()
            self.figure.canvas.draw()
            self.figure.canvas.flush_events()

    def update_draw(self):
        self.axes.clear()
        self.axes.relim()
        plt.ion()
        for index in range(1, len(self.df.columns)):
            size_tableau_colors = len(list(mcolors.TABLEAU_COLORS))
            if index < size_tableau_colors:
                key = list(mcolors.TABLEAU_COLORS)[index]
                color_choice = mcolors.TABLEAU_COLORS[key]
            else:
                key = list(mcolors.BASE_COLORS)[index - size_tableau_colors]
                color_choice = mcolors.BASE_COLORS[key]

            self.axes.plot(self.df[0], self.df[index], color=color_choice)
        plt.ioff()

    def set_boundary(self):
        for index in range(1, len(self.df.columns)):
            y_max = self.df[index].max()
            y_min = self.df[index].min()
            if y_max > self.y_max:
                self.y_max = y_max
            if y_min < self.y_min:
                self.y_min = y_min

    def add_toolbar(self):
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        # By adding toolbar in sizer, we are able to put it at the bottom
        # of the frame - so appearance is closer to GTK version.
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        # update the axes menu on the toolbar
        self.toolbar.update()


if __name__ == "__main__":
    df = utils.csv_to_DataFrame('C:\\Projets\\CNA\\test_MatPlotLib\\animation\\11_courbes.txt')
    df = df[:][1:].astype(float)
    
    graph = App()
    graph.add(df.iloc[0])
    graph.display()

    # graph.MainLoop()

    for line in range(1, df.shape[0]):
        graph.add(df.iloc[line])
        graph.display()
        # sleep(.05)
    print(df)
    sleep(10)
