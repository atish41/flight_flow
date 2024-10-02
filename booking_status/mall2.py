from flask import Flask, request, jsonify
from pprint import pprint
from function_1 import book_flight
from names import namedivider
from date_format import dict_to_date
# from person_details import process_passenger_info
from person_info import process_passenger_info
from gender_function import get_gender_from_title
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to booking status"

@app.route('/status', methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        pprint(data)
        session_info = data['sessionInfo']
        parameters = session_info['parameters']
        # pprint(parameters)
        
        # Extract all necessary parameters
        # Extract all necessary parameters
        adults = int(parameters["adults"])
        childs = int(parameters.get("children", "0"))
        infants = int(parameters.get("infants", "0"))
        from_city = parameters.get('origin-city', '')
        # print(f'this from city{from_city}-and type is ')
        # print(type(from_city))
        to_city = parameters.get('destination-city2', '')
        # print(f'this to city{to_city}')
        # print(type(to_city))
        departdate = dict_to_date(parameters.get("departure-date", {}))
        # print(f'this is deaparture date:{departdate}')
        # print(type(departdate))
        returndate = parameters.get("returndate", "")
        # print(f'this is return date:{returndate}')
        # print(type(returndate))
        cabinClass = parameters.get("travel-class", "")
        print(f'this is cabin-{cabinClass}')
        print(type(cabinClass))
        trip_type = parameters['triptype']
        print(f'this is trip type-{trip_type}')
        print(type(trip_type))

        flight_id = str(int(parameters['flight_id']))
        print(f'flightid--{flight_id}')
        print(type(flight_id))
        session_id = parameters.get("session_id", "")
        print(f'this session_id-{session_id}')
        print(type(session_id))
        unique_ref_no = parameters.get("unique_no")or parameters.get('uniqueRefno','')
        print(f'this is unique strating-{unique_ref_no}')
        print(type(unique_ref_no))
        group_ind = str(int(parameters['group_ind']))
        print(f'geuoup ind-{group_ind}')
        print(type(group_ind))
        airline_image = parameters.get("airline_image")[0] or parameters.get('re_airline_image','')[0]
        print(f'airline imagess-{airline_image}')
        # print(type(airline_image))

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
        title=adult_info['adultTitle']
        gender=get_gender_from_title(title)
        print(f'this is gender from title {gender}')
        print(type(gender))
        print(f"this is details{adult_info}-{child_info}- {infant_info}")

        result = book_flight(
            flight_t_id=flight_id,
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
        print("Booking Result:")
        pprint(f'this is webhookl result{result}')

        if result.get("message") == "Booking initialized successfully.":
            response = {
                "fulfillmentResponse": {
                    "messages": [
                        {
                            "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                            "channel": "",
                            "payload": {
                                "botcopy": [
                                    {
                                        "card": {
                                            "action": {
                                                "buttons": [
                                                    {
                                                        "action": {
                                                            "link": {
                                                                "target": "_blank",
                                                                "url": f"{result.get('payment_link','')}",
                                                            }
                                                        },
                                                        "title": "Make Payment"
                                                    }
                                                ]
                                            },
                                            "body": f"{result.get('message', '')}\n{result.get('created_at', '')}",
                                            "image": {
                                                "alt": "Image of airline",
                                                "url": airline_image
                                            },
                                            "subtitle": f"Booking ID-{result.get('booking_id', '')} | {result.get('payment_type', '')}",
                                            "title": f"{result.get('currnency', '')}| ₦ {result.get('amount', '')}"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        else:
            response = {
                "fulfillmentResponse": {
                    "messages": [
                        {
                            "text": {
                                "text": [
                                    f"Booking failed: {result.get('message', 'Unknown error')}"
                                ]
                            }
                        }
                    ]
                }
            }

        return jsonify(response), 200

    except Exception as e:
        error_message = f"Error occurred: {str(e)}"
        print(error_message)
        return jsonify({
            "fulfillmentResponse": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"An error occurred while processing your request: {error_message}"
                            ]
                        }
                    }
                ]
            }
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=9000)