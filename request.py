import requests
import json

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
r=requests.post(url,json={"LIMIT_BAL":4,
                          "MARRIAGE":1,
                          "EDUCATION":1,
                          "SEX":2,
                          "AGE":35,
                          "PAY_1":1,
                          "PAY_2":2,
                          "PAY_3":0,
                          "BILL_AMT1":3372,
                          "BILL_AMT2":2948,
                          "BILL_AMT3":3372,
                          "PAY_AMT1":1500,
                          "PAY_AMT2":1500,
                          "PAY_AMT3":1200})
print(r.json())