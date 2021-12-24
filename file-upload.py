from flask import Flask, json
#from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os
import urllib.request
#from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import csv
from flask_cors import cross_origin,CORS

app = Flask(__name__)
CORS(app)
#api = Api(app)


ALLOWED_EXTENSIONS = set(['csv', 'pdf', ])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)

		res=extract(filename)

		# resp = jsonify(res)
		# res.status_code = 201
		return res
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp


def extract(filename):
    # input_file = csv.DictReader(open(filename))
    # data = []
    # for i in input_file:
    #         data.append(i)
    # print(data)

    df = pd.read_csv(filename)

    dfnew = df.dropna(axis=0, how="all", thresh=None, subset=None, inplace=False)
    dfnew = dfnew.fillna(0)

    dfnew.rename(columns = {'Closing Balance':'ClosingBalance'}, inplace = True)
    dfnew.rename(columns = {'Withdrawal Amt.':'Withdrawal'}, inplace = True)
    dfnew.rename(columns = {'Deposit Amt.':'Deposit'}, inplace = True)
    # dfnew.rename(columns = {'Closing Balance':'ClosingBalance'}, inplace = True)
    # res = dfnew['Date']
    # res['Date'] = df['Date']
    res = dfnew.to_json(orient='records')


    # print(dfnew)
    # print(res)

    # credits=0
    # debits=0
    # balance=0
    # for i in data:
    #     if(len(i['Deposit Amt.'])>0):
    #         print(len(i['Deposit Amt.']))
    #         credits+=float(i["Deposit Amt."])
    #     if(len(i['Withdrawal Amt.'])>0):
    #         print(len(i['Withdrawal Amt.']))
    #         debits+=float(i["Withdrawal Amt."])

    # # balance=float(data[-1]["Closing Balance"])
    # print(credits)
    # print(debits)
    # # print(balance)
    # res["Deposit Amt."]=credits
    # res["Withdrawal Amt."]=debits
    # res["Closing Balance"]=balance

    return res

if __name__ == "__main__":
    app.run()