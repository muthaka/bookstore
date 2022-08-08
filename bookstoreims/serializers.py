from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'email', 'dob')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_year', 'description')

    def create(self, validated_data):
        author_data = validated_data.pop("author")
        author_instance = Author.objects.create(**author_data)
        book_instance = Book.objects.create(author=author_instance, **validated_data)

        return book_instance


class StockSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Stock
        fields = ('id', 'book', 'stock_units', 'updated_on', 'date')

    def create(self, validated_data):
        book_data = validated_data.pop("book")
        author_data = book_data.pop("author")
        author_instance = Author.objects.create(**author_data)
        book_instance = Book.objects.create(author=author_instance, **book_data)
        stock_instance = Stock.objects.create(book=book_instance, **validated_data)

        # # Save stock to the history model
        StockHistory.objects.create(stock=stock_instance, **validated_data)

        return stock_instance


class StockHistorySerializer(serializers.ModelSerializer):
    # # stock = StockSerializer()
    class Meta:
        model = Stock
        fields = ('id', 'stock_units', 'date')
