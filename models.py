class User_web:
    count_comments = 0

    def __init__(self, id_p, name, avatar, picture_url, content, views_count=0, likes_count=0):
        self.id_p = id_p
        self.name = name
        self.avatar = avatar
        self.content = content
        self.picture_url = picture_url
        self.views_count = views_count
        self.likes_count = likes_count
        self.comment = []

    def add_comment(self, a_n, a_c, a_d):
        User_web.count_comments += 1
        return self.comment.append({"commenter_name": a_n, "comment": a_c, "pk": a_d})

    @staticmethod
    def get_score():
        print("Всего постов", User_web.count_comments+1)
        return User_web.count_comments

    def __repr__(self):
        return f'{self.name}'

    def __len__(self):
        return len(self.id_p)



