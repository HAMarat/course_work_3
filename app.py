from flask import Flask, render_template, request, redirect
from utils import get_json_data, get_post_by_post_id, get_posts_by_user, write_json_data, \
    get_comments_by_post_id, search_for_posts, get_end_word, POST_PATH, BOOKMARKS_PATH
from api_request.api_request import api_request

app = Flask(__name__)

# регистрируем Blueprint для работы с API
app.register_blueprint(api_request, url_prefix='/api')


@app.route('/')
def main_page():
    """
    Представление показывающее все посты
    """
    posts = get_json_data(POST_PATH)
    bookmarks_posts = get_json_data(BOOKMARKS_PATH)
    return render_template('index.html', posts=posts, bookmarks_posts=bookmarks_posts)


@app.route('/posts/<int:post_id>')
def post_by_post_id(post_id):
    """
    Представление показывающее пост по pk
    """
    post = get_post_by_post_id(post_id)
    comments = get_comments_by_post_id(post_id)
    end_word_comment = get_end_word(len(comments))
    bookmarks_posts = get_json_data(BOOKMARKS_PATH)
    return render_template('post.html', post=post, comments=comments,
                           end_word_comment=end_word_comment, bookmarks_posts=bookmarks_posts)


@app.route('/search', methods=['GET'])
def search():
    """
    Представление обрабатывающее поиск постов
    """
    query = request.args['s']
    found_posts = search_for_posts(query)
    bookmarks_posts = get_json_data(BOOKMARKS_PATH)
    return render_template('search.html', found_posts=found_posts, bookmarks_posts=bookmarks_posts)


@app.route('/users/<username>')
def get_user_posts(username):
    """
    Представление показывающее посты выбранного пользователя
    """
    user_posts = get_posts_by_user(username)
    bookmarks_posts = get_json_data(BOOKMARKS_PATH)
    return render_template('user-feed.html', user_posts=user_posts, username=username, bookmarks_posts=bookmarks_posts)


@app.errorhandler(404)
def page_not_found(error):
    """
    Представление для обработки ошибки не найденной страницы
    """
    return render_template('errors.html', title="Страница не найдена", error="Страница не найдена"), 404


@app.errorhandler(500)
def page_not_found(error):
    """
    Представление для обработки ошибки на стороне сервера
    """
    return render_template('errors.html', title=f"Ошибка сервера", error="Что-то пошло не так"), 500


@app.route('/bookmarks')
def bookmarks_pages():
    """
    Представление для отображения постов в закладках
    """
    bookmarks_posts = get_json_data(BOOKMARKS_PATH)
    return render_template('bookmarks.html', bookmarks_posts=bookmarks_posts)


@app.route('/bookmarks/remove/<int:post_id>')
def bookmarks_remove_pages(post_id):
    """
    Представление для удаления поста из закладок кнопкой "удалить"
    """
    bookmarks_posts = get_json_data(BOOKMARKS_PATH)
    for post in bookmarks_posts:
        if post['pk'] == post_id:
            bookmarks_posts.remove(post)
            break
    write_json_data(BOOKMARKS_PATH, bookmarks_posts)
    return redirect('/bookmarks', code=302)


@app.route('/bookmarks/remove_from_icon/<int:post_id>')
def bookmarks_remove_from_icon(post_id):
    """
    Представление для удаления поста из закладок с иконки закладки
    """
    bookmarks_posts = get_json_data(BOOKMARKS_PATH)
    for post in bookmarks_posts:
        if post['pk'] == post_id:
            bookmarks_posts.remove(post)
            break
    write_json_data(BOOKMARKS_PATH, bookmarks_posts)
    return redirect('/', code=302)


@app.route('/bookmarks/add/<int:post_id>')
def bookmarks_add_pages(post_id):
    """
    Представление для добавления поста в закладки
    """
    bookmarks_posts = get_json_data(BOOKMARKS_PATH)
    post = get_post_by_post_id(post_id)
    if post not in bookmarks_posts:
        bookmarks_posts.append(post)
    write_json_data(BOOKMARKS_PATH, bookmarks_posts)
    return redirect('/bookmarks', code=302)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=1000)
