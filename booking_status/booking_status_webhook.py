from flask import Flask,request,jsonify
from pprint import pprint

app=Flask(__name__)


@app.route('/')
def hello():
    return "welcome to booking status"
    
@app.route('/status',methods=["POST"])
def webhook():
    data=request.get_json(force=True)
    pprint(data)


    return data






if __name__=="__main__":
    app.run(debug=True,port=9000)

