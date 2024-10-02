import requests
from pprint import pprint

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

    top_flights = response.get('data', [])[:2]
    flight_results = []

    for entry in top_flights:
        if 'onewaydata' in entry:
            # Iterate over the list under onewaydata
            for item in entry['onewaydata']:
                # Collect flight details, extracting the first element from each list
                flight_details = {
                    'arrival_airport': item.get("Arrival_LocationText", [''])[0],
                    'departure_airport': item.get('Departure_LocationText', [''])[0],
                    'airline': item.get('OperatingAirline_Text', [''])[0],
                    'airline_image': item.get('OperatingAirline_Image', [''])[0],
                    'arrival_time': item.get('arrival_date_time', [''])[0],
                    'departure_time': item.get('departure_date_time', [''])[0],
                    'total_fare': item.get('total_fare', 0),
                    'trip_type': item.get('trip_type', ''),
                    'unique_no': item.get('unique_ref_no', '')
                }

                # Check if return data exists and add it to the flight details
                if 'returndata' in item and item['returndata']:
                    return_data = item['returndata'][0]
                    return_flight_details = {
                        'return_arrival': return_data.get('Arrival_LocationText', [''])[0],
                        'return_departure': return_data.get('Departure_LocationText', [''])[0],
                        're_airline_image': return_data.get('OperatingAirline_Image', [''])[0],
                        're_airline': return_data.get('OperatingAirline_Text', [''])[0],
                        're_arrival_time': return_data.get('arrival_date_time', [''])[0],
                        're_departure_time': return_data.get('departure_date_time', [''])[0],
                        're_stops': return_data.get('stops', 0),
                        're_total_fare': return_data.get('total_fare', 0),
                        're_trip_type': return_data.get('trip_type', ''),
                        're_unique_no': return_data.get('unique_ref_no', '')
                    }
                    flight_details.update(return_flight_details)

                # Add the flight details to the results list
                flight_results.append(flight_details)

    return flight_results

# Example usage
flights = fetch_flight_result(
    trip_type="R",
    from_city="Mumbai, India - Chhatrapati Shivaji International (BOM)",
    to_city="New Delhi, India - Indira Gandhi Intl (DEL)",
    depart_date="2024-10-22",
    return_date="2024-12-22",
    adults=1,
    children=0,
    infants=0,
    cabin_class="Y",
    currency="NGN"
)

pprint(flights)
