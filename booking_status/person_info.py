from names import namedivider

def process_passenger_info(parameters, passenger_type, count=1):
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
        # Handle both numbered and non-numbered cases
        suffix = f"_{i}" if count > 1 else ""
        fullname = parameters.get(f"{passenger_type}_fullname{suffix}", "")
        fname, lname = namedivider(fullname)
        info[f'{passenger_type}FName'].append(fname)
        info[f'{passenger_type}LName'].append(lname)

        info[f'{passenger_type}Title'].append(parameters.get(f"{passenger_type}_title{suffix}", ""))
        info[f'{passenger_type}DOB'].append(parameters.get(f"{passenger_type}_dob{suffix}", ""))
        info[f'{passenger_type}Id_type'].append(parameters.get(f"{passenger_type}_id_type{suffix}", ""))
        info[f'{passenger_type}PPNo'].append(parameters.get(f"{passenger_type}_id_number{suffix}", ""))

        # These fields are left empty as they are not provided
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

# Test the function
if __name__ == "__main__":
    parameters = {
        "adult_fullname": "John Doe",
        "adult_title": "Mr",
        "adult_dob": "1990-01-01",
        "adult_id_type": "Passport",
        "adult_id_number": "A1234567",
        "email": "johndoe@example.com",
        "mobile": "1234567890"
    }

    result = process_passenger_info(parameters, "adult", 1)
    print(result)
