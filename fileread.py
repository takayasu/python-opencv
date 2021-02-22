
import os
import sys

import numpy as np

JPEG2000_EXT = 'jp2'

def convert(input_path, filename):
    sp_name = filename.split('.')
    if sp_name[1] == JPEG2000_EXT:
        with open(input_path + '/' + filename,mode='rb') as fop:
            data = np.fromfile(fop,np.float64,-1)
            print(len(data))

def list_convert(input_path):
    list(map(lambda name: convert(input_path, name), os.listdir(input_path)))

if __name__ == '__main__':
    arguments = sys.argv

    if len(arguments) == 2:
        list_convert(arguments[1])