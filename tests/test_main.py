from fastapi import status
from fastapi.testclient import TestClient
from link_shortener_fastapi.main import app

client = TestClient(app)

def test_get_root():
    resp = client.get('/')
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"message": "Hello World"}

def test_get_link():
    resp = client.get('/link/123')
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"message": "Hello World"}

def test_get_empty_link():
    resp = client.get('/link/')
    assert resp.status_code == status.HTTP_404_NOT_FOUND
    assert resp.json() == {'error': 'No redirect'}