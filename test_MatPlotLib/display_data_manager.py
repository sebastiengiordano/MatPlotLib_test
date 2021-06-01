import pandas as pd
from . import display

class DisplayDataManager():

    def __init__(self, labels):
        self.frame_number = frame_number = len(labels)
        frame_index = []
        for i in range(frame_number):
            frame_index.append([])
            frame_index[i] = [None] * len(labels[i])

        self.df = [pd.DataFrame([frame_index[i]]) for i in range(frame_number)]
        print(self.df)
        print(self.df[0])
        self.labels = [0] * frame_number
        self.df_size = [0] * frame_number

        self._set_labels(labels)

    def add_data(self, abscise, labels, data):
        if not isinstance(labels[0], list):
            labels = [labels]
        if not isinstance(data[0], list):
            data = [data]
        # df = [pd.DataFrame()] * self.frame_number
        # preview_update = self.df[0][0][df[0].index[-1]]
        # Is the last data has the same timestamp
        # if not (preview_update == abscise or (abscise - preview_update) < 0.001):
        #     for i in range(self.frame_number):
                # if self.labels[i]
        
        
        for i in range(self.frame_number):
            self.df[i][0][0] = 
            for label_index, label in enumerate(labels[i]):
                if label in self.labels[i]:
                    curve_index = self.labels[i].index(label)
                    self.df[i][curve_index][0] = data[i][label_index]

            self.df[i] = pd.concat([self.df[i], pd.DataFrame([data[i].values])], ignore_index=True)
            index_min = self.df[i].index[0]
            index_max = self.df[i].index[-1]
            if index_max - index_min > STORED_DATA_LIMIT:
                self.df[i] = self.df[i].drop(range(index_min, index_min + DATA_TO_REMOVED))

    def _set_labels(self, labels):
        for i in range(self.frame_number):
            self.labels[i] = list(labels[i])
            self.df_size[i] = len(labels[i])


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

    display_data_manager = DisplayDataManager([df_labels1, df_labels2, df_labels3])

    # start_time = time.time()
    # step_time = start_time
    # graph0 = Display([df_labels2])
    # graph1 = Display([df_labels1, df_labels2])
    # graph2 = Display([df_labels1, df_labels2, df_labels3])
    # graph.display()

    for line in range(1, df1.shape[0]):
        pass
        # graph0.add_data([df2.iloc[line]])
        # graph1.add_data([df1.iloc[line], df2.iloc[line]])
        # graph2.add_data([df1.iloc[line], df2.iloc[line], df3.iloc[line]])

        # graph0.display()
        # graph1.display()
        # graph2.display()

        # sleep(.01)

        # if not line % 1000:
            # print(graph.df)
            # print("\tY-Range", graph.y_min, graph.y_max)
            # print(f"Temps après \t{line}\tlignes:\t{time.time() - step_time:.2f} s")
            # step_time = time.time()

    end_add_data = time.time()
    print(f"Durée du test: {end_add_data-start_time:.2f} s")
    # print(f"Durée ajout data: {end_add_data-start_time:.2f} s")
    # graph0.display()
    # graph1.display()
    # print(f"Temps affichage: {time.time()-end_add_data:.2f} s")
    # print(graph0.df)
    # print(graph1.df)
    # print(graph2.df)
    sleep(100)
