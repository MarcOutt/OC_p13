import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_create_address():
    address = Address.objects.create(number='0150658456',
                                     street='13 rue de paris',
                                     city='Paris',
                                     state='Seine',
                                     zip_code='75001',
                                     country_iso_code=23
                                     )
    assert address.number == '0150658456'
    assert address.street == '13 rue de paris'
    assert address.city == 'Paris'
    assert address.state == 'Seine'
    assert address.zip_code == '75001'
    assert address.country_iso_code == 23


@pytest.mark.django_db
def test_create_letting():
    address = Address.objects.create(number='0150658456',
                                     street='13 rue de paris',
                                     city='Paris',
                                     state='Seine',
                                     zip_code='75001',
                                     country_iso_code=23
                                     )

    letting = Letting.objects.create(title='Blue Lagoon',
                                     address=address)

    assert letting.title == 'Blue Lagoon'
    assert letting.address == address
