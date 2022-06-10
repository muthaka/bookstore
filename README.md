# Bookstore Inventory Management System
Creating a Restful API for the system.


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

API endpoint to check single author

Endpoint: api/author/<author_id>
Endpoint Example: api/author/1


API endpoint to list all books

Endpoint: api/books


API endpoint to list all stocks

Endpoint: api/stocks


API endpoint to list all stocks

Endpoint: api/stock/status/<stock_id>
Endpoint Example: api/stock/status/1

# Running the Unit Test
Run the test using the below command:
```json
pytest
```