from flask import Flask, request
from pprint import pprint
from main import flight_validation
from date_format import dict_to_date

app = Flask(__name__)

@app.route('/')
def hello():
    return "welcome to flight validation"

@app.route('/check', methods=['POST'])
def main():
    data = request.get_json(force=True)
    pprint(data)
    session_info = data['sessionInfo']
    session_name = data.get('sessionInfo').get('session')

    parameters = session_info['parameters']
    trip_type = parameters['triptype']
    
    # Common parameters for both one-way and round-trip
    from_city = parameters.get('origin-city', '') if parameters.get('origin-city') else parameters.get('origin-city2', '')
    to_city = parameters.get('destination-city', '') if parameters.get('destination-city') else parameters.get('destination-city2', '')
    session_id = parameters.get('session_id', '')
    unique_no = parameters.get('unique_no', '')
    group_ind = parameters.get('group_ind', '')
    adults = parameters.get('adults', '')
    children = parameters.get('children', '')
    infants = parameters.get('infants', '')
    cabin_class = parameters.get('travel-class', '')
    currency = "NGN"
    
    # One-way specific parameters
    if trip_type == 'S':
        flight_id = parameters.get('flight_id', '')
        flight_number = parameters.get('flight_number', '')
        departure_date = dict_to_date(parameters.get('departure-date', ''))
        returndate = None
    
    # Round-trip specific parameters
    elif trip_type == 'R':
        flight_id = parameters.get('re_flight_id', '')
        flight_number = parameters.get('re_flight_number', '')
        departure_date = dict_to_date(parameters.get('departure-date', ''))
        returndate = dict_to_date(parameters.get('returndate', ''))
        print(returndate)
    
    else:
        return {"error": "Invalid trip type"}, 400

    result = flight_validation(group_ind, unique_no, flight_id, trip_type, from_city, to_city, departure_date, returndate, adults, children, infants, cabin_class, currency, session_id)

    if result['message'] == "Selected Flight Booking is available":
        response = {
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"Good news! Seats are available for flight {flight_number[0]}. Simply fill out the form to continue with your booking!"
                            ]
                        }
                    }
                ]
            },
            "session_info": {
                "session": session_name
            },
            "target_page": "projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/a2735fbd-0179-49a4-99e8-30577c9ccf93/pages/930aeb34-c905-442c-b672-22f96dd0deaf"
        }
        return response
    else:
        no_seats = {
            "fulfillmentResponse": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"Oops! It looks like there are no available seats on flight {flight_number[0]} at the moment. Don't worry though, you can explore other flight options that might suit your schedule!"
                            ]
                        }
                    }
                ]
            },
            "session_info": {
                "session": session_name,
            },
            "target_page": "projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/a2735fbd-0179-49a4-99e8-30577c9ccf93/pages/3b348fb4-e397-4cc0-8b09-52bb5e8283da"
        }
        return no_seats

if __name__ == "__main__":
    app.run(debug=True, port=4500)