from flask import Flask, request, jsonify, json, render_template
from fetch_data import extract_data
import pandas as pd
import sys

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/commodity')
def commodity():
    start_date = request.args["start_date"] if "start_date" in request.args else None
    end_date = request.args["end_date"] if "end_date" in request.args else None
    commodity_type = request.args["commodity_type"] if "commodity_type" in request.args else None
    if commodity_type == None or start_date == None or end_date == None:
        return "You must provide commodity_type, start_date and end_date params", 422
    commodity = pd.DataFrame()
    if commodity_type == "gold":
        commodity = extract_data("gold")
    elif commodity_type == "silver":
        commodity = extract_data("silver")

    converted_date = pd.to_datetime(commodity['Date']).dt.date.astype(str)
    mask = (converted_date >= start_date) & (converted_date <= end_date)
    commodity = commodity.loc[mask]

    # set index column as Date, for formatting requirements of the exercise
    commodity = commodity.set_index("Date")
    data = json.loads(commodity.to_json())["Price"]
    return jsonify(
        data=data,
        mean=commodity.mean()["Price"],
        variance=commodity.var()["Price"])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="8080")
