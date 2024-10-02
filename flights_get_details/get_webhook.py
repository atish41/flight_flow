from flask import Flask,request
from pprint import pprint

app=Flask(__name__)



@app.route('/')
def hello():
    return "this for get details"


def get_details():
    data=request.get_json(force=True)
    sessionInfo=data['sessionInfo']
    parameters=sessionInfo['parameters']
    triptype=parameters['']




if __name__=='__main__':
    app.run(debug=True,port=9000)