# from flask import Flask,jsonify, request
# from flask_restful import Resource, Api
# import json
# app = Flask(__name__)

# api = Api(app)
# @app.route('/addage',methods=['GET'])
# def addage():
#      age=(request.args["age"])
#      a=age.split(',')
#      sum=int(a[0])+int(a[1])
#      return jsonify(int(sum))
# if __name__=='__main__':
#     app.run(debug = True,host='127.0.0.1',port=5001)
from flask import Flask, request, jsonify
import json, requests
app =  Flask(__name__)

def conversion(weight,heights):
    result = {}
    weightInKG = weight / 1000      # weight * .001
    heightInMeter = heights * 0.31
    result['weight'] = weightInKG
    result['height'] = heightInMeter
    return(result)

@app.route('/conversion', methods=['POST'])
def bmiConversion():
    input = request.get_json()
    weight = input['weight']
    height = input['height']
    name = input['name']
    ConversionResult = conversion(weight,height)
    url = "http://0.0.0.0:"
    port1 = 5001
    payload = json.dumps({
        "weight": ConversionResult["weight"],
        "height": ConversionResult["height"]
    })
    print(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url+str(port1)+"/bmi", headers=headers, data=payload)
    next_response = json.loads(response.text)
    return(jsonify({"result": str(name) + " you are " + str(next_response["category"])}))

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 5000, debug= True)