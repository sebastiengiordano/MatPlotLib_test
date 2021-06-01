import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
from time import sleep, time

from convsens.plugin.display.display import Display
from convsens.plugin.display.display_data_manager import CNA_DisplayDataManager
from . import utils


def test_pyplot():
    df = utils.csv_to_DataFrame()
    df_x = df[0][1:].astype(int)
    df_y = df[1][1:].astype(int)
    df_z = df[3][1:].astype(int)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(df_x, df_y, color='tab:blue')
    ax.plot(df_x, df_z, color='tab:orange')

    if df_y[1:].min() < df_z[1:].min():
        y_min = df_y[1:].min()
    else:
        y_min = df_z[1:].min()

    if df_y[1:].max() > df_z[1:].max():
        y_max = df_y[1:].max()
    else:
        y_max = df_z[1:].max()

    border = int(y_max / 100)

    plt.ylim(y_min - border, y_max + border)
    ax.xaxis.set_major_locator(plt.MaxNLocator(6))
    ax.yaxis.set_major_locator(plt.MaxNLocator(10))

    plt.show()


def test_display():
    from . import utils
    from time import sleep
    import time
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
    # graph0 = Display([df_labels2])
    graph1 = Display([df_labels1, df_labels2])
    # graph2 = Display([df_labels1, df_labels2, df_labels3])
    # graph.display()

    for line in range(1, df1.shape[0]):
        data_1 = []
        data_2 = []
        data_3 = []
        for i in range(len(df_labels1)):
            data_1.append(df1.iloc[line].iloc[i])

        for i in range(len(df_labels2)):
            data_2.append(df2.iloc[line].iloc[i])

        for i in range(len(df_labels3)):
            data_3.append(df3.iloc[line].iloc[i])
        # print (pd.DataFrame(data_1))
        # print (pd.DataFrame(data_2))
        # print (pd.DataFrame(data_3))
        # graph0.add_data([pd.DataFrame(data_2)])
        graph1.add_data([pd.DataFrame(data_1), pd.DataFrame(data_2)])
        # graph2.add_data([pd.DataFrame(data_1), pd.DataFrame(data_2), pd.DataFrame(data_3)])
        # graph2.add_data([df1.iloc[line], df2.iloc[line], df3.iloc[line]])

        # graph0.display()
        graph1.display()
        # graph2.display()

        sleep(.01)

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


def EZ_display():
    g =Display([["x", "y"],["x","z"]])
    print(g.labels)
    for _ in range(10000):
        data_1 = pd.DataFrame([_, _**2])
        data_2 = pd.DataFrame([_, _**3])
        # print("\ndata_2:\n", data_2)
        # print("\ndata_2.iloc[1]:\n", data_2.iloc[1][0:1])
        g.add_data([data_1, data_2])


def test_display_data_manager():
    import cProfile
    import pstats


    with cProfile.Profile() as pr:
        test_display_data_manager_main()

    # pr.dump_stats('profilingDumpStats.txt')

    with open("package/test/test_MatPlotLib/data/Profile/profilingStatsAsText.txt", "w") as f:
        ps = pstats.Stats(pr, stream=f)
        ps.sort_stats('cumulative')
        ps.print_stats()


def test_display_data_manager_main():
    import os
    module_dir = os.path.dirname(__file__)
    file_dir1 = os.path.join(module_dir, "data/Temperatures.txt")
    file_dir2 = os.path.join(module_dir, "data/PhotoDiode_LED.txt")
    df1 = utils.csv_to_DataFrame(file_dir1)
    df2 = utils.csv_to_DataFrame(file_dir2)

    display_data_manager = CNA_DisplayDataManager()

    start_time = time()
    step_time = start_time

    for line in range(0, df1.shape[0]):
        elem = []
        for e in df1.iloc[line]:
            elem.append(e)
        display_data_manager.add_temperature(elem[0], elem[1], elem[2], elem[3], elem[4])
        if not line % 10:
            elem = []
            for e in df2.iloc[line]:
                elem.append(e)
            display_data_manager.add_power(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5])

        if not line % 1000:
            print(f"Temps après \t{line}\tlignes:\t{time() - step_time:.2f} s")
            step_time = time()
        
        # if time() - start_time > 3 * 60:
        #     break
        # sleep(0.010)


    end_add_data = time()
    print(f"Durée du test: {end_add_data-start_time:.2f} s")
    # sleep(100)


if __name__ == '__main__':
    # test_display()
    test_display_data_manager()
    # EZ_display()
