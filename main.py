import funtions_1
# from flask import Flask, request

templates_img = '/templates/'
read_method = ["r", "w", "a"]

list_f, dir_o = funtions_1.find_files(templates_img)


for f in list_f:
     old_file = funtions_1.open_file(templates_img[1:] + f, read_method[0], "utf-8", 1)
     new_file = old_file.replace('<img src="img', '<img src="/static/img')





