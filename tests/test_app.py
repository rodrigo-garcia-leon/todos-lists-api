import pytest
from src.app import app

client = app.test_client();

def test_hello_world():
    response = client.get('/')
    assert b'Hello World' in response.data