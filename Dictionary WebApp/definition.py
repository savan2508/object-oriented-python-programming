import os
import sys

import pandas


def resource_path(relative_path):
    """ Get an absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEI PASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv(resource_path("data.csv"))
        return tuple(df.loc[df['word'] == self.term]['definition'])
