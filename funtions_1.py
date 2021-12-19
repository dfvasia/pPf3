import os
from os.path import abspath, dirname
import json
import models


def find_files(dir_find, type_file='.html'):
    """
    Поиск файлов в заданной папке и выводит только заданных типов файлов.
    :param dir_find: указание папки в каталоге проекта.
    :param type_file: указываем тип файла, по умолчанию .html
    :return: возвращает 2 аргумента список фалов и саму папку проекта
    """
    files = os.listdir(dirname(abspath(__file__)) + dir_find)
    images = list(filter(lambda x: x.endswith(type_file), files))
    return images, str(dirname(abspath(__file__)) + '\\')


def open_file(files, mode, code, id_l=0, new_file=0):
    """
    Открытие файла и выполнение заданных действий
    :param files:Имя файла
    :param mode: метод чтение файла
    :param code: кодировка файла
    :param id_l: метод обработки файла
    :param new_file: куда записывать изменение файла
    :return: вывод результата
    """
    with open(files, mode, encoding=code) as file:
        if id_l == 0:
            return json.load(file)
        if id_l == 1:
            return file.read()
        if id_l == 2 and new_file != 0:
            file.write(new_file)
            print(files)



def actual_ver_file(templates_img, read_method, list_name, find_text, replace_text):
    """
    Поиск в списке файлов и изм. их.
    :param templates_img: папка с файлами
    :param read_method: метод чтение файла
    :param list_name: список файлов для перебора
    :param find_text:  Поиск заданного текста (что будем искать)
    :param replace_text: Замена заданного текста (на что будем заменять)
    :return: вывод 'Готово'
    """
    for f in list_name:
        old_file = open_file(templates_img[1:] + f, read_method[0], "utf-8", 1)
        if replace_text not in old_file:
            new_file = old_file.replace( find_text, replace_text)
            open_file(templates_img[1:] + f, read_method[1], "utf-8", 2, new_file)
        else:
            print('Файл был уже изменен.')
    return "Готово"


def person_data(file_name, mode, code):

    person_list = []
    dict_p_data = open_file(file_name, mode, code)
    for k in dict_p_data:
        person_list.append(models.User_web(
            id_p=k["pk"],
            name=k["poster_name"],
            content=k["content"],
            avatar=k["poster_avatar"],
            picture_url=k["pic"],
            views_count=k["views_count"],
            likes_count=k["likes_count"],
        ))
    return person_list