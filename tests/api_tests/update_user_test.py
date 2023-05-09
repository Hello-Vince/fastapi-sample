'''This module performs API tests on the following directory: ./apis/routers/update_user.py'''

from starlette.testclient import TestClient

from config import settings
from main import app
from apis.exceptions import exc


client = TestClient(app)


def test_update_user_200():
    '''Test a Good request to the API /user/update'''

    response = client.post(
        url='/user/update',
        json=dict(
            email=settings.TESTING.USER_EMAIL,
            password=settings.TESTING.USER_PASSWORD,
            is_active=settings.TESTING.USER_STATUS
        )
    )

    assert response.status_code == 200
    assert response.json() == dict(
        message='User has successfully been updated.'
    )


def test_update_user_401():
    '''Test Bad requests to the API /user/update'''

    response1 = client.post(
        url='/user/update',
        json=dict(
            email='invalid@email.com',
            password=settings.TESTING.USER_PASSWORD,
            is_active=settings.TESTING.USER_STATUS
        )
    )

    assert response1.status_code == 401
    assert response1.json() == dict(
        message=exc.NOT_EMAIL
    )

    response2 = client.post(
        url='/user/update',
        json=dict(
            email=settings.TESTING.USER_EMAIL,
            password='invalid-password',
            is_active=settings.TESTING.USER_STATUS
        )
    )

    assert response2.status_code == 401
    assert response2.json() == dict(
        message=exc.NOT_PASSWORD
    )
