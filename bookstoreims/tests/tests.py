import pytest

from django.urls import reverse

from bookstoreims.models import Author, Book
from bookstoreims.serializers import AuthorSerializer, BookSerializer


@pytest.mark.django_db
def test_list_author(client):
    url = reverse('list_authors')
    response = client.get(url)

    authors = Author.objects.all()
    expected_data = (AuthorSerializer(authors, many=True)).data
    expected_data = {"authors": expected_data}

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_list_books(client):
    url = reverse('list_books')
    response = client.get(url)

    books = Book.objects.all()
    expected_data = (BookSerializer(books, many=True)).data
    expected_data = {"books": expected_data}

    assert response.status_code == 200
    assert response.data == expected_data
