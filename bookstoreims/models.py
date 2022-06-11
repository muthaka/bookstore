from django.db import models

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
    book = models.OneToOneField(Book, on_delete=models.CASCADE, unique=True, related_name="stock_books")
    stock_units = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    @property
    def status(self):
        # # Validate the stock status
            if self.stock_units >= 10:
                return "Good"
            elif (self.stock_units >= 5) and (self.stock_units < 10):
                return "Bad"
            elif (self.stock_units >= 1) and (self.stock_units < 5):
                return "Critical"
            else:
                return "Out of stock"

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return self.book.title


class StockHistory(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="stock")
    stock_units = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'StockHistory'

    def __str__(self):
        return self.stock.book.title
