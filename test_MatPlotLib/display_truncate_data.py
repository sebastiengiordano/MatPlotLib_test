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
        self.labels = ""
        self.y_min = int_max_value
        self.y_max = - int_max_value

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        # self.lines, = self.ax.plot([],[], 'o')
        self.fig.subplots_adjust(left=0.2)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(6))
        self.ax.yaxis.set_major_locator(plt.MaxNLocator(10))

        self.limit_data = 500
        self.range_min = 0
        self.range_max = 0
        self.time = time.time()
        self.df_size = 0

        self.color_choice = []

    def set_labels(self, labels):
        # print('\nlabels: ', labels)
        # self.df = pd.DataFrame(columns=labels)
        # print('\ndf: ', self.df)
        self.labels = labels
        self.df_size = len(self.df.columns)
        self._assign_color_init(self.df_size)
        self.visible = [True] * self.df_size
        self._add_check_box()

    def add_data(self, data):
        if (len(data) == self.df_size) or (self.df_size == 0):
            self.df = self.df.append([data.values], ignore_index=True)

        # Limitation of amount of data saved
        len_data = self.df.count()[0]
        if len_data > self.limit_data * 2:
            self.df = self.df[self.limit_data:]
        self.set_boundary()

    def display(self):
        time_now = time.time()
        if time_now - self.time > 0.115:
            self.time = time_now
            plt.ylim(self.y_min, self.y_max)
            self.update_draw()
            # ani = animation.FuncAnimation(self.fig, self.animate, interval=100)
            self.fig.canvas.draw()
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
        r_min = self.range_min
        r_max = self.range_max
        for index in range(1, self.df_size):
            y_max = self.df[index][r_min:r_max].max()
            y_min = self.df[index][r_min:r_max].min()
            if y_max > self.y_max:
                self.y_max = y_max
            if y_min < self.y_min:
                self.y_min = y_min

    def update_draw(self):
        r_min = self.range_min
        r_max = self.range_max
        # x_label = self.df.columns[0]
        # print('\nx_label: ', x_label)
        # print('type(x_label): ', type(x_label))
        # print('df.columns: ', self.df.columns)
        # print('df: ', self.df)
        print('self.range_max: ', self.range_max, '\ttype(self.range_max): ', type(self.range_max))
        x_min = self.df[0].loc[0]
        x_max = self.df[0].loc[self.range_max]
        self.ax.clear()
        self.ax.ignore_existing_data_limits = True
        self.ax.update_datalim(((x_min, self.y_min),(x_max, self.y_max)))
        self.ax.autoscale_view()
        # self.ax.set_xlim((r_min, r_max))
        # self.ax.set_ylim((self.y_min, self.y_max))
        # self.ax.relim()

        for index in range(1, self.df_size):
            self.ax.plot(
                self.df[0][r_min:r_max],
                self.df[index][r_min:r_max],
                color=self.color_choice[index],
                visible=self.visible[index]
                )

    def _add_check_box(self):
        CheckButton = plt.axes([0.01, 0.01, 0.1, 0.9])
        # CheckButton = plt.axes([0.05, 0.4, 0.1, 0.15])
        self.chxbox = CheckButtons(CheckButton, self.labels[1:], self.visible)
        [rec.set_facecolor(self.color_choice[i+1]) for i, rec in enumerate(self.chxbox.rectangles)] 
        self.chxbox.on_clicked(self._set_visible)

    def _set_visible(self, label):
        index = list(self.df.columns).index(label)
        self.visible[index] = not self.visible[index]

    def _assign_color_init(self, curves_number):
        for index in range(curves_number):
            size_tableau_colors = len(list(mcolors.TABLEAU_COLORS))
            if index < size_tableau_colors:
                key = list(mcolors.TABLEAU_COLORS)[index]
                self.color_choice.append(mcolors.TABLEAU_COLORS[key])
            else:
                key = list(mcolors.BASE_COLORS)[index - size_tableau_colors]
                self.color_choice.append(mcolors.BASE_COLORS[key])


if __name__ == '__main__':
    import utils
    from time import sleep
    df = utils.csv_to_DataFrame('C:\\Projets\\CNA\\MatPlotLib_test\\test_MatPlotLib\\animation\\6_courbes.txt')
    df_labels = list(df.iloc[0])
    df = df[1:].astype(float)
    
    graph = Display()
    graph.set_labels(df_labels)
    graph.display()

    for line in range(1, df.shape[0]):
        graph.add_data(df.iloc[line])
        graph.display()
        # sleep(.01)
    sleep(10)
