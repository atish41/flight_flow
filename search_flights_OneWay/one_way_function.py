import requests
from pprint import pprint

url = "https://goagentgomarket.vgtechdemo.com/api/search-flights"

payload = {
    "trip_type": "S",
    "from_city": "(DEL)",
    "to_city": "(DXB)",
    "depart_date": "2024-10-22",
    "return_date": "",
    "adults": 1,
    "children": 0,
    "infants": 0,
    "cabin_class": "Y",
    "currency": "NGN"
}
response = requests.request("POST", url, json=payload)
data=response.json()

top_flights=data.get("data",[])[:3]
pprint(top_flights)