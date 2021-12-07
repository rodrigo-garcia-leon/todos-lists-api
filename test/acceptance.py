"""Acceptance test for the API."""
import requests


def test_acceptance():
    """Acceptance test for the API."""
    response = requests.get('http://localhost:5000/todos')
    assert len(response.json()) == 0
    assert response.status_code == 200

    response = requests.post('http://localhost:5000/todos',
                             json={'title': 'Buy milk'})
    assert response.json() == {
        'title': 'Buy milk',
        'done': False,
    }
    assert response.status_code == 201

    response = requests.get('http://localhost:5000/todos')
    assert response.json() == [{
        'title': 'Buy milk',
        'done': False,
    }]
    assert response.status_code == 200

    response = requests.patch('http://localhost:5000/todos',
                              json={'title': 'Buy milk', 'done': True})
    assert response.json() == {
        'title': 'Buy milk',
        'done': True,
    }
    assert response.status_code == 200

    response = requests.get('http://localhost:5000/todos')
    assert response.json() == [{
        'title': 'Buy milk',
        'done': True,
    }]
    assert response.status_code == 200

    response = requests.delete('http://localhost:5000/todos',
                               json={'title': 'Buy milk'})
    assert response.json() == {
        'title': 'Buy milk',
    }
    assert response.status_code == 200

    response = requests.get('http://localhost:5000/todos')
    assert len(response.json()) == 0
    assert response.status_code == 200
