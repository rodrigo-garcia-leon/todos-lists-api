"""Acceptance test for the API"""

import requests


def test_acceptance():
    """Acceptance test for the API."""
    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
    assert len(response.json()) == 0

    response = requests.post('http://localhost:5000/todos',
                             json={'title': 'Buy milk'})
    id = response.json()['_id']
    assert response.status_code == 201
    assert response.json() == {
        '_id': id,
        'title': 'Buy milk',
        'done': False,
        'comments': []
    }

    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
    assert response.json() == [{
        '_id': id,
        'title': 'Buy milk',
        'done': False,
        'comments': []
    }]

    response = requests.get('http://localhost:5000/todo/' + id)
    assert response.status_code == 200
    assert response.json() == {
        '_id': id,
        'title': 'Buy milk',
        'done': False,
        'comments': []
    }

    response = requests.patch('http://localhost:5000/todos',
                              json={'_id': id, 'title': 'Buy milk', 'done': True})
    assert response.status_code == 200
    assert response.json() == {
        '_id': id,
        'title': 'Buy milk',
        'done': True,
        'comments': []
    }

    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
    assert response.json() == [{
        '_id': id,
        'title': 'Buy milk',
        'done': True,
        'comments': []
    }]

    response = requests.delete('http://localhost:5000/todos',
                               json={'title': 'Buy milk'})
    assert response.status_code == 204
    assert response.text == ''

    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
    assert len(response.json()) == 0
