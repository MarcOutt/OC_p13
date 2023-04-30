import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_create_address():
    user = User.objects.create(username='Jean',
                               password='Azerty12345'
                           )
    assert user.username == 'Jean'
    assert user.password == 'Azerty12345'

    profile = Profile.objects.create(user=user,
                                     favorite_city='Paris')

    assert profile.user == user
    assert profile.favorite_city == 'Paris'
