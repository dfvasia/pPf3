import funtions_1
# from flask import Flask, request

templates_img = '/templates/'
read_method = ["r", "w", "a"]
find_text = '<img src="img'
replace_text = '<img src="/static/img'

list_f, _ = funtions_1.find_files(templates_img)
funtions_1.actual_ver_file(templates_img, read_method, list_f, find_text, replace_text)






