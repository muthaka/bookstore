from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class BookStorePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class AuthorsListApiView(APIView):
    # # permission to allow anyone to access the api
    permission_classes = [permissions.AllowAny]
    pagination_class = BookStorePagination

    # # List all Authors
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data}, status=status.HTTP_200_OK)

    # # Create an Author
    def post(self, request):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'dob': request.data.get('dob')
        }
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"authors": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorSingleApiView(APIView):
    # # permission to allow anyone to access the api
    permission_classes = [permissions.AllowAny]

    def get_object(self, author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    # # Retrieve Author using author id
    def get(self, request, author_id):
        author = self.get_object(author_id)
        if not author:
            return Response(
                {"response": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AuthorSerializer(author)
        return Response({"author": serializer.data}, status=status.HTTP_200_OK)

    # # Update Author using author id
    def put(self, request, author_id):
        author = self.get_object(author_id)
        if not author:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'dob': request.data.get('dob')
        }
        serializer = AuthorSerializer(instance=author, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Author Updated!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # Delete Author using author id
    def delete(self, request, author_id):
        author = self.get_object(author_id)
        if not author:
            return Response(
                {"response": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        author.delete()
        return Response(
            {"response": "Author deleted!"},
            status=status.HTTP_200_OK
        )


class BooksListApiView(APIView):
    # # permission to allow anyone to access the api
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer

    # # List all Books as per the filter
    def get(self, request):
        books = Book.objects.all()
        publication_year = self.request.query_params.get('publication_year', None)
        author = self.request.query_params.get('author', None)
        if publication_year is not None:
            books = books.filter(publication_year=publication_year)
        if author is not None:
            books = books.filter(Q(author__first_name__icontains=author) | Q(author__last_name__icontains=author))
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data}, status=status.HTTP_200_OK)

    # # Create a Book
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"books": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockListApiView(APIView):
    # # permission to allow anyone to access the api
    permission_classes = [permissions.AllowAny]
    serializer_class = StockSerializer

    # # List all Stocks
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response({"stocks": serializer.data}, status=status.HTTP_200_OK)

    # # Create a Stock
    def post(self, request):
        serializer = StockSerializer(data=request.data)
        book_id = self.request.query_params.get('book', None)
        if book_id is not None:
            stock_units = request.data.get('stock_units')
            book_instance = Book.objects.get(id=book_id)
            stock_instance = Stock.objects.create(book=book_instance, stock_units=stock_units)
            # # Save stock to the history model
            StockHistory.objects.create(stock=stock_instance, stock_units=stock_units)
            return Response({"stocks": " 'Stock added Successfully"}, status=status.HTTP_201_CREATED)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response({"stocks": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockSingleApiView(APIView):
    # # permission to allow anyone to access the api
    permission_classes = [permissions.AllowAny]

    def get_object(self, stock_id):
        try:
            return Stock.objects.get(id=stock_id)
        except Stock.DoesNotExist:
            return None

    # # Retrieve Stock using stock id
    def get(self, request, stock_id):
        stock = self.get_object(stock_id)
        if not stock:
            return Response(
                {"response": "Object with stock id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StockSerializer(stock)
        return Response({"stock": serializer.data}, status=status.HTTP_200_OK)

    # # Update Stock using stock id
    def put(self, request, stock_id):
        stock = self.get_object(stock_id)
        if not stock:
            return Response(
                {"res": "Object with stock id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'stock_units': request.data.get('stock_units')
        }

        serializer = StockSerializer(instance=stock, data=data, partial=True)
        history_data = request.data.get('stock_units')
        if serializer.is_valid():
            serializer.save()
            # # Save stock update to the history model
            StockHistory.objects.create(stock=stock, stock_units=history_data)

            return Response({"response": "Stock Updated!"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # Prevent Deleting Stock using stock id
    def delete(self, request, stock_id):
        stock = self.get_object(stock_id)
        if not stock:
            return Response(
                {"response": "Deleting Stock is Not allowed!!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"response": "Deleting Stock is Not allowed!!"},
            status=status.HTTP_200_OK
        )


class StockStatusApiView(APIView):
    # # permission to allow anyone to access the api
    permission_classes = [permissions.AllowAny]

    def get_object(self, stock_id):
        try:
            return Stock.objects.get(id=stock_id)
        except Stock.DoesNotExist:
            return None

    # # Retrieve Stock using stock id
    def get(self, request, stock_id):
        stock = self.get_object(stock_id)
        if not stock:
            return Response(
                {"response": "Stock with stock id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"Stock Status": stock.status}, status=status.HTTP_200_OK)


class StockHistoryApiView(APIView):
    # # permission to allow anyone to access the api
    permission_classes = [permissions.AllowAny]

    # # List History of Stock
    def get(self, request, stock_id):
        stocks = StockHistory.objects.filter(stock=stock_id)
        serializer = StockHistorySerializer(stocks, many=True)
        return Response({"stock_history": serializer.data}, status=status.HTTP_200_OK)
