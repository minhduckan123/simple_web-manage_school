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

def test_delete_classroom(client):
    response = client.post('/classroom/delete/<id>')
    assert response.status_code == 308

def test_student(client):
    response = client.get('/student')
    assert response.status_code == 200

def test_student_not_found(client):
    response = client.get('/students')
    assert response.status_code == 404

def test_insert_student(client):
    response = client.post('/student/insert')
    assert response.status_code == 400
    
def test_delete_student(client):
    response = client.post('/student/delete/<id>')
    assert response.status_code == 308

def test_subject(client):
    response = client.get('/subject')
    assert response.status_code == 200

def test_subject_not_found(client):
    response = client.get('/subjects')
    assert response.status_code == 404

def test_insert_subject(client):
    response = client.post('/subject/insert')
    assert response.status_code == 400

def test_delete_subject(client):
    response = client.post('/subject/delete/<id>')
    assert response.status_code == 308
    
def test_teacher(client):
    response = client.get('/teacher')
    assert response.status_code == 200

def test_teacher_not_found(client):
    response = client.get('/teachers')
    assert response.status_code == 404

def test_insert_teacher(client):
    response = client.post('/teacher/insert')
    assert response.status_code == 400
    
def test_delete_teacher(client):
    response = client.post('/teacher/delete/<id>')
    assert response.status_code == 308

def test_class(client):
    response = client.get('/school')
    assert response.status_code == 200

def test_class_not_found(client):
    response = client.get('/schools')
    assert response.status_code == 404

def test_insert_class(client):
    response = client.post('/school/insert')
    assert response.status_code == 400
    
def test_delete_class(client):
    response = client.post('/school/delete/<id>')
    assert response.status_code == 308