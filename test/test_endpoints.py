import os
import sys
import json
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
    response = client.get("/routers")
    assert response.status_code == 200
    assert response.json() == ["Test endpoint"]
    
def test_redis():
    response = client.get("/redis/set/keys/world")
    assert response.status_code == 200
    assert response.json() == ["Successfully registered"]

    response = client.get("/redis/get/keys/world")
    assert response.status_code == 200

    with open("test/test_data/redis_input.json") as f:
        expect_data = json.load(f)
        
    assert response.json() == expect_data
