Sales Data API - Darsh Sitapara

Introduction
This Sales Data API is a Flask-based web application that showcases CRUD operations
on a Sales dataset. It allows you to query sales data with a specified date range
or add new records to the database. It is built with Python, Flask, and MySQL.
In my testing all functionality was operational, I tested the GET via URL in
Google Chrome, and the POST with a short Python script. You can specify the
output format within the request (JSON, list, or Pandas DataFrame).

Prerequisites
Python 3.10
MySQL Server
Dependencies listed in the requirements.txt

Query Sales Data
    GET Request
        Endpoint: /sales?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&format=json
        Example: http://localhost:5000/sales?start_date=2023-01-01&end_date=2023-02-28&format=json


Add Sales Record
    POST Request
        Endpoint: /sales
        Example: curl -X POST http://localhost:5000/sales \
                 -H 'Content-Type: application/json' \
                 -d '{"id": 1002, "store_id": "TX002", "total_sales": 150.00, "date": "2023-02-01"}'