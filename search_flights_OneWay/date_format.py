# def convert_to_date(date_dict):
#     day=int(date_dict['day'])
#     month=int(date_dict['month'])
#     year=int(date_dict['year'])

#     formated_date=f"{year:04d}-{month:02d}-{day:02d}"
#     return formated_date

# date_dict = {'day': 4.0, 'month': 9.0, 'year': 2024.0}
# print(convert_to_date(date_dict))


# import datetime
# def dictodate(departureDate):
#   departureDate['year']=int(departureDate['year'])
#   departureDate['month']=int(departureDate['month'])
#   departureDate['day']=int(departureDate['day'])
#   departure_date = datetime.datetime(departureDate['year'], departureDate['month'], departureDate['day'])
#   formatted_departure_date = departure_date.strftime('%Y-%m-%d')
#   return formatted_departure_date


# date_dict = {'day': 4.0, 'month': 9.0, 'year': 2024.0}
# print(dictodate(date_dict))




import datetime

def dict_to_date(date_dict, key='future'):
    # Select the date dictionary to be converted
    if key in date_dict and isinstance(date_dict[key], dict):
        date_to_convert = date_dict[key]
    else:
        # If no specific key is found, use the main date dictionary
        date_to_convert = date_dict
    
    # Convert date fields to integers
    date_to_convert['year'] = int(date_to_convert['year'])
    date_to_convert['month'] = int(date_to_convert['month'])
    date_to_convert['day'] = int(date_to_convert['day'])
    
    # Create a datetime object and format it as a string
    date_obj = datetime.datetime(date_to_convert['year'], date_to_convert['month'], date_to_convert['day'])
    return date_obj.strftime('%Y-%m-%d')

date_dict = {
    'day': 13.0,
    'future': {'day': 13.0, 'month': 9.0, 'year': 2024.0},
    'month': 9.0,
    'partial': {'day': 13.0, 'month': 9.0, 'year': 2024.0},
    'past': {'day': 6.0, 'month': 9.0, 'year': 2024.0},
    'year': 2024.0
}

# Example: Get the 'future' date
formatted_date = dict_to_date(date_dict, key='future')
print(formatted_date)
