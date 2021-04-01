import wx

from .GUI.display_graph import DisplayGraph

def main():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, "./models/Log.csv")

    dg = DisplayGraph
    dg.set_scale(0, 7500)

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if (row[0]).isnumeric() :
                dg.received_data(x,y,z)


if __name__ == '__main__':
    main()
    