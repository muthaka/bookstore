from django.db import models
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-first_name']
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='book_author')
    publication_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-title']
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Stock(models.Model):
    stock_name = models.CharField(max_length=100, null=True)
    books = models.ManyToManyField(Book, blank=True, related_name="stock_books")
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    # stock_status = len(stock_books)

    class Meta:
        ordering = ['-stock_name']
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return self.stock_name

