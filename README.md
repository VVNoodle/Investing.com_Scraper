#  investing.com_exercise
  
##  Prerequisites

- Python 3.*
- Docker and docker-compose is preferred but optional.

##  Installing

Clone the repository
```

git clone https://github.com/VVNoodle/Investing.com_Scraper.git

```

## How to Run
You can choose to run using Docker or manually.
### Using Docker
build docker image and run it by executing
```
docker-compose up --build
```
docker automatically:

 - installs dependencies
 - fetches data 
 - runs the flask server

### Manually
 install dependencies. you can choose to create a virtual environment if preferred.
 ```
 pip install -r requirements.txt
 ```
 fetch data
 ```
 python3 fetch_data.py
 ```
 After finish executing, there will be 2 .csv files: `gold.csv` and `silver.csv`. They consist the corresponding `Date` and `Price` features as per exercise specs. 
Next thing to do is to run the flask server
 ```
 python3 service.py
 ```

## API Endpoints 

* **URL**

  /commodity?start_date=2019-04-17&end_date=2019-05-01&commodity_type=gold

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `start_date=[datetime]`
   `end_date=[datetime]`
    `commodity_type=[string]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**  JSON Response
    ``
    { 
    data : {
    "2017-05-10": 1253.06,  
"2017-05-11": 1280.46,  
"2017-05-12": 1278.21
},
mean: 1270.57,
"variance": 231.39
	 }
 ``
 
* **Error Response:**

  * **Code:** 422 Unprocessable Entity <br />
    **Content:** `{ error : "valid url, but not all required parameters are entered (start_date, end_date, commodity_type)" }`

  OR

  * **Code:** 404 URL not found <br />

* **Sample Call:**
  ```
  http://127.0.0.1:8080/commodity?start_date=2019-04-17&end_date=2019-05-01&commodity_type=gold
  ```


##  Built With
*  [Pandas](https://pandas.pydata.org/) - data structures and data analysis tools
*  [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web Scraping
  

##  Author
*  **Egan Bisma**
  