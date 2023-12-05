from uuid import UUID
from fastapi import status
from fastapi.testclient import TestClient
from link_shortener_fastapi.main import app

client = TestClient(app)


def test_get_root():
    resp = client.get("/")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"message": "Hello World"}


def test_post_link():
    payload = {"redirect_url": "http://www.example.com"}
    resp = client.post("/link", json=payload)
    print(resp.json())
    assert resp.status_code == status.HTTP_200_OK
    assert isinstance(UUID(resp.json().get("id")), UUID)


def test_post_get_link():
    payload = {"redirect_url": "http://www.example.com"}
    post_resp = client.post("/link", json=payload)
    assert post_resp.status_code == status.HTTP_200_OK
    get_resp = client.get(f"/link/{post_resp.json().get('id')}")
    assert get_resp.status_code == status.HTTP_200_OK
    assert get_resp.json() == {"message": "Hello World"}
