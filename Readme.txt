Sales Data API - Darsh Sitapara

Introduction
This Sales Data API is a Flask-based web application that showcases CRUD operations
on a Sales dataset. It allows you to query sales data with a specified date range
or add new records to the database. It is built with Python, Flask, and MySQL.
In my testing all functionality was operational, I tested the GET via URL in
Google Chrome, and the POST with a short Python script. You can specify the
output format within the requests (JSON, list, or Pandas DataFrame).

Prerequisites
Python 3.10
MySQL Server
Dependencies listed in the requirements.txt

Query Sales Data
    GET Request (JSON)
        Endpoint: /sales?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&format=json
        Example: http://localhost:5000/sales?start_date=2023-01-01&end_date=2023-02-28&format=json
    GET Request (List)
        Endpoint: /sales?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&format=list
        Example: http://localhost:5000/sales?start_date=2023-01-01&end_date=2023-02-28&format=list
    GET Request (Data Frame)
        Endpoint: /sales?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&format=json
        Example: Using Python (Example file GET.py)

Add Sales Record
    POST Request
        Endpoint: /sales
        Example: (Example file POST.py)