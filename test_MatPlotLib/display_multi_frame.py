import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.widgets import CheckButtons
import pandas as pd
import time
from sys import maxsize as int_max_value


DISPLAY_DATA_LIMIT = 3000
STORED_DATA_LIMIT = 10000
DATA_TO_REMOVED = STORED_DATA_LIMIT - (2 * DISPLAY_DATA_LIMIT)

DISPLAY_REFRESH = 0.5 #0.125
# DISPLAY_DATA_LIMIT = 2000000


class Display():

    def __init__(self, labels):
        plt.ion()

        self.frame_number = frame_number = len(labels) 
        self.df = [pd.DataFrame() for _ in range(frame_number)]
        self.y_min = [int_max_value for _ in range(frame_number)]
        self.y_max = [- int_max_value for _ in range(frame_number)]
        self.range_min = [0 for _ in range(frame_number)]
        self.range_max = [0 for _ in range(frame_number)]
        self.visible = [[] for _ in range(frame_number)]
        self.color_choice = [[] for _ in range(frame_number)]
        self.chxbox = [0 for _ in range(frame_number)]
        self.df_size = [0 for _ in range(frame_number)]
        self.labels = [0 for _ in range(frame_number)]

        self.fig = plt.figure()
        self.ax = [
            self.fig.add_subplot(frame_number, 1, i)
            for i in range(1, frame_number + 1)]

        self.fig.subplots_adjust(left=0.2, right=0.98, bottom=0.05, top=0.95, hspace=0.16)

        for i in range(frame_number):
            self.ax[i].xaxis.set_major_locator(plt.MaxNLocator(6))
            self.ax[i].yaxis.set_major_locator(plt.MaxNLocator(10))
        self._set_labels(labels)

        self.time = time.time()

    def _set_labels(self, labels):
        for i in range(self.frame_number):
            self.labels[i] = list(labels[i])
            self.df_size[i] = len(labels[i])
            self._assign_color_init(i, self.df_size[i])
            self.visible[i] = [True] * self.df_size[i]
        self._add_check_box()

    def add_data(self, data):
        for i in range(self.frame_number):
            self.df[i] = pd.concat([self.df[i], pd.DataFrame([data[i].values])], ignore_index=True)
            index_min = self.df[i].index[0]
            index_max = self.df[i].index[-1]
            if index_max - index_min > STORED_DATA_LIMIT:
                self.df[i] = self.df[i].drop(range(index_min, index_min + DATA_TO_REMOVED))

    def display(self):
        time_now = time.time()
        if time_now - self.time > DISPLAY_REFRESH:
            self.time = time_now
            self.update_draw()
            self.fig.canvas.draw_idle()
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    def set_boundary(self):
        for i in range(self.frame_number):
            # Reinit y-axis
            self.y_min[i] = int_max_value
            self.y_max[i] = - int_max_value

            # Limitation of amount of data to plot
            r_min = self.range_min[i] = self.df[i].index[0]
            r_max = self.range_max[i] = self.df[i].index[-1]
            if r_max - r_min > DISPLAY_DATA_LIMIT:
                self.range_min[i] = r_max - DISPLAY_DATA_LIMIT

    def update_draw(self):
        self.set_boundary()
        for i in range(self.frame_number):
            r_min = self.range_min[i]
            r_max = self.range_max[i]
            self.ax[i].clear()

            for index in range(1, self.df_size[i]):
                if self.visible[i][index]:
                    self.ax[i].plot(
                        self.df[i][0][r_min:r_max],
                        self.df[i][index][r_min:r_max],
                        color=self.color_choice[i][index]
                        )

    def _add_check_box(self):
        for i in range(self.frame_number):
            frame_height = 0.95 / self.frame_number
            # [left, bottom, width, height].
            CheckButton = plt.axes([0.01, (0.02 + ((frame_height + 0.02) * (self.frame_number - i - 1))), 0.1, frame_height])
            self.chxbox[i] = CheckButtons(CheckButton, self.labels[i][1:], self.visible[i])

            [rec.set_facecolor(self.color_choice[i][j+1]) for j, rec in enumerate(self.chxbox[i].rectangles)]
            [rec.set_width(0.8) for rec in self.chxbox[i].rectangles]
            [(line1.set_linewidth(1.1), line2.set_linewidth(1.1)) for (line1, line2) in self.chxbox[i].lines]
            for line1, line2 in self.chxbox[i].lines:
                # Change width of the cross
                ((x0, y0), (x1, y1)) = line1.get_xydata()
                line1.set_data([x0+0.006, x1+0.05],[y0-0.001, y1-0.001])
                ((x0, y0), (x1, y1)) = line2.get_xydata()
                line2.set_data([x0+0.006, x1+0.05],[y0-0.001, y1-0.001])

            self.chxbox[i].on_clicked(self._set_visible)

    def _set_visible(self, label):
        for i, labels in enumerate(self.labels):
            if label in labels:
                index = labels.index(label)
                self.visible[i][index] = not self.visible[i][index]
                if self.visible[i][index]:
                    self.chxbox[i].rectangles[index-1].set_facecolor(self.color_choice[i][index])
                else:
                    self.chxbox[i].rectangles[index-1].set_facecolor('white')

    def _assign_color_init(self, graph_number, curves_number):
        for index in range(curves_number):
            size_tableau_colors = len(list(mcolors.TABLEAU_COLORS))
            if index < size_tableau_colors:
                key = list(mcolors.TABLEAU_COLORS)[index]
                self.color_choice[graph_number].append(mcolors.TABLEAU_COLORS[key])
            else:
                key = list(mcolors.BASE_COLORS)[index - size_tableau_colors]
                self.color_choice[graph_number].append(mcolors.BASE_COLORS[key])


