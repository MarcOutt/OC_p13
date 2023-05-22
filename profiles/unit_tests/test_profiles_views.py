import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_profile_index(client):
    user = User.objects.create(username='Jean',
                               password='Azerty12345'
                               )

    profiles = Profile.objects.create(user=user,
                                      favorite_city='Paris')

    path = reverse('profiles_index')
    response = client.get(path)
    assert response.status_code == 200
    assert b'<title>Profiles</title>' in response.content
    assert f'<a href="/profiles/{profiles}/">' in str(response.content)


@pytest.mark.django_db
def test_profiles(client):
    user = User.objects.create(username='Jean',
                               password='Azerty12345'
                               )

    Profile.objects.create(user=user,
                           favorite_city='Paris')

    response = client.get('/profiles/Jean/')
    assert response.status_code == 200
    assert b'<title>Jean</title>' in response.content
    assert b'<p>Favorite city: Paris</p>' in response.content
