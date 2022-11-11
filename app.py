from flask import Flask, render_template, request
from utils import get_posts_all, get_post_content, get_posts_by_user, get_comments_by_post_id, search_for_posts

app = Flask(__name__)


@app.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>')
def post_by_post_id(post_id):
    post = get_post_content(post_id)
    comments = get_comments_by_post_id(post_id)
    print(comments)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search', methods=['GET'])
def search():
    query = request.args['s']
    found_posts = search_for_posts(query)
    return render_template('search.html', found_posts=found_posts)


@app.route('/users/<username>')
def user_posts():
    return render_template('user-feed.html')


app.run(debug=True, host='127.0.0.1', port=4000)
