import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as animation
import pandas as pd
import time
from sys import maxsize as int_max_value

class Display():

    def __init__(self):
        plt.ion()

        self.df = pd.DataFrame()
        self.y_min = int_max_value
        self.y_max = - int_max_value

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.lines, = self.ax.plot([],[], 'o')
        self.ax.set_xlim(0, 10)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(6))
        self.ax.yaxis.set_major_locator(plt.MaxNLocator(10))

        self.time = time.time()

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
            # ani = animation.FuncAnimation(self.fig, self.animate, interval=100)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    def set_boundary(self):
        for index in range(1, len(self.df.columns)):
            y_max = self.df[index].max()
            y_min = self.df[index].min()
            if y_max > self.y_max:
                self.y_max = y_max
            if y_min < self.y_min:
                self.y_min = y_min

    def animate(self, i):
        self.ax.clear()
        for index in range(1, len(self.df.columns)):
            key = list(mcolors.TABLEAU_COLORS)[index]
            color_choice = mcolors.TABLEAU_COLORS[key]
            self.ax.plot(self.df[0], self.df[index], color=color_choice)

    def update_draw_new(self):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(self.df[0])
        for index in range(1, len(self.df.columns)):
            key = list(mcolors.TABLEAU_COLORS)[index]
            color_choice = mcolors.TABLEAU_COLORS[key]
            self.lines.set_ydata(self.df[index], color=color_choice)

    def update_draw(self):
        self.ax.clear()
        self.ax.relim()
        for index in range(1, len(self.df.columns)):
            size_tableau_colors = len(list(mcolors.TABLEAU_COLORS))
            if index < size_tableau_colors:
                key = list(mcolors.TABLEAU_COLORS)[index]
                color_choice = mcolors.TABLEAU_COLORS[key]
            else:
                key = list(mcolors.BASE_COLORS)[index - size_tableau_colors]
                color_choice = mcolors.BASE_COLORS[key]

            self.ax.plot(self.df[0], self.df[index], color=color_choice)
