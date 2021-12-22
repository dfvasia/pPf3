import funtions_1
from flask import Flask, request, render_template, redirect

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


@app.route('/bookmarks')
def bookmarks_website():
    return render_template('/bookmarks.html')


@app.route('/user-feed')
def user_feed_website():
    return render_template('/user-feed.html')


@app.route('/search/')
def p_search():
    p_search = request.args.get("s")
    list_person = person_data_user
    temp_search = {}
    if p_search:
        if settings_app["case-sensitive"] is False:
            p_s = p_search.lower()
            for person in list_person:
                if p_s in person.name.lower():
                    temp_search[person.id_p] = person.name
        else:
            for person in list_person:
                if p_search in person.name:
                    temp_search[person.id_p] = person.name

    return render_template("search.html", p_search=temp_search, temp_search=temp_search)


@app.route('/post_p/<int:post_id>')
def post_website(post_id):
    if 0 < post_id <= len(user_data_json):
        for user_data in user_data_json:
            post_id_t = post_id - 1
            print(post_id, '---', user_data.id_p, '---', len(user_data_json))
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
    return redirect("http://127.0.0.1:5000/404", code=302)


@app.errorhandler(404)
def not_found_error(errors):
    return render_template('404.html'), 404


app.run(debug=True)
