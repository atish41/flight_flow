# from flask import Flask, request 
# from pprint import pprint

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "This server returns an activity booking form"

# @app.route('/form', methods=['POST'])
# def webhook():
#     req = request.get_json(force=True)
#     pprint(req)
#     sessionInfo = req['sessionInfo']
#     parameters = sessionInfo['parameters']
#     adults = int(parameters['adults'])
#     infants = int(parameters['infants'])
#     children = int(parameters['children'])
    
#     response = {
#         "fulfillmentResponse": {
#             "messages": [
#                 {
#                     "responseType": "RESPONSE_TYPE_UNSPECIFIED",
#                     "channel": "",
#                     "payload": {
#                         "botcopy": [
#                             {
#                                 "form": {
#                                     "force": True,
#                                     "subtitle": "",
#                                     "fields": [],
#                                     "action": {
#                                         "message": {
#                                             "type": "training",
#                                             "command": "Submit"
#                                         }
#                                     },
#                                     "title": "Flight Booking",
#                                     "style": "message"
#                                 }
#                             }
#                         ]
#                     }
#                 }
#             ]
#         }
#     }

#     fields = response["fulfillmentResponse"]["messages"][0]["payload"]["botcopy"][0]['form']["fields"]

#     # Helper function to create dropdown fields
#     def create_dropdown(parameter, group_label, options):
#         return {
#             "expose": True,
#             "groupLabel": group_label,
#             "parameter": parameter,
#             "select": [{"parameter": key, "selectLabel": value} for key, value in options.items()],
#             "fieldType": "select"
#         }

#     # Add fields for adults
#     for i in range(1, adults + 1):
#         fields.extend([
#             create_dropdown(f"adult_title_{i}", f"Adult Title", 
#                             {"Mr": "Mr", "Mrs": "Mrs", "Ms": "Ms", "Dr": "Dr"}),
#             {
#                 "error": "This field is required.",
#                 "helperText": "",
#                 "expose": True,
#                 "required": True,
#                 "parameter": f"adult_fullname_{i}",
#                 "placeholder": f"Adult {i} Full Name",
#                 "type": "text",
#                 "label": f"Adult {i} Full Name"
#             },
#             {
#                 "error": "This field is required.",
#                 "helperText": "",
#                 "expose": True,
#                 "required": True,
#                 "parameter": f"adult_dob_{i}",
#                 "placeholder": "YYYY-MM-DD",
#                 "type": "date",
#                 "label": f"Adult {i} Date of Birth"
#             },
#             create_dropdown(f"adult_id_type_{i}", f"Adult {i} ID Type", 
#                             {"passport": "Passport"}),
#             {
#                 "error": "This field is required.",
#                 "helperText": "",
#                 "expose": True,
#                 "required": True,
#                 "parameter": f"adult_id_number_{i}",
#                 "placeholder": "Enter Passport Number",
#                 "type": "text",
#                 "label": f"Adult {i} ID Number"
#             }
#         ])


from flask import Flask, request 
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def hello():
    return "This server returns an activity booking form"

