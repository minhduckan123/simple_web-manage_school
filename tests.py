import pytest
from api_web import app as _app

@pytest.fixture
def app():
    return _app

def test_home(client):
    response = client.get('/home')
    assert "About" in response.data.decode()

def test_classroom(client):
    response = client.get('/classroom')
    assert response.status_code == 200

def test_classroom_not_found(client):
    response = client.get('/classroomxxx')
    assert response.status_code == 404

def test_insert_classroom(client):
    response = client.post('/classroom/insert')
    assert response.status_code == 400

# app()
test_home()