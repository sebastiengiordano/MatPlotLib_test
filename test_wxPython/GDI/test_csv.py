import os
import csv

def main():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, "./models/Log.csv")
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print('\t'.join(row))


if __name__ == '__main__':
    main()
