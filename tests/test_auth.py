from fastapi.testclient import TestClient
from app.main import app

client =TestClient(app)

def test_register_login():
  resp = client.post('/auth/register', json={'email':'t@t.com','password':'1234','role':'pacient'})
  assert resp.status_code == 201
  resp2 = client.post('/auth/login'), data={'username':'t@t.com','password':'1234'}
  assert resp2.status_code == 200
  assert 'access_token' in resp2.json()