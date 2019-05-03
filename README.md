
# Investing.com_Scraper

# assumptions
    - 

# fetch_data.py
### requirements
    - fetch data from 2 URLs
      - what do they mean by fetch?
    - only fetch date and price
    - save as csv or other format that makes sense
    - Python3
### extras
    - containerize
    - unit tests
### pseudocode
    1) create table
    2) scrape website for date and range (only on first page)
    3) add data to table
    4) save data as csv

# service.py
### requirements
    - API web-service (port 8080)
    - flask
    - return stored data
    - Python3
    - GET endpoints
      - return value: JSON time series, mean and variance
      - over specified period
        - start_date - required (iso format like 2017-05-10)
        - end_date - required (iso format like 2017-05-22)
        - commodity_type - required (gold, silver)
        - example of calling by using curl:
          - curl 'http://127.0.0.1:8080/commodity?start_date=2017-05-10&end_date=2017-05-22&commodity_type=gold'
        - example of output data:
            `{
            "data": {
            "2017-05-10": 1253.06,
            "2017-05-11": 1280.46,
            "2017-05-12": 1278.21
            }
            "mean": 1270.57,
            "variance": 231.39
            }`
### extras
    - containerize
    - unit tests
### pseudocode
    1) create table

# questions
    - should the two programs be in one docker container
