from flask import Flask
from flask import request, render_template, jsonify, g

import json

# TODO: import any necessary models and/or DB utiilities
# ie: from app.models.models import Company

import os

# TODO: delete line below
app = Flask(__name__, static_folder="../React/vested/build/static", template_folder="../React/vested/build")

# base path, render according to react-generated html file
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# catch all route to keep users on react single page
@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')

# route to fetch company data from the API
@app.route("/api/get_company_data", methods=["POST"])
def get_company_data():
    # get the request from the POST in JSON format
    incoming = request.get_json()
    # extract the company from the JSON
    incoming.get('company')

    # return the JSON representation of the data
    # ie: return jsonify(data=Company.get_stocks_and_sentiments)

    # for now, we'll return the sample_data.json
    # TODO: replace with static method call from model
    filename = os.path.join('./', 'sample_data.json')
    with open(filename) as sample_data:
        data = json.load(sample_data)

    print('Data from sample file:\n')
    print(data)

    return jsonify(data)
    