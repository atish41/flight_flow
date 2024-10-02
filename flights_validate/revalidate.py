# import requests

# url = "https://goagentgomarket.vgtechdemo.com/api/revalidate-flight"

# #payload = "group_ind=1&unique_ref_no=6ITZPEVA7077&flight_id=0&trip_type=S&from_city=Hong%20Kong%2C%20Hong%20Kong%20-%20Hong%20Kong%20International%20(ATL)&to_city=Tokyo%2C%20Japan%20-%20New%20Tokyo%20International%20Airport%20(DXB)&depart_date=2024-10-01&return_date=&adults=1&children=1&infants=0&cabin_class=Y&currency=NGN&api=sabre&session_id=6ITZPEVA70771"
# payload = {
#     "group_ind": 1,
#     "unique_ref_no": "6ITZPEVA7077",
#     "flight_id": 0,
#     "trip_type": "S",
#     "from_city": "Hong Kong, Hong Kong - Hong Kong International (ATL)",
#     "to_city": "Tokyo, Japan - New Tokyo International Airport (DXB)",
#     "depart_date": "2024-10-01",
#     "return_date": "",
#     "adults": 1,
#     "children": 1,
#     "infants": 0,
#     "cabin_class": "Y",
#     "currency": "NGN",
#     "api": "sabre",
#     "session_id": "6ITZPEVA70771"
# }
# headers = {"token": "p2lbgWkFrykA4QyUmpHihzmc5BNzIABq"}

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)


import requests
import json

url = "https://goagentgomarket.vgtechdemo.com/api/revalidate-flight"
def revalidate_flight(group_ind, unique_ref_no, flight_id, trip_type, from_city, to_city, depart_date, return_date, adults, children, infants, cabin_class, currency, api, session_id, token):
    
    
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
        "api": api,
        "session_id": session_id
    }
    
    headers = {"token": token}
    
    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
        
        response_json = response.json()
        
        message = response_json.get("message")
        
        # from the second object in the data array
        access_token = None
        if "data" in response_json and len(response_json["data"]) > 1:
            access_token = response_json["data"][1].get("AccessToken")
        
        return message, access_token
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None
    except json.JSONDecodeError:
        print("Error: Unable to parse JSON response")
        return None, None

# Example usage
# message, access_token = revalidate_flight(
#     group_ind=1,
#     unique_ref_no="W93YECH41034",
#     flight_id=0,
#     trip_type="R",
#     from_city="Hong Kong, Hong Kong - Hong Kong International (ATL)",
#     to_city="Tokyo, Japan - New Tokyo International Airport (DXB)",
#     depart_date="2024-11-22",
#     return_date="2024-12-22",
#     adults=1,
#     children=1,
#     infants=0,
#     cabin_class="Y",
#     currency="NGN",
#     api="sabre",
#     session_id="T_oqSyhUQ8GFAx3pOVEiGw",
#     token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2dvYWdlbnRnb21hcmtldC52Z3RlY2hkZW1vLmNvbS9hcGkvbG9naW4iLCJpYXQiOjE3MjY0ODcxMTQsImV4cCI6MTcyNjU3MzUxNCwibmJmIjoxNzI2NDg3MTE0LCJqdGkiOiJ5aVpLVklzUnNSNENjdUZKIiwic3ViIjoiNjA3IiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.5FXSjEzahb8Kpum6mwXc0tnM7RgOasRJcuuCiCx4j2g"
# )


message, access_token = revalidate_flight(
    group_ind=1,
    unique_ref_no="W93YECH41034",
    flight_id=0,
    trip_type="R",
    from_city="Hong Kong, Hong Kong - Hong Kong International (ATL)",
    to_city="Tokyo, Japan - New Tokyo International Airport (DXB)",
    depart_date="2024-11-22",
    return_date="2024-12-22",
    adults=1,
    children=1,
    infants=0,
    cabin_class="Y",
    currency="NGN",
    api="sabre",
    session_id="T_oqSyhUQ8GFAx3pOVEiGw",
    token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2dvYWdlbnRnb21hcmtldC52Z3RlY2hkZW1vLmNvbS9hcGkvbG9naW4iLCJpYXQiOjE3MjY0ODcxMTQsImV4cCI6MTcyNjU3MzUxNCwibmJmIjoxNzI2NDg3MTE0LCJqdGkiOiJ5aVpLVklzUnNSNENjdUZKIiwic3ViIjoiNjA3IiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.5FXSjEzahb8Kpum6mwXc0tnM7RgOasRJcuuCiCx4j2g"
)

print("Message:", message)
print("Access Token:", access_token)