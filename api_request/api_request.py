from flask import Blueprint, jsonify
# import logging
from utils import get_json_data, get_post_by_post_id, POST_PATH

# создаем Blueprint для работы с API
api_request = Blueprint('api_request', __name__)

#logging.basicConfig(filename='logs/api.log', level=logging.INFO, encoding='utf-8',
#                    format="%(asctime)s %(levelname)s %(message)s")


@api_request.route('/posts')
def post_by_api():
    """
    Представление обрабатывающее GET запрос и возвращающее данные постов в json формате
    """
    # logging.info('Произведен запрос к /api/posts')
    posts = get_json_data(POST_PATH)
    return jsonify(posts)


@api_request.route('/posts/<int:post_id>')
def get_api_post(post_id):
    """
    Представление обрабатывающее GET запрос и возвращающее данные поста в json формате
    """
    # logging.info(f'Произведен запрос к /api/posts/{post_id}')
    post = get_post_by_post_id(post_id)
    return jsonify(post)
