# This is a sample Python script.
# import numpy as np
import os
import sys

import cv2

import time


JPEG2000_EXT = 'jp2'
JPEG_EXT = 'jpg'
WRITE_JPEG_QUALITY = 67

def convert(input_path, filename,output_path):
    """
    JPEG2000の画像ファイルをJPEGに変換する関数

    定数　JPEG2000_EXT、JPEG_EXT、WRITE_JPEG_QUALITY（圧縮率：自然数）が設定されている必要がある。

    :param input_path: ファイルのディレクトリ
    :type input_path: str
    :param filename: ファイル名
    :type filename: str
    :param output_path: 出力先
    :type output_path: str
    :return: なし
    """
    sp_name = filename.split('.')
    if sp_name[1] == JPEG2000_EXT:
        img = cv2.imread(input_path + '/' + filename)
        write_name = output_path + '/' + sp_name[0] + '.' + JPEG_EXT
        cv2.imwrite(write_name,img,[cv2.IMWRITE_JPEG_QUALITY, WRITE_JPEG_QUALITY])

def list_convert(input_path, output_path):
    list(map(lambda name: convert(input_path, name, output_path), os.listdir(input_path)))

if __name__ == '__main__':
    arguments = sys.argv

    if len(arguments) == 3:
        list_convert(arguments[1],arguments[2])
    else:
        print('Usage: python main.py InputDirectory OutputDirectory')
