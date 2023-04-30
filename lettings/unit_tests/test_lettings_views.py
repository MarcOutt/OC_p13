import pytest
from django.test import Client
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_index(client):
    address = Address.objects.create(number='0150658456',
                                     street='13 rue de paris',
                                     city='Paris',
                                     state='Seine',
                                     zip_code='75001',
                                     country_iso_code=23
                                     )

    letting = Letting.objects.create(title='Blue Lagoon',
                                     address=address)

    path = reverse('lettings_index')
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting(client):
    address = Address.objects.create(number='0150658456',
                                     street='13 rue de paris',
                                     city='Paris',
                                     state='Seine',
                                     zip_code='75001',
                                     country_iso_code=23
                                     )

    letting = Letting.objects.create(title='Blue Lagoon',
                                     address=address)

    response = client.get('/lettings/1/')
    assert response.status_code == 200
