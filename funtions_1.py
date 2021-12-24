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
        if id_l == 3 and new_file != 0:
            json.dump(new_file, file, ensure_ascii=False, indent=4)
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
            new_file = old_file.replace(find_text, replace_text)
            open_file(templates_img[1:] + f, read_method[1], "utf-8", 2, new_file)
        else:
            print('Файл был уже изменен.')
    return "Готово"


def person_data(file_name, mode, code):
    """


    :param file_name:
    :param mode: метод чтение файла
    :param code: кодировка файла
    :return:
    """
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


def add_person_data_comm_from_file(user_data, file_name, mode, code):
    """
    обработка коммен. из архива

    :param user_data: куда добавлять будем
    :param file_name: файл с комментариями архив
    :param mode: метод чтение файла
    :param code: кодировка файла
    :return: результат
    """
    json_p_comm = open_file(file_name, mode, code)
    for u in user_data:
        for m in json_p_comm:
            if u.id_p == m["post_id"]:
                u.add_comment(m["commenter_name"], m["comment"], m["pk"])


def add_person_data_comm_from_web(web_post, file_name, mode, code):
    """
    обработка коммен. из формы веб

    :param user_data: куда добавлять будем
    :param file_name: файл с комментариями архив
    :param mode: метод чтение файла
    :param code: кодировка файла
    :return: результат
    """
    json_p_comm_archive = open_file(file_name, mode[0], code)
    json_p_comm_archive.append(web_post)
    open_file(file_name, mode[1], code, 3, json_p_comm_archive)
    print(json_p_comm_archive)


    # def open_file(files, mode, code, id_l=0, new_file=0):
    # for u in user_web:
    #     for m in json_p_comm_archive:
    #         if u.id_p == m["post_id"]:
    #             u.add_comment(m["commenter_name"], m["comment"], m["pk"])
    return "add_person_data_comm_from_file отработала"

