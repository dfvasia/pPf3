import os
from os.path import abspath, dirname
import json


def find_files(dir_find, type_file='.html'):
    files = os.listdir(dirname(abspath(__file__)) + dir_find)
    images = list(filter(lambda x: x.endswith(type_file), files))
    return images, str(dirname(abspath(__file__)) + '\\')


def open_file(files, mode, code, id_l=0):
    with open(files, mode, encoding=code) as file:
        if id_l == 0:
            return json.load(file)
        if id_l == 1:
            return file.read()
        if id_l == 2:
            file.write()
            print(files)



def actual_ver_file(templates_img, read_method, list_name):
    for f in list_name:
        old_file = open_file(templates_img[1:] + f, read_method[0], "utf-8", 1)
        new_file = old_file.replace('<img src="img', '<img src="/static/img')
        return new_file
