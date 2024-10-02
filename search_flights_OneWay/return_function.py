import requests
from pprint import pprint
from datetime import datetime

# trip_type="R"
# from_city="Mumbai, India - Chhatrapati Shivaji International (BOM)"
# to_city="New Delhi, India - Indira Gandhi Intl (DEL)"
# depart_date="2024-10-22"
# return_date="​2024-12-22"
# adults=1
# children=0
# infants=0
# cabin_class="Y"
# currency="NGN"

def fetch_flight_result(trip_type,from_city,to_city,depart_date,return_date,adults,children,infants,cabin_class,currency):
    
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
    response=response.json()

    top_flights=response.get('data',[])[:2]
    # top_flights=response.get('data',[])[:2]


    flight_results=[]
    # flight_list=[flight_list for flight_list in flight_results]
    
    
    # for item in top_flights:
    #     details={
    #         "arrival_airport":item.get(["Arrival_LocationText"],[])


    #     }
    #     flight_results.append(details)

    for entry in top_flights:
        # pprint(entry)
        if 'onewaydata' in entry:
            #iterate over the list under oneway data
            for item in entry['onewaydata']:
                #access over individual data
                flight_details={

                    'arrival_airport':item.get("Arrival_LocationText",''),
                    'departure_airport':item.get('Departure_LocationText',''),
                    'airline_name':item.get('OperatingAirline_Text',''),
                    'airline_image':item.get('OperatingAirline_Image',''),
                    'arrival_time':item.get('arrival_date_time',''),
                    'departure_time':item.get('departure_date_time',''),
                    'total_fare':item.get('total_fare',''),
                    'trip_type':item.get('trip_type',''),
                    'unique_no':item.get('unique_ref_no',''),
                    'Cabin_type':item.get('Cabin_Text',''),
                    'stops':item.get('stops',''),
                    'flight_number':item.get('flight_number',''),
                    'group_ind':item.get('group_ind',''),
                    'duration':item.get('duration','')

                }
                

                if 'returndata' in item:
                    for return_data in item['returndata'][0]:
                        return_flight_details={
                            'return_arrival':return_data.get('Arrival_LocationText',''),
                            'return_departure':return_data.get('Departure_LocationText',''),
                            're_airline_image':return_data.get('OperatingAirline_Image',''),
                            're_airline_name':return_data.get('OperatingAirline_Text',''),
                            're_arrival_time':return_data.get('arrival_date_time',''),
                            're_departure_time':return_data.get('departure_date_time',''),
                            're_stops':return_data.get('stops',''),
                            're_total_fare':return_data.get('total_fare',''),
                            're_trip_type':return_data.get('trip_type',''),
                            're_unique_no':return_data.get('unique_ref_no',''),
                            're_duration':return_data.get('duration','')
                        }
                        flight_details.update(return_flight_details)
                flight_results.append(flight_details)
    #for flight_list in flight_results:

    
    # fligh_list=[flight_list for flight_list in flight_results]

    return flight_results




            
                       







# pprint(flight_results)