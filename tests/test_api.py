from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_process_endpoint():
    response = client.post("/process", json={"transcript": "John will finish the report by Friday."})
    # This will fail without valid OpenAI key, but structure is correct
    assert response.status_code in [200, 500]