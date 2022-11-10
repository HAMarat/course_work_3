import json

POST_PATH = "static/data/posts.json"


def get_posts_all():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        all_posts = json.load(file)
        return all_posts


def get_posts_by_user(user_name):
    user_posts = []
    for post in get_posts_all():
        if post["poster_name"] == user_name:
            user_posts.append(post)
    return user_posts


def get_comments_by_post_id(post_id):
    for post in get_posts_all():
        if post["pk"] == post_id:
            return post["content"]
    return ValueError


def search_for_posts(query):
    posts_by_query = []
    for post in get_posts_all():
        if query in post["content"]:
            posts_by_query.append(post)
    return posts_by_query


def get_post_by_pk(pk):
    for post in get_posts_all():
        if post["pk"] == pk:
            return post["content"]
    return ValueError
