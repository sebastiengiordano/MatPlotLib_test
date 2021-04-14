import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.widgets import CheckButtons
import pandas as pd
import time
from sys import maxsize as int_max_value


DISPLAY_DATA_LIMIT = 2000
STORED_DATA_LIMIT = 10000
DATA_TO_REMOVED = STORED_DATA_LIMIT - DISPLAY_DATA_LIMIT * 3

DISPLAY_REFRESH = 0.125 #0.125


class Display():

    def __init__(self):
        plt.ion()

        self.df = pd.DataFrame()
        self.y_min = int_max_value
        self.y_max = - int_max_value

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.fig.subplots_adjust(left=0.2)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(6))
        self.ax.yaxis.set_major_locator(plt.MaxNLocator(10))

        self.range_min = 0
        self.range_max = 0
        self.time = time.time()

        self.color_choice = []

    def set_labels(self, labels):
        self.labels = list(labels)
        self.df_size = len(labels)
        self._assign_color_init(self.df_size)
        self.visible = [True] * self.df_size
        self._add_check_box()

    def add_data(self, data):
        self.df = pd.concat([self.df, pd.DataFrame([data.values])], ignore_index=True)
        index_min = self.df.index[0]
        index_max = self.df.index[-1]
        if index_max - index_min > STORED_DATA_LIMIT:
            self.df = self.df.drop(range(index_min, index_min + DATA_TO_REMOVED))

    def display(self):
        time_now = time.time()
        if time_now - self.time > DISPLAY_REFRESH:
            self.time = time_now
            self.update_draw()
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    def set_boundary(self):
        # Reinit y-axis
        self.y_min = int_max_value
        self.y_max = - int_max_value

        # Limitation of amount of data to plot
        r_min = self.range_min = self.df.index[0]
        r_max = self.range_max = self.df.index[-1]
        if r_max - r_min > DISPLAY_DATA_LIMIT:
            self.range_min = r_max - DISPLAY_DATA_LIMIT

    def update_draw(self):
        self.set_boundary()
        r_min = self.range_min
        r_max = self.range_max
        self.ax.clear()
        # self.ax.ignore_existing_data_limits = True
        # self.ax.update_datalim(((self.df[0][r_min], self.y_min),(self.df[0][r_max], self.y_max)))
        # self.ax.autoscale()
        # self.ax.set_xlim((r_min, r_max))
        # self.ax.set_ylim((self.y_min, self.y_max))
        # self.ax.relim()

        for index in range(1, self.df_size):
            if self.visible[index]:
                self.ax.plot(
                    self.df[0][r_min:r_max],
                    self.df[index][r_min:r_max],
                    color=self.color_choice[index]
                    )

    def _add_check_box(self):
        CheckButton = plt.axes([0.01, 0.01, 0.1, 0.9])
        self.chxbox = CheckButtons(CheckButton, self.labels[1:], self.visible)

        [rec.set_facecolor(self.color_choice[i+1]) for i, rec in enumerate(self.chxbox.rectangles)]
        [rec.set_width(0.8) for rec in self.chxbox.rectangles]
        [(line1.set_linewidth(1.1), line2.set_linewidth(1.1)) for (line1, line2) in self.chxbox.lines]
        for line1, line2 in self.chxbox.lines:
            # Change width of the cross
            ((x0, y0), (x1, y1)) = line1.get_xydata()
            line1.set_data([x0+0.006, x1+0.05],[y0-0.001, y1-0.001])
            ((x0, y0), (x1, y1)) = line2.get_xydata()
            line2.set_data([x0+0.006, x1+0.05],[y0-0.001, y1-0.001])

        self.chxbox.on_clicked(self._set_visible)

    def _set_visible(self, label):
        index = self.labels.index(label)
        self.visible[index] = not self.visible[index]
        if self.visible[index]:
            self.chxbox.rectangles[index-1].set_facecolor(self.color_choice[index])
        else:
            self.chxbox.rectangles[index-1].set_facecolor('white')

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
    import os
    module_dir = os.path.dirname(__file__)
    file_dir = os.path.join(module_dir, "data/11_courbes.txt")
    df = utils.csv_to_DataFrame(file_dir)
    df_labels = list(df.iloc[0])
    df = df[1:].astype(float)

    start_time = time.time()
    step_time = start_time
    graph = Display()
    graph.set_labels(df_labels)
    graph.display()

    for line in range(1, df.shape[0]):
        graph.add_data(df.iloc[line])
        graph.display()
        # sleep(.01)
        # if not line % 1000:
        #     print("\tY-Range", graph.y_min, graph.y_max)
        #     print(f"Temps après \t{line}\tlignes:\t{time.time() - step_time:.2f} s")
        #     step_time = time.time()
    end_add_data = time.time()
    print(f"Durée du test: {end_add_data-start_time:.2f} s")
    # print(f"Durée ajout data: {end_add_data-start_time:.2f} s")
    # graph.display()
    # print(f"Temps affichage: {time.time()-end_add_data:.2f} s")
    # print(graph.df)
    sleep(10)
