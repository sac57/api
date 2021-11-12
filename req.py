# import requests,json

# response = requests.get('http://127.0.0.1:5001/addage?age=50,30')
# print("Sum of ages: ",response.json())
# resp = requests.get('http://127.0.0.1:5003/sumby2?add={response.json()}')
# print("Divided by 2 ",resp.json())
from flask import Flask, request, jsonify
import json

app =  Flask(__name__)

def category(bmi):
    result = {}
    if bmi < 18.5:
        result['category'] = "Under Weight"
    elif bmi >= 18.5 and bmi <= 24.9:
        result['category'] = "Normal"
    elif bmi >= 25 and bmi <= 29.9:
        result['category'] = "Over Weight"
    elif bmi >= 30 and bmi <= 34.9:
        result['category'] = "Obese"
    else:
        result['category'] = "Extreme Obese"
    return(result)

@app.route('/score', methods=['POST'])
def bmiCategory():
    input = request.get_json()
    bmi = input['bmi']
    CategoryResult = category(bmi)
    dump = CategoryResult["category"]
    return(jsonify({"category":dump}))

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 5002, debug= True)