@app.route('/form', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    pprint(req)
    sessionInfo = req['sessionInfo']
    parameters = sessionInfo['parameters']
    adults = int(parameters['adults'])
    infants = int(parameters['infants'])
    children = int(parameters['children'])
    
    response = {
        "fulfillmentResponse": {
            "messages": [
                {
                    "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                    "channel": "",
                    "payload": {
                        "botcopy": [
                            {
                                "form": {
                                    "force": True,
                                    "subtitle": "",
                                    "fields": [],
                                    "action": {
                                        "message": {
                                            "type": "training",
                                            "command": "Submit"
                                        }
                                    },
                                    "title": "Flight Booking",
                                    "style": "message"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

    fields = response["fulfillmentResponse"]["messages"][0]["payload"]["botcopy"][0]['form']["fields"]

    # Helper function to create dropdown fields
    def create_dropdown(parameter, group_label, options):
        return {
            "expose": True,
            "groupLabel": group_label,
            "parameter": parameter,
            "select": [{"parameter": key, "selectLabel": value} for key, value in options.items()],
            "fieldType": "select"
        }

    # Add fields for adults
    for i in range(1, adults + 1):
        if i == 1:
            # Fields for the first adult (without numbering)
            fields.extend([
                create_dropdown("adult_title", "Adult Title", 
                                {"Mr": "Mr", "Mrs": "Mrs", "Ms": "Ms"}),
                {
                    "error": "This field is required.",
                    "helperText": "",
                    "expose": True,
                    "required": True,
                    "parameter": "adult_fullname",
                    "placeholder": "Adult Full Name",
                    "type": "text",
                    "label": "Adult Full Name"
                },
                {
                    "error": "This field is required.",
                    "helperText": "",
                    "expose": True,
                    "required": True,
                    "parameter": "adult_dob",
                    "placeholder": "YYYY-MM-DD",
                    "type": "date",
                    "label": "Adult Date of Birth"
                },
                create_dropdown("adult_id_type", "Adult ID Type", 
                                {"passport": "Passport"}),
                {
                    "error": "This field is required.",
                    "helperText": "",
                    "expose": True,
                    "required": True,
                    "parameter": "adult_id_number",
                    "placeholder": "Enter Passport Number",
                    "type": "text",
                    "label": "Adult ID Number"
                }
            ])
        else:
            # Fields for additional adults (with numbering)
            fields.extend([
                create_dropdown(f"adult_title_{i}", f"Adult {i} Title", 
                                {"Mr": "Mr", "Mrs": "Mrs", "Ms": "Ms"}),
                {
                    "error": "This field is required.",
                    "helperText": "",
                    "expose": True,
                    "required": True,
                    "parameter": f"adult_fullname_{i}",
                    "placeholder": f"Adult {i} Full Name",
                    "type": "text",
                    "label": f"Adult {i} Full Name"
                },
                {
                    "error": "This field is required.",
                    "helperText": "",
                    "expose": True,
                    "required": True,
                    "parameter": f"adult_dob_{i}",
                    "placeholder": "YYYY-MM-DD",
                    "type": "date",
                    "label": f"Adult {i} Date of Birth"
                },
                create_dropdown(f"adult_id_type_{i}", f"Adult {i} ID Type", 
                                {"passport": "Passport"}),
                {
                    "error": "This field is required.",
                    "helperText": "",
                    "expose": True,
                    "required": True,
                    "parameter": f"adult_id_number_{i}",
                    "placeholder": "Enter Passport Number",
                    "type": "text",
                    "label": f"Adult {i} ID Number"
                }
            ])

    # Rest of the code remains the same...

    # Add fields for children
    for i in range(1, children + 1):
        fields.extend([
            create_dropdown(f"child_title_{i}", f"Child {i} Title", 
                            {"Master": "Master", "Miss": "Miss"}),
            {
                "error": "This field is required.",
                "helperText": "",
                "expose": True,
                "required": True,
                "parameter": f"child_fullname_{i}",
                "placeholder": f"Child {i} Full Name",
                "type": "text",
                "label": f"Child {i} Full Name"
            },
            {
                "error": "This field is required.",
                "helperText": "",
                "expose": True,
                "required": True,
                "parameter": f"child_dob_{i}",
                "placeholder": "YYYY-MM-DD",
                "type": "date",
                "label": f"Child {i} Date of Birth"
            },
            create_dropdown(f"child_id_type_{i}", f"Child {i} ID Type", 
                            {"passport": "Passport"}),
            {
                "error": "This field is required.",
                "helperText": "",
                "expose": True,
                "required": True,
                "parameter": f"child_id_number_{i}",
                "placeholder": "Enter Passport Number",
                "type": "text",
                "label": f"Child {i} ID Number"
            }
        ])

    # Add fields for infants
    for i in range(1, infants + 1):
        fields.extend([
            create_dropdown(f"infant_title_{i}", f"Infant {i} Title", 
                            {"Master": "Master", "Miss": "Miss"}),
            {
                "error": "This field is required.",
                "helperText": "",
                "expose": True,
                "required": True,
                "parameter": f"infant_fullname_{i}",
                "placeholder": f"Infant {i} Full Name",
                "type": "text",
                "label": f"Infant {i} Full Name"
            },
            {
                "error": "This field is required.",
                "helperText": "",
                "expose": True,
                "required": True,
                "parameter": f"infant_dob_{i}",
                "placeholder": "YYYY-MM-DD",
                "type": "date",
                "label": f"Infant {i} Date of Birth"
            },
            create_dropdown(f"infant_id_type_{i}", f"Infant {i} ID Type", 
                            {"passport": "Passport"}),
            {
                "error": "This field is required.",
                "helperText": "",
                "expose": True,
                "required": True,
                "parameter": f"infant_id_number_{i}",
                "placeholder": "Enter Passport Number",
                "type": "text",
                "label": f"Infant {i} ID Number"
            }
        ])

    # Add email and phone number fields
    fields.extend([
        {
            "error": "This field is required.",
            "helperText": "",
            "expose": True,
            "required": True,
            "parameter": "email",
            "placeholder": "johndoe@gmail.com",
            "type": "email",
            "label": "Email"
        },
        {
            "error": "This field is required.",
            "helperText": "",
            "expose": True,
            "required": True,
            "parameter": "mobile",
            "placeholder": "+918424883935",
            "type": "text",
            "label": "Contact number"
        }
    ])

    return response

if __name__ == "__main__":
    app.run(debug=True, port=8000)