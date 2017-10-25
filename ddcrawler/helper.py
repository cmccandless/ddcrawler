import os
import json


class WorkingDirectory:
    def __init__(self, dir):
        self.dir = dir
        if os.path.isfile(dir):
            self.dir = os.path.dirname(os.path.abspath(dir))
        self.cwd = os.getcwd()

    def __enter__(self):
        os.chdir(self.dir)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.cwd)


def import_presets(preset_type):
    preset_type = '.'.join(preset_type.split(os.path.sep)[-1].split('.')[:-1])
    with WorkingDirectory(__file__):
        with open('{}.json'.format(preset_type), 'r') as f:
            return json.load(f)
