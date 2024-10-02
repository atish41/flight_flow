import requests
from pprint import pprint

def book_flight(flight_t_id, session_id, unique_ref_no, groupInd, payment_method, search, 
                adultTitle, adultFName, adultLName, adultDOB, adultId_type, adultPPNo, 
                adultEmail, adultMobile, 
                childTitle, childFName, childLName, childDOB, childId_type, childPPNo,  
                infantTitle, infantFName, infantLName, infantDOB, infantId_type,infantPPNo):
    
    url = "https://goagentgomarket.vgtechdemo.com/api/book-flight"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2dvcGFkZGliYWNrZW5kLnZndGVjaGRlbW8uY29tL2FwaS92MS9hdXRoL2xvZ2luIiwiaWF0IjoxNzI3ODcwMDQxLCJleHAiOjE3Mjc5NTY0NDEsIm5iZiI6MTcyNzg3MDA0MSwianRpIjoiOGRtdlg0WGk5bVBiSUVlNSIsInN1YiI6IjE2MSIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.lcseZIEWD1qKZYVXqj35hlokFUqumEqpeVu0BnUSuhs"
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
        "adultPPICountry":[""],
        "adultPPNationality":[""],
        "adultEmail": adultEmail,
        "adultMobile": adultMobile,
        "childTitle": childTitle,
        "childFName": childFName,
        "childLName": childLName,
        "childDOB": childDOB,
        "childId_type": childId_type,
        "childPPNo": childPPNo,
        "childPPED": [""],
        "childPPICountry":[""],
        "childPPNationality":[""],
        "childEmail": [""],
        "childMobile": [""],
        "infantTitle": infantTitle,
        "infantFName": infantFName,
        "infantLName": infantLName,
        "infantDOB": infantDOB,
        "infantId_type": infantId_type,
        "infantPPNo": infantPPNo,
        "infantPPED":[""],
        "infantPPICountry":[""],
        "infantPPNationality":[""],
        "infantEmail":[""],
        "infantMobile":[""]
    }
    
    response = requests.post(url, json=payload, headers=headers)
    pprint(f'this is respone-{response}')
    data=response.json()
    # pprint(data)re

    # Add try and except clause for exception handling 
    booking=[]
    details={
        'message':data.get('message'),
        'currnency':data['data']['booking'].get('currency'),
        'amount':data['data'].get('amount'),
        'created_at':data['data']['booking'].get('created_at'),
        'payment_type':data['data']['booking'].get('payment_method'),
        'payment_link':data['data'].get('link'),
        'booking_id':data['data'].get('booking_id'),
        "reference_id":data['data']['payment'].get('reference','')
     
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

# result = book_flight(
#     flight_t_id="0", 
#     session_id="6ITZPEVA70771", 
#     unique_ref_no="6ITZPEVA7077", 
#     groupInd="1", 
#     payment_method="flutterwave", 
#     search=search_data,
#     adultTitle=["Mrs"], 
#     adultFName=["Jane"], 
#     adultLName=["Doe"], 
#     adultDOB=["1988-11-04"], 
#     adultId_type=["passport"], 
#     adultPPNo=["1854841784"], 
#     # adultPPED=[], 
#     adultPPICountry=["NG"], 
#     adultPPNationality=["NG"], 
#     adultEmail=["amitpawar118@gmail.com"], 
#     adultMobile=["7894561230"], 
#     childTitle=["Mstr"], 
#     childFName=["John"], 
#     childLName=["Doe"], 
#     childDOB=["2011-12-04"], 
#     childId_type=["passport"], 
#     childPPNo=["12121215141"], 
#     childPPED=["2030-11-05"], 
#     childPPICountry=["NG"], 
#     childPPNationality=["NG"], 
#     childEmail=["amitpawar118@gmail.com"], 
#     childMobile=["7894561230"], 
#     infantTitle=[], 
#     infantFName=[], 
#     infantLName=[], 
#     infantDOB=[], 
#     infantId_type=[], 
#     infantPPNo=[], 
#     infantPPED=[], 
#     infantPPICountry=[], 
#     infantPPNationality=[], 
#     infantEmail=[], 
#     infantMobile=[]
# )

# pprint(result)

if __name__=="__main__":

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
        # adultPPED=["2007-11-05"], 
        # adultPPICountry=["NG"], 
        # adultPPNationality=["NG"], 
        adultEmail=["amitpawar118@gmail.com"], 
        adultMobile=["7894561230"], 
        childTitle=["Mstr"], 
        childFName=["John"], 
        childLName=["Doe"], 
        childDOB=["2011-12-04"], 
        childId_type=["passport"], 
        childPPNo=["12121215141"], 
        # childPPED=["2030-11-05"], 
        # childPPICountry=["NG"], 
        # childPPNationality=["NG"], 
        # childEmail=["amitpawar118@gmail.com"], 
        # childMobile=["7894561230"], 
        infantTitle=[], 
        infantFName=[], 
        infantLName=[], 
        infantDOB=[], 
        infantId_type=[], 
        infantPPNo=[], 
        # infantPPED=[], 
        # infantPPICountry=[], 
        # infantPPNationality=[], 
        # infantEmail=[], 
        # infantMobile=[]
    )

    pprint(result)
