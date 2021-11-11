from flask import Flask,jsonify, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)

api = Api(app)

class body(Resource):

    def get(self,weight,height):
        bmi=weight/((height/100)**2)
        if bmi < 18:
            return jsonify({'Underweight=': bmi})
        elif bmi < 25:
            return jsonify({'Normal': bmi})
        else:
            return jsonify({'Overweight': bmi})

api.add_resource(body, '/body/<int:weight>/<int:height>')

if __name__=='__main__':
    app.run(debug = True,host='127.0.0.1',port=5000)