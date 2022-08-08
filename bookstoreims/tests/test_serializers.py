import pytest

from django.urls import reverse

from bookstoreims.models import *
from bookstoreims.serializers import *


@pytest.mark.django_db
def test_list_authors(client):
    url = reverse('list_authors')
    response = client.get(url)

    authors = Author.objects.all()
    expected_data = (AuthorSerializer(authors, many=True)).data
    expected_data = {"authors": expected_data}
    assert response.data == expected_data


@pytest.mark.django_db
def test_list_books(client):
    url = reverse('list_books')
    response = client.get(url)

    books = Book.objects.all()
    expected_data = (BookSerializer(books, many=True)).data
    expected_data = {"books": expected_data}
    assert response.data == expected_data


@pytest.mark.django_db
def test_list_stocks(client):
    url = reverse('list_stocks')
    response = client.get(url)

    stocks = Stock.objects.all()
    expected_data = (StockSerializer(stocks, many=True)).data
    expected_data = {"stocks": expected_data}
    assert response.data == expected_data

