import requests
from pprint import pprint

url = "https://goagentgomarket.vgtechdemo.com/api/book-flight"

payload = {
    "flight_t_id": "0",
    "session_id": "6ITZPEVA70771",
    "unique_ref_no": "6ITZPEVA7077",
    "groupInd": "1",
    "payment_method": "flutterwave",
    "search": [
        {
            "tripType": "S",
            "fromCity": "Hong Kong, Hong Kong - Hong Kong International (HKG)",
            "toCity": "Tokyo, Japan - New Tokyo International Airport (NRT)",
            "departDate": "2024-10-01",
            "returnDate": "",
            "adults": "1",
            "childs": "1",
            "infants": "0",
            "cabinClass": "Y",
            "currency": "NGN",
            "unique_ref_no": "6ITZPEVA7077"
        }
    ],
    "adultTitle": ["Mrs"],
    "adultFName": ["Jane"],
    "adultLName": ["Doe"],
    "adultDOB": ["1988-11-04"],
    "adultId_type": ["passport"],
    "adultPPNo": ["1854841784"],
    "adultPPED": ["2007-11-05"],
    "adultPPICountry": ["NG"],
    "adultPPNationality": ["NG"],
    "adultEmail": ["amitpawar118@gmail.com"],
    "adultMobile": ["7894561230"],
    "childTitle": ["Mstr"],
    "childFName": ["John"],
    "childLName": ["Doe"],
    "childDOB": ["2011-12-04"],
    "childId_type": ["passport"],
    "childPPNo": ["12121215141"],
    "childPPED": ["2030-11-05"],
    "childPPICountry": ["NG"],
    "childPPNationality": ["NG"],
    "childEmail": ["amitpawar118@gmail.com"],
    "childMobile": ["7894561230"],
    "infantTitle": [],
    "infantFName": [],
    "infantLName": [],
    "infantDOB": [],
    "infantId_type": [],
    "infantPPNo": [],
    "infantPPED": [],
    "infantPPICountry": [],
    "infantPPNationality": [],
    "infantEmail": [],
    "infantMobile": []
}
headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2dvcGFkZGliYWNrZW5kLnZndGVjaGRlbW8uY29tL2FwaS92MS9hdXRoL2xvZ2luIiwiaWF0IjoxNzI3MDE5NzI1LCJleHAiOjE3MjcxMDYxMjUsIm5iZiI6MTcyNzAxOTcyNSwianRpIjoidGxmTjU2MjZFWHZaZENROCIsInN1YiI6IjE2NiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.0FnlPashkCG--ht_y0zTmhddF7oGkT6X0oajmwiEt_A"}

response = requests.request("POST", url, json=payload, headers=headers)
data=response.json()

booking_itmes={
    'message':data.get("message"),
    'currnency':data['data']['booking'].get('currency'),
    'amount':data['data'].get('amount'),
    'created_at':data['data']['booking'].get('created_at'),
    'payment_type':data['data']['booking'].get('payment_method'),
    'payment_link':data['data'].get('link'),
    'booking_id':data['data'].get('booking_id')
}     

# print(amount)
# print(message)
# print(currnency)

# final_booking=[]
# for i in data:
#     details={
#         "booking_statues":data[i]
#     }
#     data[i]
# pprint(data)