from flask import Flask, request, jsonify
from pprint import pprint
from function_1 import book_flight
from names import namedivider

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to booking status"

@app.route('/status', methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    session_info = data['sessionInfo']
    parameters = session_info['parameters']
    
    # Extract all necessary parameters
    adults = int(parameters["adults"])
    childs = int(parameters.get("children", "0"))
    infants = int(parameters.get("infants", "0"))
    from_city = parameters.get('origin-city') or parameters.get('origin-city2', '')
    to_city = parameters.get('destination-city') or parameters.get('destination-city2', '')
    departdate = parameters.get("departure_time", [])
    returndate = parameters.get("returndate", [])
    cabinClass = parameters.get("travel-class", "")
    trip_type = parameters['triptype']
    flight_id = parameters['flight_id']
    session_id = parameters.get("session_id")
    unique_ref_no = parameters.get("unique_no")
    group_ind = parameters['group_ind']

    # Create search_data
    search_data = [{
        "tripType": trip_type,
        "fromCity": from_city,
        "toCity": to_city,
        "departDate": departdate,
        "returnDate": returndate,
        "adults": str(adults),
        "childs": str(childs),
        "infants": str(infants),
        "cabinClass": cabinClass,
        "currency": "NGN",
        "unique_ref_no": unique_ref_no
    }]

    # Process passenger information
    adult_info = process_passenger_info(parameters, 'adult', adults)
    child_info = process_passenger_info(parameters, 'child', childs)
    infant_info = process_passenger_info(parameters, 'infant', infants)

    try:
        result = book_flight(
            flight_t_id=int(flight_id),
            session_id=session_id,
            unique_ref_no=unique_ref_no,
            groupInd=group_ind,
            payment_method="flutterwave",
            search=search_data,
            adultTitle=adult_info['adultTitle'],
            adultFName=adult_info['adultFName'],
            adultLName=adult_info['adultLName'],
            adultDOB=adult_info['adultDOB'],
            adultId_type=adult_info['adultId_type'],
            adultPPNo=adult_info['adultPPNo'],
            adultEmail=adult_info['adultEmail'],
            adultMobile=adult_info['adultMobile'],
            childTitle=child_info['childTitle'],
            childFName=child_info['childFName'],
            childLName=child_info['childLName'],
            childDOB=child_info['childDOB'],
            childId_type=child_info['childId_type'],
            childPPNo=child_info['childPPNo'],
            infantTitle=infant_info['infantTitle'],
            infantFName=infant_info['infantFName'],
            infantLName=infant_info['infantLName'],
            infantDOB=infant_info['infantDOB'],
            infantId_type=infant_info['infantId_type'],
            infantPPNo=infant_info['infantPPNo']
        )
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

        
        # Print the result
        print("Booking Result:")
        pprint(result)
        
        return jsonify(result), 200
    except Exception as e:
        error_message = f"Error occurred: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

def process_passenger_info(parameters, passenger_type, count):
    info = {
        f'{passenger_type}Title': [],
        f'{passenger_type}FName': [],
        f'{passenger_type}LName': [],
        f'{passenger_type}DOB': [],
        f'{passenger_type}Id_type': [],
        f'{passenger_type}PPNo': []
    }
    
    for i in range(count):
        fullname = parameters.get(f"{passenger_type}_fullname_{i+1}", "")
        fname, lname = namedivider(fullname)
        info[f'{passenger_type}FName'].append(fname)
        info[f'{passenger_type}LName'].append(lname)
        
        info[f'{passenger_type}Title'].append(parameters.get(f"{passenger_type}_title_{i+1}", ""))
        info[f'{passenger_type}DOB'].append(parameters.get(f"{passenger_type}_dob_{i+1}", ""))
        info[f'{passenger_type}Id_type'].append(parameters.get(f"{passenger_type}_id_type_{i+1}", ""))
        info[f'{passenger_type}PPNo'].append(parameters.get(f"{passenger_type}_id_number_{i+1}", ""))
    
    if passenger_type == 'adult':
        info['adultEmail'] = parameters.get("email", "")
        info['adultMobile'] = parameters.get("mobile", "")
    
    return info

if __name__ == "__main__":
    app.run(debug=True, port=9000)