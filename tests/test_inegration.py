import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Compliment
from app.database import get_db
from fastapi.testclient import TestClient
from app.main import app

# Setup an in-memory SQLite test DB
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

# Override FastAPI dependency to use our test DB
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_create_and_read_compliment_in_db():
    response = client.post("/compliments/", json={"text": "Test compliment"})
    assert response.status_code == 200
    comp_id = response.json()["id"]

    all_comps = client.get("/compliments/")
    assert any(c["id"] == comp_id for c in all_comps.json())
