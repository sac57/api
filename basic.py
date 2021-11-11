from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/hello',methods=['GET'])
def world():
    if(request.method=='GET'):
        data={"data":"hello"}
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)