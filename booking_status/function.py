import requests
from pprint import pprint

def book_flight(flight_t_id, session_id, unique_ref_no, groupInd, payment_method, search, 
                adultTitle, adultFName, adultLName, adultDOB, adultId_type, adultPPNo, 
                adultPPICountry, adultPPNationality, adultEmail, adultMobile, 
                childTitle, childFName, childLName, childDOB, childId_type, childPPNo, 
                childPPED, childPPICountry, childPPNationality, childEmail, childMobile, 
                infantTitle, infantFName, infantLName, infantDOB, infantId_type, infantPPNo, 
                infantPPED, infantPPICountry, infantPPNationality, infantEmail, infantMobile):
    
    url = "https://goagentgomarket.vgtechdemo.com/api/book-flight"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2dvcGFkZGliYWNrZW5kLnZndGVjaGRlbW8uY29tL2FwaS92MS9hdXRoL2xvZ2luIiwiaWF0IjoxNzI3MDE5NzI1LCJleHAiOjE3MjcxMDYxMjUsIm5iZiI6MTcyNzAxOTcyNSwianRpIjoidGxmTjU2MjZFWHZaZENROCIsInN1YiI6IjE2NiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.0FnlPashkCG--ht_y0zTmhddF7oGkT6X0oajmwiEt_A"
    }
    
    payload = {
        "flight_t_id": flight_t_id,
        "session_id": session_id,
        "unique_ref_no": unique_ref_no,
        "groupInd": groupInd,
        "payment_method": payment_method,
        "search": search,
        "adultTitle": adultTitle,
        "adultFName": adultFName,
        "adultLName": adultLName,
        "adultDOB": adultDOB,
        "adultId_type": adultId_type,
        "adultPPNo": adultPPNo,
        "adultPPED": [""],
        "adultPPICountry": adultPPICountry,
        "adultPPNationality": adultPPNationality,
        "adultEmail": adultEmail,
        "adultMobile": adultMobile,
        "childTitle": childTitle,
        "childFName": childFName,
        "childLName": childLName,
        "childDOB": childDOB,
        "childId_type": childId_type,
        "childPPNo": childPPNo,
        "childPPED": childPPED,
        "childPPICountry": childPPICountry,
        "childPPNationality": childPPNationality,
        "childEmail": childEmail,
        "childMobile": childMobile,
        "infantTitle": infantTitle,
        "infantFName": infantFName,
        "infantLName": infantLName,
        "infantDOB": infantDOB,
        "infantId_type": infantId_type,
        "infantPPNo": infantPPNo,
        "infantPPED": infantPPED,
        "infantPPICountry": infantPPICountry,
        "infantPPNationality": infantPPNationality,
        "infantEmail": infantEmail,
        "infantMobile": infantMobile
    }
    
    response = requests.post(url, json=payload, headers=headers)
    data=response.json()
    booking=[]
    details={
        'message':data.get('message'),
        'currnency':data['data']['booking'].get('currency'),
        'amount':data['data'].get('amount'),
        'created_at':data['data']['booking'].get('created_at'),
        'payment_type':data['data']['booking'].get('payment_method'),
        'payment_link':data['data'].get('link'),
        'booking_id':data['data'].get('booking_id')
     
    }
    # booking.append(details)


    

    return details

   

# Example usage:
search_data = [
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
]

result = book_flight(
    flight_t_id="0", 
    session_id="6ITZPEVA70771", 
    unique_ref_no="6ITZPEVA7077", 
    groupInd="1", 
    payment_method="flutterwave", 
    search=search_data,
    adultTitle=["Mrs"], 
    adultFName=["Jane"], 
    adultLName=["Doe"], 
    adultDOB=["1988-11-04"], 
    adultId_type=["passport"], 
    adultPPNo=["1854841784"], 
    # adultPPED=[], 
    adultPPICountry=["NG"], 
    adultPPNationality=["NG"], 
    adultEmail=["amitpawar118@gmail.com"], 
    adultMobile=["7894561230"], 
    childTitle=["Mstr"], 
    childFName=["John"], 
    childLName=["Doe"], 
    childDOB=["2011-12-04"], 
    childId_type=["passport"], 
    childPPNo=["12121215141"], 
    childPPED=["2030-11-05"], 
    childPPICountry=["NG"], 
    childPPNationality=["NG"], 
    childEmail=["amitpawar118@gmail.com"], 
    childMobile=["7894561230"], 
    infantTitle=[], 
    infantFName=[], 
    infantLName=[], 
    infantDOB=[], 
    infantId_type=[], 
    infantPPNo=[], 
    infantPPED=[], 
    infantPPICountry=[], 
    infantPPNationality=[], 
    infantEmail=[], 
    infantMobile=[]
)

pprint(result)
