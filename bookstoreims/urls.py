from django.urls import path
from .views import (
    AuthorsListApiView,
    AuthorSingleApiView,
    BooksListApiView,
    StockListApiView,
    StockSingleApiView,
    StockStatusApiView,
    StockHistoryApiView,
)


urlpatterns = [
    path('api/authors', AuthorsListApiView.as_view(), name='list_authors'),
    path('api/author/<int:author_id>', AuthorSingleApiView.as_view(), name='single_author'),
    path('api/books', BooksListApiView.as_view(), name='list_books'),
    path('api/stocks', StockListApiView.as_view(), name='list_stocks'),
    path('api/stock/<int:stock_id>', StockSingleApiView.as_view(), name='single_stock'),
    path('api/stock/status/<int:stock_id>', StockStatusApiView.as_view(), name='stock_status'),
    path('api/stock/history/<int:stock_id>', StockHistoryApiView.as_view(), name='stock_history'),
]
