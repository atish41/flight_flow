import requests
from pprint import pprint



def flight_validation(group_ind,unique_ref_no,flight_id,trip_type,from_city,to_city,depart_date,return_date,
                      adults,children,infants,cabin_class,currency,session_id):

    url = "https://goagentgomarket.vgtechdemo.com/api/revalidate-flight"

    payload = {
        "group_ind": group_ind,
        "unique_ref_no": unique_ref_no,
        "flight_id": flight_id,
        "trip_type": trip_type,
        "from_city": from_city,
        "to_city": to_city,
        "depart_date": depart_date,
        "return_date": return_date,
        "adults": adults,
        "children": children,
        "infants": infants,
        "cabin_class": cabin_class,
        "currency": currency,
        "api": "sabre",
        "session_id":session_id
    }
    headers = {"Accept": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    print(f"thiss is apiu response{response}")
    data=response.json()
    # response=data["message"]

    return data

# pprint(data)


group_ind=2
unique_ref_no="J4ZPAKVC5813"
flight_id=2
trip_type="R"
from_city="Hong Kong, Hong Kong - Hong Kong International (ATL)"
to_city="Tokyo, Japan - New Tokyo International Airport (DXB)"
depart_date="2024-10-22"
return_date="2024-12-22"
adults=1
children=0
infants= 0
cabin_class= "Y"
currency= "NGN"
#api= "sabre"
session_id="l86yvJV8Q166nO2l8BHTUw"

result=flight_validation(group_ind,unique_ref_no,flight_id,trip_type,from_city,to_city,depart_date,return_date,adults,children,infants,cabin_class,currency,session_id)
response=result["message"]
pprint(response)
