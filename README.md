# Bookstore Inventory Management System
Creating a Restful API for the system using Django.


Dependencies
------------

App runs on Python 3.8.10 and Django 4.0.5

# Running the application
To run the app on the root folder using your terminal, run the commands:

1. Create an environment and Activate it.

```json
virtualenv env
source env/bin/activate
```
2. Install the app dependencies to your environment.

```json
pip install -r requirements.txt
```
3. Run the app

```json
python manage.py runserver
```


# Accessing the API endpoints
The app sqlite database has dummy data that can retrieve existing data.

Default localhost address and port is 127.0.0.1:8000 which can change depending with the one set.
NOTE: to access the endpoint in your browser or other end, start with the adress then the endpoint.
e.g 127.0.0.1:8000/api/authors

API endpoint to list all book authors and Add authors

Endpoint: api/authors

Returns all the book authors in json format as shown below

```json
    {
    "authors": [
        {
            "first_name": "Ramachandra",
            "last_name": "Guha",
            "email": "ramachandra@gmail.com",
            "dob": "1965-11-06"
        }
      ]
    }
```

Json to Add an author

POST

```json
    {
         "first_name": " ",
         "last_name": " ",
         "email": " ",
         "dob": " "
    }
```

API endpoint to check single author

Endpoint: api/author/<author_id>
Endpoint Example: api/author/5

```json
{
    "author": {
        "first_name": "Alfredo",
        "last_name": "Covelli",
        "email": "alfredo@gmail.com",
        "dob": "1955-06-01"
    }
}
```

API endpoint to list all books and add a book

Endpoint: api/books

```json
    {
    "books": [
        {
            "title": "Vahana Masterclass",
            "author": {
                "first_name": "Alfredo",
                "last_name": "Covelli",
                "email": "alfredo@gmail.com",
                "dob": "1955-06-01"
            },
            "publication_year": 2020,
            "description": "Masterclass"
        }
      ]
    }
```
Json to Add a book

POST

```json
    {
        "title": " ",
        "author": {
            "first_name": " ",
            "last_name": " ",
            "email": " ",
            "dob": " "
        },
        "publication_year": ,
        "description": " "
    }
```

API endpoint to filter books by publication year and author(checks first name and second name)

Endpoint: api/books?publication_year=
Endpoint: api/books?author=
Endpoint: api/books?publication_year=2021&author=Singh

```json
    {
    "books": [
        {
            "title": "Making of a General-A Himalayan Echo",
            "author": {
                "first_name": "Lt. Gen. Konsam Himalay",
                "last_name": "Singh",
                "email": "singh@gmail.com",
                "dob": "1950-09-24"
            },
            "publication_year": 2021,
            "description": "first Three Star General."
        }
    ]
}
```


API endpoint to list all stocks and add new stock

Endpoint: api/stocks

```json
{
    "stocks": [
        {
            "book": {
                "title": "Vahana Masterclass",
                "author": {
                    "first_name": "Alfredo",
                    "last_name": "Covelli",
                    "email": "alfredo@gmail.com",
                    "dob": "1955-06-01"
                },
                "publication_year": 2020,
                "description": "Masterclass"
            },
            "stock_units": 20,
            "updated_on": "2022-06-11T13:49:48.384431+03:00",
            "date": "2022-06-11T13:49:48.384485+03:00"
        }
    ]
}
```

Json to Add a new stock and new book

POST

```json

        {
            "book": {
                "title": " ",
                "author": {
                    "first_name": " ",
                    "last_name": " ",
                    "email": " ",
                    "dob": " "
                },
                "publication_year": ,
                "description": " "
            },
            "stock_units":
        }

```

API endpoint to update stock unit

Endpoint: api/stock/<stock_id>
Endpoint Example: api/stock/1

POST

```json
    {
    "stock_units":
    }
```

API endpoint to check stock status

Endpoint: api/stock/status/<stock_id>
Endpoint Example: api/stock/status/1

```json
    {
    "Stock Status": "Good"
    }
```

API endpoint to check stock history

Endpoint: api/stock/history/<stock_id>
Endpoint Example: api/stock/history/1

```json
{
    "stock_history": [
        {
            "stock_units": ,
            "date": " "
        }
    ]
}
```

# Running the Unit Test using Pytest
Run the test using the below command:
```json
pytest
```