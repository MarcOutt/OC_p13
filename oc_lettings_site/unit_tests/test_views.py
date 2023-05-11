import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
