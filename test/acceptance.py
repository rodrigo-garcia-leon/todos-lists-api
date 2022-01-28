"""Acceptance test for the API"""

import requests


def test_acceptance():
    """Acceptance test for the API."""
    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
    assert len(response.json()) == 0

    response = requests.post('http://localhost:5000/todos',
                             json={'title': 'Buy milk'})
    assert response.status_code == 201
    assert response.json() == {
        'title': 'Buy milk',
        'done': False,
    }

    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
    assert response.json() == [{
        'title': 'Buy milk',
        'done': False,
    }]

    response = requests.patch('http://localhost:5000/todos',
                              json={'title': 'Buy milk', 'done': True})
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Buy milk',
        'done': True,
    }

    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
    assert response.json() == [{
        'title': 'Buy milk',
        'done': True,
    }]

    response = requests.delete('http://localhost:5000/todos',
                               json={'title': 'Buy milk'})
    assert response.status_code == 204
    assert response.text == ''

    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
    assert len(response.json()) == 0
