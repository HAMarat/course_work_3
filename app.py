from flask import Flask, render_template
from utils import get_posts_all, get_post_content, get_posts_by_user

app = Flask(__name__)


@app.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<post_id>')
def post_by_post_id(post_id):
    post = get_post_content(post_id)
    return render_template('post.html', post=post)


app.run(debug=True, host='127.0.0.1', port=2000)