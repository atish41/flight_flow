import requests
from pprint import pprint
from datetime import datetime

# Function to format timestamps, handling lists and single items
def format_timestamp(timestamps):
    if isinstance(timestamps, list):
        return [datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S").strftime("%b %d, %Y at %I:%M %p") for ts in timestamps]
    else:
        dt_object = datetime.strptime(timestamps, "%Y-%m-%dT%H:%M:%S")
        return dt_object.strftime("%b %d, %Y at %I:%M %p")

# Function to convert total flight duration from minutes to a human-readable format, handling lists and single items
def convert_minutes_to_readable_format(total_duration):
    def format_duration(minutes):
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if hours:
            return f"{hours}hr and {remaining_minutes}min"
        else:
            return f"{remaining_minutes} minutes"
    
    if isinstance(total_duration, list):
        return [format_duration(duration) for duration in total_duration]
    else:
        return format_duration(total_duration)

# Function to fetch flight results from the API
def fetch_flight_result(trip_type, from_city, to_city, depart_date, return_date, adults, children, infants, cabin_class, currency):
    
    url = "https://goagentgomarket.vgtechdemo.com/api/search-flights"

    payload = {
        "trip_type": trip_type,
        "from_city": from_city,
        "to_city": to_city,
        "depart_date": depart_date,
        "return_date": return_date,
        "adults": adults,
        "children": children,
        "infants": infants,
        "cabin_class": cabin_class,
        "currency": currency
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    response = response.json()

    top_flights = response.get('data', [])[:5]  # Top 5 flights
    
    flight_results = []

    for entry in top_flights:
        if 'onewaydata' in entry:
            for item in entry['onewaydata']:
                flight_details = {
                    'arrival_airport': item.get("Arrival_LocationText", ''),
                    'departure_airport': item.get('Departure_LocationText', ''),
                    'airline_name': [item.get('OperatingAirline_Text', '')],  # List for multiple airlines
                    'airline_image': [item.get('OperatingAirline_Image', '')],  # List for multiple airline images
                    'arrival_time': format_timestamp(item.get('arrival_date_time', '')),  # Handle multiple times
                    'departure_time': format_timestamp(item.get('departure_date_time', '')),  # Handle multiple times
                    'total_fare': item.get('total_fare', ''),
                    'trip_type': item.get('trip_type', ''),
                    'unique_no': item.get('unique_ref_no', ''),
                    'cabin_type': item.get('Cabin_Text', ''),
                    'stops': item.get('stops', ''),
                    'flight_number': [item.get('flight_number', '')],  # List for multiple flight numbers
                    'group_ind': item.get('group_ind', ''),
                    'duration': convert_minutes_to_readable_format(item.get('total_duration', '')),  # Handle multiple durations
                    'arrival_location': item.get('arrival_location_code', ''),
                    'departure_location': item.get('departure_location_code', '')
                }

                # Handle return data if available
                if 'returndata' in item:
                    for return_data in item['returndata'][0]:
                        return_flight_details = {
                            'return_arrival': return_data.get('Arrival_LocationText', ''),
                            'return_departure': return_data.get('Departure_LocationText', ''),
                            're_airline_name': [return_data.get('OperatingAirline_Text', '')],  # List for return airlines
                            're_airline_image': [return_data.get('OperatingAirline_Image', '')],  # List for return airline images
                            're_arrival_time': format_timestamp(return_data.get('arrival_date_time', '')),  # Handle multiple times
                            're_departure_time': format_timestamp(return_data.get('departure_date_time', '')),  # Handle multiple times
                            're_stops': return_data.get('stops', ''),
                            're_total_fare': return_data.get('total_fare', ''),
                            're_trip_type': return_data.get('trip_type', ''),
                            're_unique_no': return_data.get('unique_ref_no', ''),
                            're_duration': convert_minutes_to_readable_format(return_data.get('total_duration', '')),  # Handle multiple durations
                            're_arrival_location': return_data.get('arrival_location_code', ''),
                            're_departure_location': return_data.get('departure_location_code', '')
                        }
                        flight_details.update(return_flight_details)

                flight_results.append(flight_details)

    return flight_results

# Sample call to the function
# trip_type = "R"
# from_city = "Mumbai, India - Chhatrapati Shivaji International (BOM)"
# to_city = "New Delhi, India - Indira Gandhi Intl (DEL)"
# depart_date = "2024-10-22"
# return_date = "2024-12-22"
# adults = 1
# children = 0
# infants = 0
# cabin_class = "Y"
# currency = "NGN"

# result = fetch_flight_result(trip_type, from_city, to_city, depart_date, return_date, adults, children, infants, cabin_class, currency)
# pprint(result)
