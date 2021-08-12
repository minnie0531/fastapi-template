import os
import sys
from fastapi.testclient import TestClient

sys.path.append(
    (os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "/app/")
)

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ["Hello World :D"]


def test_router_query():
    response = client.get("/queries")
    assert response.status_code == 200
    assert response.json() == ["Test endpoint"]
