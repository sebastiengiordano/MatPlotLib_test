import os
import pandas as pd


def csv_to_DataFrame(file_path=None, delimiter=','):
    if not file_path:
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        file_path = os.path.join(fileDir, "../test_wxPython/models/Log.csv")
    return pd.read_csv(file_path, sep=delimiter, header=None)
