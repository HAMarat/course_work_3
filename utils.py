import json

POST_PATH = "static/data/posts.json"
COMMENTS_PATH = "static/data/comments.json"
BOOKMARKS_PATH = "static/data/bookmarks.json"


def get_json_data(path: str) -> list[dict]:
    """
    Функция для загрузки постов из json файла
    """
    with open(path, 'r', encoding='utf-8') as file:
        all_data = json.load(file)
        return all_data


def write_json_data(path: str, data) -> None:
    """
    Функция для загрузки постов из json файла
    """
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_posts_by_user(user_name: str) -> list[dict]:
    """
    Функция для поиска постов по автору
    """
    user_posts = []
    for post in get_json_data(POST_PATH):
        if post["poster_name"] == user_name:
            user_posts.append(post)
    return user_posts


def get_comments_by_post_id(post_id: int) -> list[dict]:
    """
    Функция для поиска комментариев по id поста
    """
    comments = []
    for comment in get_json_data(COMMENTS_PATH):
        if comment["post_id"] == post_id:
            comments.append(comment)
            post_found = True
    return comments
    # return ValueError


def search_for_posts(query: str) -> list[dict]:
    """
    Функция для поиска пост по запросу
    """
    posts_by_query = []
    for post in get_json_data(POST_PATH):
        if query.lower() in post["content"].lower() and len(posts_by_query) < 10:
            posts_by_query.append(post)
    return posts_by_query


def get_post_by_post_id(pk: int) -> dict:
    """
    Функция для получения контента поста по его pk
    """
    for post in get_json_data(POST_PATH):
        if post["pk"] == pk:
            return post


def get_end_word(count: int) -> str:
    """
    Функция для выведения слова с правильным окончанием
    """
    ends = ['комментариев', 'комментарий', 'комментария']
    i = 2
    if count % 10 == 0 or 10 <= count % 100 <= 20:
        i = 0
    elif count % 10 == 1:
        i = 1
    return ends[i]
