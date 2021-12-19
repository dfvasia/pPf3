import funtions_1
from flask import Flask, request, render_template

templates_img = '/templates/'
read_method = ["r", "w", "a"]
find_text = '<img src="img'
replace_text = '<img src="/static/img'
people_list = 'data/data.json'

# list_f, _ = funtions_1.find_files(templates_img)
# funtions_1.actual_ver_file(templates_img, read_method, list_f, find_text, replace_text)
user_data_json = funtions_1.person_data(people_list, read_method[0], "utf-8")



app = Flask(__name__)


@app.route('/')
def index_website():
    temp_dict = []
    for candidate in user_data_json:
        temp_dict.append({
            "id": candidate.id_p,
            "name": candidate.name,
            "picture": candidate.picture_url,
            "avatar": candidate.avatar,
            "content": candidate.content[:50] + "...",
            "views_count": candidate.views_count,
            "likes_count": candidate.likes_count,
        })
    return render_template('index.html',list_person=temp_dict)


@app.route('/bookmarks.html')
def bookmarks_website():
    return render_template('/bookmarks.html')


@app.route('/user-feed.html')
def user_feed_website():
    return render_template('/user-feed.html')


@app.route('/post.html')
def post_website():
    return render_template('/post.html')


app.run(debug=True)



