from datetime import datetime
# def timeformatter(arrivaltime):
#     arrtime = datetime.fromisoformat(arrivaltime)
    
#     arrtime = arrtime.strftime("%Y-%m-%d %H:%M:%S")
#     return arrtime

# def stopsprinter(data,stops):
#     if not data:
#         return ""
#     output=f"Stop: {int(stops)}\n"

#     for city, details in data.items():
#         output+= f'''🟡{city}
#     Arrival : {timeformatter(details['arrivalTime'])}
#     Departure : {timeformatter(details['departureTime'])}
# '''
#     return output



def timeformatter(arrivaltime):
    arrtime = datetime.fromisoformat(arrivaltime)
    arrtime = arrtime.strftime("%d %b %Y, %I:%M %p")  # Format: 01 Oct 2024, 10:15 PM
    return arrtime

def stopsprinter(data, stops):
    if not data:
        return ""
    output = f"Stop: {int(stops)}\n"
    for city, details in data.items():
        output += f'''🟡{city}     Arrival: {timeformatter(details['arrivalTime'])}     Departure: {timeformatter(details['departureTime'])}\n'''
    return output