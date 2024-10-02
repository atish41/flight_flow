# from demo import fetch_flight_result
# from trial_function import fetch_flight_result
# # from return_function import fetch_flight_result
# # from main import fetch_flight_result
# # from trial_function import fetch_flight_result
# from pprint import pprint



# response=fetch_flight_result(
#     trip_type="R", 
#     from_city="New Delhi, India - Indira Gandhi Intl (DEL)", 
#     to_city="(DXB)", 
#     #to_city="New Delhi, India - Indira Gandhi Intl (DEL)", 
#     depart_date="2024-10-22", 
#     return_date="2024-12-22", 
#     adults=1, 
#     children=0, 
#     infants=0, 
#     cabin_class="Y", 
#     currency="NGN"
# )


# # for result in response:
# pprint(response)


def stops_finder(arrloctxt, deploctext, arrtime, deptime):
    stops = [places for places in deploctext if places in arrloctxt]
    stops_arr = arrtime[:-1]
    stops_dep = deptime[1:]
    stops_and_time = {}
    
    for i in range(0, len(stops)):
        stops_and_time[stops[i]] = {"arrivaltime": stops_arr[i], "departureTime": stops_dep[i]}
    
    return stops_and_time



arrloctxt = ['CityA', 'CityB', 'CityC']
deploctext = ['CityX', 'CityB', 'CityY']
arrtime = ['10:00', '12:00', '14:00']
deptime = ['09:00', '11:00', '13:00']

result = stops_finder(arrloctxt, deploctext, arrtime, deptime)
print(result)