from flask import Flask,request
from pprint import pprint
# from return_function import fetch_flight_result
from demo import fetch_flight_result
from date_format import dict_to_date
from flight_date import flightdate

app=Flask(__name__)


@app.route('/')
def hello():
    return "this is to collect user request"

@app.route('/oneway',methods=['POST'])
def search_flight():
    data=request.get_json(force=True)
    pprint(data)
    sessioninfo=data['sessionInfo']
    parameters=sessioninfo['parameters']
    trip_type=parameters['triptype']
    from_city=parameters.get('origin-city','')if parameters.get('origin-city')else parameters.get('origin-city2','')
    to_city=parameters.get('destination-city')if parameters.get('destination-city')else parameters.get('destination-city2','')
    return_date=parameters.get('returndate','')
    if return_date:
        return_date=dict_to_date(parameters.get('returndate',''))

    depart_date=dict_to_date(parameters.get('departure-date',''))
    print(f'depart date is {depart_date}')
    
    ddate=flightdate(depart_date)
    cabin_class=parameters.get('travel-class','')
    print(f"this is cabin class,{cabin_class}")
    infants=parameters.get('infants','')
    children=parameters.get('children','')
    adults=parameters.get('adults','')
    print(f"this is person details:,{infants}, {children}, {adults}")
    currency="NGN"

    # result=fetch_flight_result()
    result=fetch_flight_result(trip_type,from_city,to_city,depart_date,return_date,adults,children,infants,cabin_class,currency)
    pprint(f'this is flight show{result}')


    # for flight in result:
    #     flight 
        

    if not result:
        noflights={
            "fulfillmentResponse":{
                "messages":[
                    {
                        "text":{
                            "text":[
                                f"sorry we couldn't find any flights between {from_city} to {to_city} for {depart_date}. come back later"
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
                                                    "command":"search for another date",
                                                    "type":"training"
                                                }
                                            },
                                            "title":"search for another date"
                                        },
                                        {
                                            "action":{
                                                "message":{
                                                    "command":"No Thanks",
                                                    "type":"training"
                                                }
                                            },
                                            "title":"No Thanks"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return noflights
    
    if result:
        if trip_type=='R':
            roundflights={
                "fulfillment_response":{
                    "messages":[
                        {
                            "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                            "channel":"",

                            "payload":{
                                "botcopy":[
                                    {
                                        "carousel":[
                                            {
                                                "subtitle":f"Stop {i['stops']} | {i['duration']}",
                                                "action":{
                                                    "message":{
                                                        "type":"training",
                                                        "command":"Get more details",
                                                        "parameters":{
                                                            "airlinename":i["airline_name"],
                                                            "departure_time":i["departure_time"],
                                                            "arrival_time":i["arrival_time"],
                                                            "total_fare":i["total_fare"],
                                                            "cabin_type":i["cabin_type"],
                                                            "stops":i['stops'],
                                                            "flight_number":i["flight_number"],
                                                            "departure_airport":i["departure_airport"],
                                                            "arrival_airport":i["arrival_airport"],
                                                            "stopsbreakdown":i['stopsbreakdown'],
                                                            # "sessionId":i["session_id"],
                                                            "uniqueRefno":i['unique_no'],
                                                            "groupIND":i['group_ind'],
                                                            'returnduration':i['re_duration'],
                                                            'returnairline':i['re_airline_name'],
                                                            'returndepartureAirport':i['return_departure'],
                                                            'returnarrivalAirport':i['return_arrival'],
                                                            'returnTotalFare':i['re_total_fare'],
                                                            'returnStops':i['re_stops'],
                                                            'returnArrivaltime':i['re_arrival_time'],
                                                            'returnDeparturetime':i['re_departure_time'],
                                                            'returnstopsbreakdown': i["returnstopsbreakdown"],
                                                            're_airline_image':i['re_airline_image']

                                                        }
                                                    }
                                                },
                                                "body":f'''{i['departure_location'][0]} To {i['arrival_location'][-1]} \n Departure: {i['departure_time'][0]}\n↓\nArrival: {i['arrival_time'][0]}''',
                                                "title":f" {i['airline_name'][0]} |₦ {i['total_fare']:,}",
                                                "image":{
                                                    "url":f"{i['airline_image'][0]}",
                                                    "alt":"Image of an airplane"
                                                }
                                            }for i in result
                                        ]
                                    }
                                ]
                            }
                        },
                        {
                            "text":{
                                "text":[
                                    f"want to know more? click on your desired option to get more details"
                                ]
                            }
                        }
                    ],
                    "mergeBehavior":"APPEND"
                }
            }
            return roundflights
        
        else:
            onewayflights={
                "fulfillment_response":{
                    "messages":[
                        {
                            "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                            "channel":"",

                            "payload":{
                                "botcopy":[
                                    {
                                        "carousel":[
                                            {
                                                "subtitle":f"Stop {i['stops']} | {i['duration']}",
                                                "action":{
                                                    "message":{
                                                        "type":"training",
                                                        "command":"Get more details",
                                                        "parameters":{
                                                            "airline_name":i['airline_name'][0],
                                                            "departure_time":i['departure_time'],
                                                            "arrival_time":i['arrival_time'],
                                                            "total_fare":i['total_fare'],
                                                            "departure_airport":i["departure_airport"],
                                                            "arrival_airport":i["arrival_airport"],
                                                            "cabin_text":i['cabin_type'],
                                                            "duration":i['duration'],
                                                            "stopsbreakdown":i['stopsbreakdown'],
                                                            "stops":i['stops'],
                                                            "flight_number":i['flight_number'],
                                                            # "session_id":i['session_id'],
                                                            "unique_no":i['unique_no'],
                                                            "group_Ind":i['group_ind']
                                                        }
                                                    }
                                                },
                                                "body":f"""{i['departure_location'][0]} To {i['arrival_location'][-1]}\nDeparture: {i['departure_time'][0]}\n↓\nArrival: {i['arrival_time'][-1]}""",
                                                "title":f"{i['airline_name'][0]} | ₦-{i['total_fare']}",
                                                "image":{
                                                    "url":f"{i['airline_image'][0]}",
                                                    "alt":"Image of an airplane"
                                                }
                                            }for i in result
                                        ]
                                    }
                                ]
                            }
                        },
                        {
                            "text":{
                                "text":[
                                    f"want to know more? click on your desired option to get more details"
                                ]
                            }
                        }
                    ],
                    "mergeBehavior":"APPEND"
                }
            }
            return onewayflights
    


   # return result

if __name__=="__main__":
    app.run(debug=True,port=4000)    