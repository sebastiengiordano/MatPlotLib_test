import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
from time import sleep
import display
import utils


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

def main():
    # test_pyplot()
    # df = utils.csv_to_DataFrame()
    df = utils.csv_to_DataFrame('C:\\Projets\\CNA\\test_MatPlotLib\\animation\\11_courbes.txt')
    df = df[:][1:].astype(float)
    
    graph = display.Display()
    graph.add(df.iloc[0])
    graph.display()

    for line in range(1, df.shape[0]):
        graph.add(df.iloc[line])
        graph.display()
        # sleep(.05)
    print(df)
    sleep(10)

if __name__ == '__main__':
    main()
