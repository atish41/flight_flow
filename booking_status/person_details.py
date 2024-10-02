from names import namedivider
def process_passenger_info(parameters, passenger_type, count):
    info = {
        f'{passenger_type}Title': [],
        f'{passenger_type}FName': [],
        f'{passenger_type}LName': [],
        f'{passenger_type}DOB': [],
        f'{passenger_type}Id_type': [],
        f'{passenger_type}PPNo': [],
        f'{passenger_type}PPED': [],
        f'{passenger_type}PPICountry': [],
        f'{passenger_type}PPNationality': []
    }
    
    for i in range(1, count + 1):
        fullname = parameters.get(f"{passenger_type}_fullname_{i}", "")
        fname, lname = namedivider(fullname)
        info[f'{passenger_type}FName'].append(fname)
        info[f'{passenger_type}LName'].append(lname)
        
        info[f'{passenger_type}Title'].append(parameters.get(f"{passenger_type}_title_{i}", ""))
        info[f'{passenger_type}DOB'].append(parameters.get(f"{passenger_type}_dob_{i}", ""))
        info[f'{passenger_type}Id_type'].append(parameters.get(f"{passenger_type}_id_type_{i}", ""))
        info[f'{passenger_type}PPNo'].append(parameters.get(f"{passenger_type}_id_number_{i}", ""))
        
        # These fields are not provided in the current parameters, so we'll leave them empty
        info[f'{passenger_type}PPED'].append("")
        info[f'{passenger_type}PPICountry'].append("")
        info[f'{passenger_type}PPNationality'].append("")
    
    if passenger_type == 'adult':
        info[f'{passenger_type}Email'] = [parameters.get("email", "")]
        info[f'{passenger_type}Mobile'] = [parameters.get("mobile", "")]
    else:
        info[f'{passenger_type}Email'] = [""]
        info[f'{passenger_type}Mobile'] = [""]
    
    return info

if __name__=="__main__":


    parameters = {
        "adult_fullname": "John Doe",
        "adult_title_1": "Mr",
        "adult_dob_1": "1990-01-01",
        "adult_id_type_1": "Passport",
        "adult_id_number_1": "A1234567",
        "email": "johndoe@example.com",
        "mobile": "1234567890"
    }
    
    result = process_passenger_info(parameters, "adult", 1)
    print(result)