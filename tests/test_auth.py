from clients.auth_client import AuthClient


def test_user_login_success():

    client = AuthClient()

    response = client.login(email="test@example.com", password="password123")

    assert response.status_code == 200
    assert client.token is not None


def test_user_login_invalid():

    client = AuthClient()
    response = client.login(email="test@example.com", password="wrong_password")

    assert response.status_code == 401
