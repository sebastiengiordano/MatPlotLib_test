import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.widgets import CheckButtons
import pandas as pd
import time
from sys import maxsize as int_max_value

class Display():

    def __init__(self):
        plt.ion()

        self.df = pd.DataFrame()
        self.y_min = int_max_value
        self.y_max = - int_max_value

        self.fig = plt.figure(figsize=(4,1.5))
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.lines, = self.ax.plot([],[], 'o')
        self.ax.set_xlim(0, 10)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(6))
        self.ax.yaxis.set_major_locator(plt.MaxNLocator(10))

        self.limit_data = 1500
        self.range_min = 0
        self.range_max = 0
        self.time = time.time()

    def set_labels(self, labels):
        self.df.columns = labels

    def add_data(self, data):
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
            self.fig.canvas.draw_idle()
            self.fig.canvas.flush_events()

    def set_boundary(self):
        # Reinit y-axis
        self.y_min = int_max_value
        self.y_max = - int_max_value

        # Limitation of amount of data to plot
        len_data = self.df.count()[0]
        if len_data > self.limit_data:
            self.range_min = len_data - self.limit_data
            self.range_max = len_data
        else:
            self.range_min = 1
            self.range_max = len_data

        # y-axis range research
        for index in range(1, len(self.df.columns)):
            r_min = self.range_min
            r_max = self.range_max
            y_max = self.df[index][r_min:r_max].max()
            y_min = self.df[index][r_min:r_max].min()
            if y_max > self.y_max:
                self.y_max = y_max
            if y_min < self.y_min:
                self.y_min = y_min

    def update_draw(self):
        r_min = self.range_min
        r_max = self.range_max
        self.ax.clear()
        self.ax.ignore_existing_data_limits = True
        self.ax.update_datalim(((r_min, self.y_min),(r_max, self.y_max)))
        self.ax.autoscale_view()
        # self.ax.set_xlim((r_min, r_max))
        # self.ax.set_ylim((self.y_min, self.y_max))
        # self.ax.relim()

        for index in range(1, len(self.df.columns)):
            size_tableau_colors = len(list(mcolors.TABLEAU_COLORS))
            if index < size_tableau_colors:
                key = list(mcolors.TABLEAU_COLORS)[index]
                color_choice = mcolors.TABLEAU_COLORS[key]
            else:
                key = list(mcolors.BASE_COLORS)[index - size_tableau_colors]
                color_choice = mcolors.BASE_COLORS[key]

            self.ax.plot(self.df[0][r_min:r_max], self.df[index][r_min:r_max], color=color_choice)
