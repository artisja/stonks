#!/usr/bin/env python3
import flask
import boto3
import requests
import csv
import codecs
from contextlib import closing
from flask import request, jsonify

url = 'https://www.alphavantage.co/query?'
api_key = 'AXEB36G7VB1LH885'
active_query = 'function=LISTING_STATUS&state=active&apikey='

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/gatherData/<string:sector>',methods=['Get'])
def retrieve_financial_data(sector):
    print(sector)
    return jsonify(get_listed_companies())

def get_listed_companies():
    response = requests.get(url + active_query +api_key)
    company_list = []
    with closing(response) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
        for row in reader:
            company_list.append(row)
    # reade = csv.reader(text, delimiter=',')
    # company_list = response.text
    # companies = csv.reader(company_list)
    # print(companies)
    # line_count = 0
    # for row in reader:
    #     print(row)
    # print(line_count)
    # company_list
    return company_list

def filter_list():
    print()

@app.route('/test',methods=['GET'])
def test():
    return '''<h1>Wano</h1>
<p>Eustass the Kid has been captured by Kaido!</p>'''

if __name__ == "__main__":
    app.run(host="localhost", debug=True)