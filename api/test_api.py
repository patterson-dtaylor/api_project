
def test_api_healthcheck(app, client):
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_create_user(app, client):
    sample_payload = {
        "name":"PLACEHOLDER", 
        "username":"PLACEHOLDER", 
        "email":"PLACEHOLDER@mail.com"
    }
    response = client.post("/user", json=sample_payload)
    assert response.status_code == 200
    assert b'{"Status":"Success","User":{"email":"PLACEHOLDER@mail.com","name":"PLACEHOLDER","username":"PLACEHOLDER"}}' in response.data

def test_get_users(app, client):
    response = client.get("/users")
    assert response.status_code == 200

def test_update_user(app, client):
    sample_payload = {
        "id": 1,
        "name":"PLACEHOLDER2", 
        "username":"PLACEHOLDER2", 
        "email":"PLACEHOLDER@mail.com"
    }
    response = client.put("/user/1", json=sample_payload)
    assert response.status_code == 200
    assert b'{"Status":"Success","User":{"email":"PLACEHOLDER@mail.com","id":1,"name":"PLACEHOLDER2","username":"PLACEHOLDER2"}}' in response.data

def test_delete_user(app, client):
    sample_payload = {
        "id": 1
    }
    response = client.delete("/user/1", json=sample_payload)
    assert response.status_code == 200
    assert b'{"Message":"User deleted successfully","Status":"Success"}' in response.data