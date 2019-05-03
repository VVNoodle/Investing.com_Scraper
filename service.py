from flask import Flask, request
from fetch_data import extract_data
import pandas as pd
import sys

app = Flask(__name__)

# http://127.0.0.1:8080/commodity?start_date=2017-05-10&end_date=2017-05-22&commodity_type=gold


@app.route('/')
def home():
    return "HI"


@app.route('/commodity')
def commodity():
    start_date = request.args["start_date"] if "start_date" in request.args else None
    end_date = request.args["end_date"] if "end_date" in request.args else None
    commodity_type = request.args["commodity_type"] if "commodity_type" in request.args else None
    if commodity_type == None:
        return "You must provide a commodity type"
    commodity = pd.DataFrame()
    if commodity_type == "gold":
        commodity = extract_data("gold")
    elif commodity_type == "silver":
        commodity = extract_data("silver")

    commodity = commodity[pd.to_datetime(commodity['Date']).dt.date.astype(
        str) >= start_date] if start_date != None else commodity

    commodity = commodity[pd.to_datetime(commodity['Date']).dt.date.astype(
        str) <= end_date] if start_date != None else commodity

    print(commodity, file=sys.stderr)

    return "{} {} {}".format(start_date, end_date, commodity_type)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="8080")
