import requests
from pprint import pprint
from datetime import datetime

# def format_timestamp(timestamp):
#     dt_object = datetime.strptime(timestamp[0], "%Y-%m-%dT%H:%M:%S")
#     return dt_object.strftime("%A, %B %d, %Y at %I:%M %p")

# def format_timestamp(timestamp):
#     dt_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
#     return dt_object.strftime("%b %d, %Y at %I:%M %p")


# def stops_finder(arrloctxt,deploctext,arrtime,deptime):
#     stops=[places for places in deploctext if places in arrloctxt]
#     stops_arr=arrtime[:-1]
#     stops_dep=deptime[1:]
#     stops_and_time={}
#     for i in range(0,len(stops)):
#         stops_and_time[stops[i]]={"arrivaltime":stops_arr[i],"departureTime":stops_dep[i]}
#         return stops_and_time


def stops_finder(arrloctxt, deploctext, arrtime, deptime):
    stops = [places for places in deploctext if places in arrloctxt]
    
    # If no stops found, return an empty dictionary
    if not stops:
        return {}

    stops_arr = arrtime[:-1]  # Take all except last for arrival times
    stops_dep = deptime[1:]   # Take all except first for departure times
    stops_and_time = {}

    for i in range(0, len(stops)):
        stops_and_time[stops[i]] = {"arrivalTime": stops_arr[i], "departureTime": stops_dep[i]}
    
    return stops_and_time


def format_timestamp(timestamps):
    if isinstance(timestamps, list):
        return [datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S").strftime("%b %d, %Y at %I:%M %p") for ts in timestamps]
    else:
        dt_object = datetime.strptime(timestamps, "%Y-%m-%dT%H:%M:%S")
        return dt_object.strftime("%b %d, %Y at %I:%M %p")


# def convert_minutes_to_readable_format(total_duration:int):
#     hours = total_duration // 60
#     minutes = total_duration % 60
#     return f"{hours}hr and {minutes}min" if hours else f"{minutes} minutes"


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
    # print(response)
    print(from_city)
    print(to_city)
    response = response.json()
    # print(f'response from function : {response}')
    top_flights = response.get('data', [])[:5]
    
    flight_results = []

    for entry in top_flights:
        if 'onewaydata' in entry:
            for item in entry['onewaydata']:
                arrival_text=item.get("Arrival_LocationText")
                print(f'this is one wya arrival{arrival_text}')
                departure_text=item.get("Departure_LocationText")
                arrival_time=item.get("arrival_date_time")
                departure_time=item.get("departure_date_time")
                # print(f'{arrival_text}, is {departure_text},is {arrival_time}, is {departure_time}')
                stopsbreakdown=stops_finder(arrival_text,departure_text,arrival_time,departure_time)
                print(f'stop breakdown is{stopsbreakdown}')
                flight_details = {
                    'arrival_airport': item.get("Arrival_LocationText", ''),
                    'departure_airport': item.get('Departure_LocationText', ''),
                    'airline_name': item.get('OperatingAirline_Text', ''),
                    'airline_image': item.get('OperatingAirline_Image', ''),
                    'arrival_time': format_timestamp(item.get('arrival_date_time', '')),
                    'departure_time': format_timestamp(item.get('departure_date_time', '')),
                    'total_fare': item.get('total_fare', ''),
                    'trip_type': item.get('trip_type', ''),
                    'unique_no': item.get('unique_ref_no', ''),
                    'cabin_type': item.get('Cabin_Text', ''),
                    'stops': item.get('stops', '')-1,
                    'flight_number': item.get('flight_number', ''),
                    'group_ind': item.get('group_ind', ''),
                    'duration': convert_minutes_to_readable_format(item.get('total_duration', '')),
                    'arrival_location':item.get('arrival_location_code',''),
                    'departure_location':item.get('departure_location_code',''),
                    'flight_id':item.get('flight_id',''),
                    'access_token':item.get('access_token',''),
                    'session_id':item.get('session_id',''),
                    'business_logo_image':item.get('business_logo_image',''),
                    'business_name':item.get('business_name',''),
                    'stopsbreakdown':stopsbreakdown
                }

                if 'returndata' in item:
                    for return_data in item['returndata'][0]:

                        return_arrival_text=return_data.get("Arrival_LocationText"),
                        return_arrival=return_arrival_text[0]
                        print(f'this is return arrival{return_arrival}')
                        return_departure_text=return_data.get("Departure_LocationText"),
                        return_departure=return_departure_text[0]
                        return_arrival_time=return_data.get("arrival_date_time"),
                        return_arrival_time_1=return_arrival_time[0]
                        # return_arrival_time=return_arrival_time[0]
                        return_departure_time=return_data.get("departure_date_time")
                        print(f'this is departure time{return_departure_time}')
                        return_departure_time_1=return_departure_time[0]
                        # stops=stops_finder(return_arrival_text,return_departure_text,return_arrival_time,return_departure_time)
                        # return_data['Stop_names']=stops
                        # return_data['']
                        returnstopsbreakdown=stops_finder(return_arrival,return_departure,return_arrival_time_1,return_departure_time)
                        print(f'this is return flight stops{returnstopsbreakdown}')


                        return_flight_details = {
                            'return_arrival': return_data.get('Arrival_LocationText', ''),
                            'return_departure': return_data.get('Departure_LocationText', ''),
                            're_airline_image': return_data.get('OperatingAirline_Image', ''),
                            're_airline_name': return_data.get('OperatingAirline_Text', ''),
                            're_arrival_time': format_timestamp(return_data.get('arrival_date_time', '')),
                            're_departure_time': format_timestamp(return_data.get('departure_date_time', '')),
                            're_stops': return_data.get('stops', '')-1,
                            're_total_fare': return_data.get('total_fare', ''),
                            're_trip_type': return_data.get('trip_type', ''),
                            're_unique_no': return_data.get('unique_ref_no', ''),
                            're_duration': return_data.get('total_duration', ''),
                            're_arrival_location':return_data.get('arrival_location_code',''),
                            're_departure_location':return_data.get('departure_location_code',''),
                            're_session_id':return_data.get('session_id',''),
                            're_flight_id':return_data.get('flight_id',''),
                            'access_token':return_data.get('access_token',''),
                            're_group_ind':return_data.get('group_ind',''),
                            're_flight_number':return_data.get('flight_number',''),
                            # 'returnstopsbreakdown':stops_finder(return_arrival_text,return_departure_text,return_arrival_time,return_departure_time),
                            'returnstopsbreakdown':returnstopsbreakdown
                            # 'Stop_names':return_data['']
                        }
                        flight_details.update(return_flight_details)

                flight_results.append(flight_details)

    return flight_results

#Sample call to the function
trip_type = "R"
from_city = "New Delhi, India - Indira Gandhi Intl (DEL)"
# to_city = "(BOM)"
to_city = "(DXB)"
depart_date = "2024-10-22"
return_date = "​2024-12-22"
adults = 1
children = 0
infants = 0
cabin_class = "Y"
currency = "NGN"

result = fetch_flight_result(trip_type, from_city, to_city, depart_date, return_date, adults, children, infants, cabin_class, currency)
pprint(result)