if __name__ == '__main__':
    import utils
    from time import sleep
    import os
    module_dir = os.path.dirname(__file__)
    file_dir1 = os.path.join(module_dir, "data/11_courbes.txt")
    file_dir2 = os.path.join(module_dir, "data/6_courbes.txt")
    df1 = utils.csv_to_DataFrame(file_dir1)
    df_labels1 = list(df1.iloc[0])
    df1 = df1[1:].astype(float)
    df2 = utils.csv_to_DataFrame(file_dir2)
    df_labels2 = list(df2.iloc[0])
    df2 = df2[1:].astype(float)
    df3 = utils.csv_to_DataFrame(file_dir2)
    df_labels3 = list(df3.iloc[0])
    df3 = df3[1:].astype(float)

    for i, (label1, label2, label3) in enumerate(zip(df_labels1, df_labels2, df_labels3)):
        df_labels1[i] = "1__" + label1
        df_labels2[i] = "2__" + label2
        df_labels3[i] = "3__" + label3

    start_time = time.time()
    step_time = start_time
    graph0 = Display([df_labels2])
    graph1 = Display([df_labels1, df_labels2])
    # graph2 = Display([df_labels1, df_labels2, df_labels3])
    # graph.display()

    for line in range(1, df1.shape[0]):
        graph0.add_data([df2.iloc[line]])
        graph1.add_data([df1.iloc[line], df2.iloc[line]])
        # graph2.add_data([df1.iloc[line], df2.iloc[line], df3.iloc[line]])

        graph0.display()
        graph1.display()
        # graph2.display()

        # sleep(.01)

        if not line % 1000:
            # print(graph.df)
            # print("\tY-Range", graph.y_min, graph.y_max)
            print(f"Temps après \t{line}\tlignes:\t{time.time() - step_time:.2f} s")
            step_time = time.time()

    end_add_data = time.time()
    print(f"Durée du test: {end_add_data-start_time:.2f} s")
    print(f"Durée ajout data: {end_add_data-start_time:.2f} s")
    # graph0.display()
    # graph1.display()
    print(f"Temps affichage: {time.time()-end_add_data:.2f} s")
    # print(graph0.df)
    # print(graph1.df)
    # print(graph2.df)
    sleep(100)
