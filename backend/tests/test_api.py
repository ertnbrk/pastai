'''
from fastapi.testclient import TestClient
from backend.app.main import app
client = TestClient(app)

def test_record_journal():
    response = client.post("/api/v1/journal", json={"user_id": 1, "text": "This is a test journal entry."})
    assert response.status_code == 201
    assert response.json() == {"message": "Journal entry recorded successfully."}

def test_get_context():
    response = client.get("/api/v1/context?user_id=1")
    assert response.status_code == 200
    assert "data" in response.json()

def test_chat():
    response = client.post("/api/v1/chat", json={"user_id": 1, "input": "Tell me about my last journal entry."})
    assert response.status_code == 200
    assert "response" in response.json()

def test_list_reminders():
    response = client.get("/api/v1/reminders?user_id=1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_reminder():
    response = client.post("/api/v1/reminders", json={"user_id": 1, "text": "Doctor's appointment", "datetime": "2023-10-10T10:00:00"})
    assert response.status_code == 201
    assert response.json() == {"message": "Reminder created successfully."}
'''
