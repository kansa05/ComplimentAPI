import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app
from app.models import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_get_all_compliments():
    response = client.get("/compliments/")
    assert response.status_code == 200

def test_post_compliment():
    response = client.post("/compliments/", json={"text": "You're awesome!"})
    assert response.status_code in [200, 201]
    assert "You're awesome!" in response.json().get("text", "")

def test_get_random_compliment():
    response = client.get("/compliments/random")
    assert response.status_code == 200
    assert "text" in response.json()

def test_put_compliment():
    # Create a compliment
    post_resp = client.post("/compliments/", json={"text": "You rock!"})
    comp_id = post_resp.json()["id"]

    # Update it
    put_resp = client.put(f"/compliments/{comp_id}", json={"text": "You rock even more!"})
    assert put_resp.status_code == 200
    assert "rock even more" in put_resp.json()["text"]

def test_delete_compliment():
    # Create
    post_resp = client.post("/compliments/", json={"text": "Temporary compliment"})
    comp_id = post_resp.json()["id"]

    #
