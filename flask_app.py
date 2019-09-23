# A very simple Flask Hello World app for you to get started with...

import numpy as np
from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# Load the model
model = joblib.load(open('/home/afifahnrswr11/mysite/Model_RF.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    pred = []

    for data in datas:
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([np.array([data['LIMIT_BAL'],data['MARRIAGE'],data['EDUCATION'],data['SEX'],data['AGE'],data['PAY_1'],data['PAY_2'],data['PAY_3'],data['BILL_AMT1'],data['BILL_AMT2'],data['BILL_AMT3'],data['PAY_AMT1'],data['PAY_AMT2'],data['PAY_AMT3']])])

        # Take the first value of prediction
        output = float(prediction[0])
        out = 'Terlamnbat' if output==1 else 'Tidak Terlambat'
        pred.append(out)
    return jsonify(pred)
