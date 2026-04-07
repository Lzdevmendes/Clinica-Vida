from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_register_user():
    resp = client.post("/auth/register", json={
        "email": "test_user@clinica.com",
        "password": "senha123",
        "role": "patient"
    })
    assert resp.status_code in (200, 400)
    if resp.status_code == 200:
        data = resp.json()
        assert "id" in data
        assert data["email"] == "test_user@clinica.com"
        assert data["role"] == "patient"


def test_login_invalid_credentials():
    resp = client.post("/auth/login", data={
        "username": "naoexiste@clinica.com",
        "password": "senhaerrada"
    })
    assert resp.status_code == 401


def test_get_patients_without_token():
    resp = client.get("/api/patients")
    assert resp.status_code == 401


def test_get_consultations_without_token():
    resp = client.get("/api/consultations")
    assert resp.status_code == 401


def test_get_doctors_without_token():
    resp = client.get("/api/doctors")
    assert resp.status_code == 401
