import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_list_authors(client):
    url = reverse('list_authors')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_books(client):
    url = reverse('list_books')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_stocks(client):
    url = reverse('list_stocks')
    response = client.get(url)
    assert response.status_code == 200


