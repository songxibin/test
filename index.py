#!/usr/bin/env python

from flask import Flask, request, jsonify
from waitress import serve
from sklearn.externals import joblib
import json
import os
app = Flask(__name__)


class Event:

    def __init__(self):
        self.body = request.get_data()
        self.headers = request.headers
        self.method = request.method
        self.args = request.args
        self.path = request.path
        self.model = joblib.load('IrisClassifier.sav')




def format_status_code(resp):
    return 200


def format_body(resp):
    mydict = {}
    dict = {}
    mydict["names"]=[]
    mydict["ndarray"]=resp.tolist()
    dict["data"]=mydict
    j=json.dumps(dict)
    return str(j)


def format_headers(resp):
    if 'headers' not in resp:
        return []
    elif type(resp['headers']) == dict:
        headers = []
        for key in resp['headers'].keys():
            header_tuple = (key, resp['headers'][key])
            headers.append(header_tuple)
        return headers

    return resp['headers']


def format_response(resp):
    statusCode = format_status_code(resp)
    body = format_body(resp)
    headers = format_headers(resp)
    return (body, statusCode, headers)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def call_handler(path):
    event = Event()
    jsons=request.args.get('json')
    if jsons==None:
        jsons=request.form.get('json')
    if jsons==None:
        jsons=json.dumps(request.json)
    print(jsons)
    dataDict = json.loads(jsons)
    print(type(dataDict))
    data=dataDict['data']
    print(data)
    print(type(data))
    iris_x = data['ndarray']
    print(iris_x[0])
    response_data = event.model.predict_proba(iris_x)
    print(response_data)
    res=format_response(response_data)
    return res


if __name__ == '__main__':
    ports=os.getenv('PREDICTIVE_UNIT_SERVICE_PORT','5000')
    serve(app, host='0.0.0.0', port=ports)
