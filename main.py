import funtions_1
from flask import Flask, request, render_template, redirect

import models

templates_img = '/templates/'
read_method = ["r", "w", "a"]
find_text = "/post/{{ id }}"
replace_text = "{{ url_for('templates',filename='post/{{ id }}') }}"
people_list = 'data/data.json'
data_json = 'data/comments.json'


# list_f, _ = funtions_1.find_files(templates_img)
# funtions_1.actual_ver_file(templates_img, read_method, list_f, find_text, replace_text)
user_data_json = funtions_1.person_data(people_list, read_method[0], "utf-8")
funtions_1.add_person_data_comm_from_file(user_data_json, data_json, read_method[0], "utf-8")

app = Flask(__name__)


@app.route('/')
def index_website():
    temp_dict = []
    for candidate in user_data_json:
        temp_dict.append({
            "id_p": int(candidate.id_p),
            "name": candidate.name,
            "picture": candidate.picture_url,
            "avatar": candidate.avatar,
            "content": candidate.content[:50] + "...",
            "views_count": candidate.views_count,
            "likes_count": candidate.likes_count,
            "count_comments": len(candidate.comment),
        })
    return render_template('index.html', list_person=temp_dict)


@app.route('/list/')
def list_p():
    list_person = user_data_json
    return render_template("list.html", list_person=list_person)


@app.route('/users/<username>')
def bookmarks_website(username):
    temp_search = []
    if username:
        username = username.lower()
        for user_n in user_data_json:
            if username in user_n.name:
                temp_search.append({
                    "id_p": int(user_n.id_p),
                    "avatar": user_n.avatar,
                    "name": user_n.name,
                    "picture": user_n.picture_url,
                    "content": user_n.content[:30] + "...",
                    "views_count": user_n.views_count,
                    "count_comments": len(user_n.comment),
                })
    return render_template("user-feed.html",
                           p_search=temp_search,
                           temp_search=temp_search,
                           list_person=temp_search)


# @app.route('/user-feed')
# def user_feed_website():
#     return render_template('user-feed.html')


@app.route('/search/')
def p_search():
    c_search = request.args.get("s")
    big_word = request.args.get("big_word")
    temp_search = []
    if c_search:
        if bool(big_word) is False:
            c_search = c_search.lower()
            for content in user_data_json:
                if c_search in content.content:
                    temp_search.append({
                        "id_p": int(content.id_p),
                        "name": content.name,
                        "picture": content.picture_url,
                        "content": content.content[:30] + "...",
                        "views_count": content.views_count,
                        "count_comments": len(content.comment),
                    })
                return render_template("search.html", count_search=len(temp_search),
                                       p_search=temp_search)
        for content in user_data_json:
            if c_search in content.content.lower():
                temp_search.append({
                    "id_p": int(content.id_p),
                    "name": content.name,
                    "picture": content.picture_url,
                    "content": content.content[:30] + "...",
                    "views_count": content.views_count,
                    "count_comments": len(content.comment),
                })
        count_search = len(temp_search)
    else:
        count_search = None

    return render_template("search.html", count_search=count_search,
                           p_search=temp_search)


@app.route('/post_p/<int:post_id>', methods=['GET', 'POST'])
def post_website(post_id):
    post_id_t = post_id - 1
    if request.method == 'POST':
        web_post = {"post_id": post_id_t + 1,
                    "commenter_name": request.form.get("web_name"),
                    "comment": request.form.get("web_content"),
                    "pk": models.User_web.get_score()+1}
        for u in user_data_json:
                if int(u.id_p) == int(web_post["post_id"]):
                    u.add_comment(web_post["commenter_name"], web_post["comment"], web_post["pk"])
        funtions_1.add_person_data_comm_from_web(web_post, data_json, read_method, "utf-8")

    if 0 < post_id <= len(user_data_json):

        data_user_name = user_data_json[post_id_t].name
        data_user_picture = user_data_json[post_id_t].picture_url
        data_user_avatar = user_data_json[post_id_t].avatar
        data_user_content = user_data_json[post_id_t].content
        data_user_views_count = user_data_json[post_id_t].views_count
        data_user_likes_count = user_data_json[post_id_t].likes_count
        data_user_comments = user_data_json[post_id_t].comment
        return render_template('/post.html',
                               data_user_name=data_user_name,
                               data_user_picture=data_user_picture,
                               data_user_avatar=data_user_avatar,
                               data_user_content=data_user_content,
                               data_user_views_count=data_user_views_count,
                               data_user_likes_count=data_user_likes_count,
                               post_id=post_id,
                               data_user_comments=data_user_comments,
                               count_comments=len(data_user_comments)
                               )

    return redirect("/404", code=302)


@app.errorhandler(404)
def not_found_error(errors):
    return render_template('404.html'), 404


app.run(debug=True)


