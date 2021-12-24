"""Acceptance test for the API"""

import requests


def test_acceptance():
    """Acceptance test for the API."""
<<<<<<< HEAD
    response = requests.get('http://localhost:5100/todos')
    assert len(response.json()) == 0
=======
    response = requests.get('http://localhost:5000/todos')
>>>>>>> 14c1270542427d15f96611cb85b7db3aec848a9a
    assert response.status_code == 200
    assert len(response.json()) == 0

    response = requests.post('http://localhost:5100/todos',
                             json={'title': 'Buy milk'})
    assert response.status_code == 201
    assert response.json() == {
        'title': 'Buy milk',
        'done': False,
    }

<<<<<<< HEAD
    response = requests.get('http://localhost:5100/todos')
=======
    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
>>>>>>> 14c1270542427d15f96611cb85b7db3aec848a9a
    assert response.json() == [{
        'title': 'Buy milk',
        'done': False,
    }]

    response = requests.patch('http://localhost:5100/todos',
                              json={'title': 'Buy milk', 'done': True})
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Buy milk',
        'done': True,
    }

<<<<<<< HEAD
    response = requests.get('http://localhost:5100/todos')
=======
    response = requests.get('http://localhost:5000/todos')
    assert response.status_code == 200
>>>>>>> 14c1270542427d15f96611cb85b7db3aec848a9a
    assert response.json() == [{
        'title': 'Buy milk',
        'done': True,
    }]

    response = requests.delete('http://localhost:5100/todos',
                               json={'title': 'Buy milk'})
    assert response.status_code == 204
    assert response.text == ''

<<<<<<< HEAD
    response = requests.get('http://localhost:5100/todos')
    assert len(response.json()) == 0
=======
    response = requests.get('http://localhost:5000/todos')
>>>>>>> 14c1270542427d15f96611cb85b7db3aec848a9a
    assert response.status_code == 200
    assert len(response.json()) == 0
