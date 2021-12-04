import requests


def test_acceptance():
    r = requests.get('http://localhost:5000/todos')
    assert len(r.json()) == 0
    assert r.status_code == 200

    r = requests.post('http://localhost:5000/todos',
                      json={'title': 'Buy milk'})
    assert r.json() == {
        'title': 'Buy milk',
        'done': False,
    }
    assert r.status_code == 201

    r = requests.get('http://localhost:5000/todos')
    assert r.json() == [{
        'title': 'Buy milk',
        'done': False,
    }]
    assert r.status_code == 200

    r = requests.patch('http://localhost:5000/todos',
                       json={'title': 'Buy milk', 'done': True})
    assert r.json() == {
        'title': 'Buy milk',
        'done': True,
    }
    assert r.status_code == 200

    r = requests.get('http://localhost:5000/todos')
    assert r.json() == [{
        'title': 'Buy milk',
        'done': True,
    }]
    assert r.status_code == 200

    r = requests.delete('http://localhost:5000/todos',
                        json={'title': 'Buy milk'})
    assert r.json() == {
        'title': 'Buy milk',
    }
    assert r.status_code == 200

    r = requests.get('http://localhost:5000/todos')
    assert len(r.json()) == 0
    assert r.status_code == 200
