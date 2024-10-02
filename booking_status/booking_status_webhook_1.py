from flask import Flask,request,jsonify
from pprint import pprint
from function_1 import book_flight
from names import namedivider


app=Flask(__name__)


@app.route('/')
def hello():
    return "welcome to booking status"
    
@app.route('/status',methods=["POST"])
def webhook():
    data=request.get_json(force=True)
    seesion_info=data['sessionInfo']
    parameters=seesion_info['parameters']
    access_token=parameters["access_token"]
    adultDOB=parameters["adult_dob_1"]
    adultPPNo=parameters["adult_id_number_1"]
    adultId_type=parameters["adult_id_type_1"]
    adultTitle=parameters["adult_title_1"]
    adults=int(parameters["adults"])
    airline_image=parameters.get("airline_image",[])
    airline_name=parameters.get("airline_name",[])
    from_city=parameters.get('origin-city','')if parameters.get('origin-city')else parameters.get('origin-city2','')
    to_city=parameters.get('destination-city')if parameters.get('destination-city')else parameters.get('destination-city2','')
    departdate=parameters.get("departure_time",[])
    returndate=parameters.get("returndate",[])
    childs=int(parameters.get("children",""))
    infants=int(parameters.get("infants",""))
    cabinClass=parameters.get("travel-class","")
    currency="NGN" 
    trip_type=parameters['triptype']
    flight_id=parameters['flight_id']
    flight_number=parameters['flight_number']
    group_ind=parameters['group_ind']
    session_id=parameters.get("session_id")
    unique_ref_no=parameters.get("unique_no")
    payment_method="flutterwave"
    # search=search_data
    adultEmail=parameters.get("email")
    adultMobile=parameters['mobile']
    childTitle=parameters.get("","")
    childFName=parameters.get("","")
    childLName=parameters.get("","")
    childDOB=parameters.get("","")
    childId_type=parameters.get("")
    childPPNo=parameters.get("","")
    infantTitle=parameters.get("","")
    infantFName=parameters.get("","")
    infantLName=parameters.get("","")
    infantDOB=parameters.get("","")
    infantId_type=parameters.get("","")
    infantPPNo=parameters.get("","")

    adult_fullname=parameters["adult_fullname_1"]
    fullnames=[]
    for i in range(adults):
        fullnames.append(parameters[f"adult_fullname_{i+1}"])
    print(fullnames)
    child_fullnames=[]
    for i in range(childs):
        child_fullnames.append(parameters[f"child_fullname_{i+1}"])
    print(child_fullnames)

    infant_fullnames=[]
    for i in range(infants):
        infant_fullnames.append(parameters.get(f"infant_fullname_{i+1}"))


    adultFName=[]
    adultLName=[]
    for i in fullnames:
        fname, lname= namedivider(i)
        adultFName.append(fname)
        adultLName.append(lname)
    childFname=[]
    childLname=[]
    for i in child_fullnames:
        fname, lname=namedivider(i)
        childFname.append(fname)
        childLname.append(lname)
    ifname=[]
    ilname=[]
    for i in infant_fullnames:
        fname, lname=namedivider(i)
        ifname.append(fname)
        ilname.append(lname)


    search_data = [
        {
            "tripType": trip_type,
            "fromCity": from_city,
            "toCity": to_city,
            "departDate": departdate,
            "returnDate": returndate,
            "adults": adults,
            "childs": childs,
            "infants": infants,
            "cabinClass": cabinClass,
            "currency": currency,
            "unique_ref_no": unique_ref_no
        }
    ]





# book_flight(flight_t_id, session_id, unique_ref_no, groupInd, payment_method, search, 
#                 adultTitle, adultFName, adultLName, adultDOB, adultId_type, adultPPNo, 
#                 adultEmail, adultMobile, 
#                 childTitle, childFName, childLName, childDOB, childId_type, childPPNo,  
#                 infantTitle, infantFName, infantLName, infantDOB, infantId_type,infantPPNo):
    result=book_flight(flight_id,session_id,unique_ref_no,group_ind,payment_method,adultTitle,
                       adultFName,adultLName,adultDOB,adultId_type,adultPPNo,
                       adultEmail,adultMobile,
                       childTitle,childFName,childLName,childDOB,childId_type,childPPNo,
                       infantTitle,infantFName,infantLName,infantDOB,infantId_type,infantPPNo,search_data)
    
    # pprint(result)

    if result["message"]=="Booking initialized successfully.":
        response={
            "fulfillmentResponse":{
                "messages":[
                    {
                        "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                        "channel":"",

                        "payload":{
                            "botcopy":[
                                {
                                    "card":{
                                        "action":{
                                            "buttons":[
                                                {
                                                    "action":{
                                                        "message":{
                                                            "command":"Make the payment",
                                                            "type":"training",
                                                        }
                                                    },
                                                    "title":"Make Payment"
                                                }
                                            ]
                                        },
                                        "body":f"""{'message'}|\n{'created_at'}""",
                                        "image":{
                                            "alt":"Image of airline",
                                            "ulr":airline_image
                                        },
                                        "subtitle":f"{'booking_id'}|{'payment_type'}",
                                        "title":f"{'currency'}|{'amount'}"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return response
    else:
        response_1={
            "fulfillment_Response":{
                "messages":[
                    {
                        "text":{
                            "text":[
                                f"booking failed"
                            ]
                        }
                    }
                ]
            }
        }
        return response_1
    

    
    


















    unique_ref_no=parameters.get("unique_no","")



    pprint(data)

    #Extract necessary details


    #Preprocessing for fname and lname


    #Preprocessing for DOB


    #Try the API call without PPNo, PPEd, PPINationality,


    #When all necessary details are there, make the function call


    # if -else 
    # IF message=="Booking initiated successfully"
    # Return card 
    # Else :
    # return "Failed message"

    return data






if __name__=="__main__":
    app.run(debug=True,port=9000)

