import requests

def test_acceptance():
    r = requests.get('http://localhost:5000/todos')
    todos = r.json()

    assert len(todos) == 0
    assert r.status_code == 200