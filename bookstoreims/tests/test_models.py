import pytest
from bookstoreims.models import *


@pytest.mark.django_db
def test_author_count():
    assert Author.objects.count() == 0


@pytest.mark.django_db
def test_book_count():
    assert Book.objects.count() == 0


@pytest.mark.django_db
def test_stock_count():
    assert Stock.objects.count() == 0


@pytest.mark.django_db
def test_stock_history_count():
    assert StockHistory.objects.count() == 0
