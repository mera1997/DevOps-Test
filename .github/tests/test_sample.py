# tests/test_sample.py

import requests

def test_example():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    data = response.json()
    assert 'title' in data

