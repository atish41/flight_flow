from flask import Flask,request
from pprint import pprint
from main import flight_validation
# from revalidate import revalidate_flight
# from round_revalidate_1 import revalidate_flight
from date_format import dict_to_date
from pprint import pprint


app=Flask(__name__)

@app.route('/')
def hello():
    return "welcome to flight validation"

@app.route('/check',methods=['POST'])
def main():
    data=request.get_json(force=True)
    pprint(data)
    session_info=data['sessionInfo']
    session_name = data.get('sessionInfo').get('session')

    parameters=session_info['parameters']
    trip_type=parameters['triptype']
    from_city=parameters.get('origin-city','')if parameters.get('origin-city')else parameters.get('origin-city2','')
    to_city=parameters.get('destination-city','')if parameters.get('destination-city')else parameters.get('destination-city2','')
    session_id=parameters.get('session_id','')
    print(f"this is session Id{session_id}")
    unique_no=parameters.get('unique_no')or parameters.get('uniqueRefno','')
    print(f'this is unique n o{unique_no}')
    flight_id=int(parameters.get('flight_id',))
    print(type(flight_id))
    flight_number=parameters.get('flight_number','')
    group_ind=int(parameters.get('group_ind',''))
    print(type(group_ind))
    infants=parameters.get('infants','')
    returndate=dict_to_date(parameters.get('returndate',''))
    print(returndate)
    print(type(returndate))
    children=parameters.get('children','')
    departure_date=dict_to_date(parameters.get('departure-date',''))
    print(departure_date)
    adults=parameters.get('adults','')
    cabin_class=parameters.get('travel-class','')
    currency="NGN"
    access_token=parameters.get('access_token','')
    api="sabre"


    # result=flight_validation(group_ind,unique_ref_no,flight_id,trip_type,from_city,to_city,depart_date,return_date,adults,children,infants,cabin_class,currency,session_id)

    result=flight_validation(group_ind,unique_no,flight_id,trip_type,from_city,to_city,departure_date,returndate,adults,children,infants,cabin_class,currency,session_id)
    print(f"this is from webhook{result}")


    
    if result['message']=="Selected Flight Booking is available":
        response={
            "fulfillment_response":{
                "messages":[
                    {
                        "text":{
                            "text":[
                                f"Good news! Seats are available for flight {flight_number[0]}. Simply fill out the form to continue with your booking!"
                            ]
                        }
                    }
                ]
            },
            "session_info":{
                "session":session_name
            },
            "target_page":"projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/a2735fbd-0179-49a4-99e8-30577c9ccf93/pages/930aeb34-c905-442c-b672-22f96dd0deaf"
        }
        return response
    
    else:
        no_seats={
            "fulfillmentResponse":{
                "messages":[
                    {
                        "text":{
                            "text":[
                                f"Oops! It looks like there are no available seats on flight {flight_number[0]} at the moment. Don't worry though, you can explore other flight options that might suit your schedule!"
                            ]
                        }
                    },
                    # {
                    #     "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                    #     "channel":"",

                    #     "payload":{
                    #         "botcopy":[
                    #             {
                    #                 "suggestions":[
                    #                     {
                    #                         "action":{
                    #                             "messgae":{
                    #                                 "command":"search for another flight", 
                    #                                 "type":"training"
                    #                             }
                    #                         },
                    #                         "title":"search for another flight"
                    #                     },
                    #                     {
                    #                         "action":{
                    #                             "message":{
                    #                                 "command":"No Thanks",
                    #                                 "type":"training"
                    #                             }
                    #                         },
                    #                         "title":"No Thanks"
                    #                     }
                    #                 ]
                    #             }
                    #         ]
                    #     }
                    # }
                ]
            },
            "session_info":{
                "session":session_name,

            },
            "target_page":"projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/a2735fbd-0179-49a4-99e8-30577c9ccf93/pages/3b348fb4-e397-4cc0-8b09-52bb5e8283da"
        }
        return no_seats




    




if __name__=="__main__":
    app.run(debug=True,port=4500)

