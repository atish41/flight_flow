from flask import Flask,request
from pprint import pprint
from stopsprinter import stopsprinter   
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

    flight_number=parameters.get('flight_number','')
    uniqueRefno=parameters.get('uniqueRefno','')
    groupIND=parameters.get('groupIND','')
    departure_airport=parameters.get('departure_airport','')
    arrival_airport=parameters.get('arrival_airport','')

    def create_flight_body(from_city, to_city, departure_airport, departure_time, arrival_airport, arrival_time, stopsbreakdown, stops):
        body_content = f'''Flight to {to_city}\n⋯\n🟢{departure_airport[0]} | {departure_time[0]}\n'''
        
        if int(stops) > 0:
            body_content += f'↓\n{stopsprinter(stopsbreakdown, stops)}\n↓\n'
        else:
            body_content += '↓\n'
        
        body_content += f'🔴{arrival_airport[-1]} | {arrival_time[-1]}'
        return body_content
    

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

        outbound_body = create_flight_body(from_city, to_city, departure_airport, departure_time, arrival_airport, arrival_time, stopsbreakdown, stops)
        inbound_body = create_flight_body(to_city, from_city, returndepartureAirport, returnDeparturetime, returnarrivalAirport, returnArrivaltime, returnstopsbreakdown, returnStops)

        full_body = f'''{outbound_body}\n⇅\n{inbound_body}'''


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
                                        "body":full_body,
                                        
                                        "image":{
                                            "alt":"Image of airline",
                                            "url":airline_image
                                        },
                                        "subtitle":f"{total_fare}",

                                        "title":f"{airline_name} |{cabin_type}"
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
                                            "title":"would you like to choose a different option"
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
        body_content = create_flight_body(from_city, to_city, departure_airport, departure_time, arrival_airport, arrival_time, stopsbreakdown, stops)

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
                                        "body":body_content,

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
                                            "title":"would you like to choose another option",
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
    
