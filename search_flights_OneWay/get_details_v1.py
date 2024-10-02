from flask import Flask,request
from pprint import pprint
from stopsprinter import stopsprinter   
import random
app=Flask(__name__)

@app.route('/')
def hello():
    return "this for get details"

@app.route('/get_flightdetails',methods=['POST'])
def get_details():
    data=request.get_json(force=True)
    pprint(data)
    sessionInfo=data['sessionInfo']
    parameters=sessionInfo['parameters']
    triptype=parameters['triptype']
    from_city=parameters.get('origin-city','')if parameters.get('origin-city')else parameters.get('origin-city2','')
    to_city=parameters.get('destination-city')if parameters.get('destination-city')else parameters.get('destination-city2','')
    airline_name=parameters.get('airline_name','')
    print(airline_name)
    airline_image=parameters.get('airline_image')
    print(airline_image)
    duration=parameters.get('duration','')
    departure_time=parameters.get('departure_time','')
    arrival_time=parameters.get('arrival_time','')
    total_fare=parameters.get('total_fare')
    cabin_type=parameters.get('cabin_type','')
    stops=parameters.get('stops','')
    stopsbreakdown=parameters['stopsbreakdown']
    print(stopsbreakdown)

    flight_number=parameters.get('flight_number','')
    uniqueRefno=parameters.get('uniqueRefno','')
    groupIND=parameters.get('groupIND','')
    departure_airport=parameters.get('departure_airport','')
    arrival_airport=parameters.get('arrival_airport','')
    another_options=["Want to pick a different option?","Would you prefer to select another choice?",
    "Ready to try a different option?","Looking to choose a new option?","Want to go with another choice?"]

    if triptype=="R":
        returnduration=parameters.get('returnduration','')
        returnairline=parameters.get('returnairline','')
        returndepartureAirport=parameters.get('returndepartureAirport','')
        returnarrivalAirport=parameters.get('returnarrivalAirport','')
        returnTotalFare=parameters.get('returnTotalFare','')
        returnStops=parameters.get('returnStops','')
        returnArrivaltime=parameters.get('returnArrivaltime','')
        returnDeparturetime=parameters.get('returnDeparturetime','')
        returnstopsbreakdown=parameters.get('returnstopsbreakdown')
        print(f"this is return stops {returnstopsbreakdown}")
        re_airline_image=parameters.get('re_airline_image','')


        re_response={
            "fulfillmentResponse":{
                "messages":[
                    {
                        "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                        "channel":"",

                        #union field message can be following
                        "payload":{
                            "botcopy":[
                                {
                                    "card":{
                                        "action":{
                                            "buttons":[
                                                {
                                                    "action":{
                                                        "message":{
                                                            "command":"Book Now",
                                                            "type":"training",
                                                        }
                                                    },
                                                    "title":"Book Now"
                                                }
                                            ]
                                        },
                                        "body":f'''Flight to {to_city}\n⋯\n🟢{departure_airport[0]} | {departure_time[0]}\n↓\n
{stopsprinter(stopsbreakdown,stops)}\n↓\n
🔴{arrival_airport[-1]} | {arrival_time[-1]}\n⇅\n
Flight to {from_city}\n⋮\n
origin:🟢{returndepartureAirport[0]} | Departure:{returnDeparturetime[0]}\n↓\n
{stopsprinter(returnstopsbreakdown,returnStops)}\n↓\n
Destination:🔴{returnarrivalAirport[-1]} | Arrival: {returnArrivaltime[-1]}''',
                                        "image":{
                                            "alt":"Image of airline",
                                            "url":re_airline_image[0]
                                        },
                                        "subtitle":f"{total_fare}",

                                        "title":f"""{returnairline[0]} |{cabin_type[0]}"""
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                        "channel":"",
                        "payload":{
                            "botcopy":[
                                {
                                    "suggestions":[
                                        {
                                            "action":{
                                                "message":{
                                                    "command":"I would like to book another option",
                                                    "type":"training"
                                                }
                                            },
                                            "title":random.choice(another_options)
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return re_response
    
    else:
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
                                                            "command":"Book Now",
                                                            "type":"training"
                                                        }
                                                    },
                                                    "title":"Book Now"
                                                }
                                            ]
                                        },
                                        "body":f'''Flight to {to_city}\n⋯\n🟢{departure_airport[0]} | {departure_time[0]}\n↓\n
{stopsprinter(stopsbreakdown,stops)or "No Stops"}\n↓\n
🔴{arrival_airport[-1]} | {arrival_time[-1]} ''',

                                        "image":{
                                            "alt":"image of plane",
                                            "url":airline_image[0]
                                        },
                                        "subtitle":f"{duration}",
                                        
                                        "title":f"{airline_name[0]}| ₦{total_fare}"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                        "channel":"",
                        "payload":{
                            "botcopy":[
                                {
                                    "suggestions":[
                                        {
                                            "action":{
                                                "message":{
                                                    "command":"I would like to choose another option",
                                                    "type":"training"
                                                }
                                            },
                                            "title":random.choice(another_options),
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return response
    
if __name__=="__main__":
    app.run(debug=True,port=3000)
    
