import pytest
from django.test import Client
from django.urls import reverse


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_index(client):
    path = reverse('index')
    response = client.get(path)
    assert response.status_code == 200
    assert b'<title>Holiday Homes</title>' in response.content
