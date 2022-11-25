import pytest
from app import app


def test_app_posts():
    """
    Функция для тестирования API '/api/posts'
    """
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list, 'не возвращается словарь'
    assert response.json[0].get("poster_name") is not None, 'у элемента отсутствует нужный ключ "poster_name"'


def test_app_posts_id():
    """
    Функция для тестирования API '/api/posts/2'
    """
    response = app.test_client().get('/api/posts/2')
    assert type(response.json) == dict, 'не возвращается словарь'
    assert response.json.get("poster_name") is not None, 'у элемента отсутствует нужный ключ "poster_name"'
