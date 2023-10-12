# import xmlrpc.client
#
# url = "http://127.0.0.1:8069"
# db = "odoo_16_new"
# username = "ansarishazan48@gmail.com"
# password = "admin"
# #
# # common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# #
# # uid = common.authenticate(db, username, password, {})
# #
# # if uid:
# #   print('authenticated')
# # else:
# #   print('cannot authenticate')
# #
#
#
#
# # Connect to Odoo using the XML-RPC API
# common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
# uid = common.authenticate(db, username, password, {})
# models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
#
# new_contact_data = {
#     'name': 'shazan',
#     'email': 'ansarishazan48@gmail.com',
#     'phone': '1234567890',
#     "is_company": True,
#     # Add other contact fields here
# }
#
# # Create the new contact
# contact_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [new_contact_data])
#
# print("conatct id created with", contact_id)



# import xmlrpc.client
#
# url = "http://127.0.0.1:8069"
# db = "odoo_16_new"
# username = "ansarishazan48@gmail.com"
# password = "admin"
#
# # Connect to Odoo using the XML-RPC API
# common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
# uid = common.authenticate(db, username, password, {})
# models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
#
# # Create a new contact with an associated address
# new_contact_data = {
#     'name': 'abcsolution',
#     'email': 'ansarishazan48@gmail.com',
#     'phone': '1234567890',
#     "is_company": True,
#     # Create a list of addresses as child records
#     'child_ids': [
#         (0, 0, {
#             "type": "delivery",
#             "name": "Rohit",
#             "street": "State Highway 5",
#             "city": "Mumbai",
#             "zip": "12345",
#             "country_id": 104,  # Replace with the ID of the country (e.g., United States)
#             "is_company": True,
#         })
#     ],
# }
#
# # Create the contact with the associated address
# contact_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [new_contact_data])
#
# print("Contact with associated address created with ID", contact_id)

import xmlrpc.client

url = "http://127.0.0.1:8069"
db = "odoo_16_new"
username = "ansarishazan48@gmail.com"
password = "admin"

# Connect to Odoo using the XML-RPC API
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Prompt the user for the email to check
email_to_check = input("Enter the email address to add/update a contact: ")

# Check if a contact with the provided email already exists
existing_contact_id = models.execute_kw(db, uid, password, 'res.partner', 'search', [['|', ('email', '=', email_to_check), ('child_ids.email', '=', email_to_check)]])

if existing_contact_id:
    # Get the ID of the existing contact
    contact_id = existing_contact_id[0]
    print("Existing contact with ID", contact_id)

    # Automatically update the existing contact without specifying the name
    update_contact_data = {}
    models.execute_kw(db, uid, password, 'res.partner', 'write', [contact_id, update_contact_data])

    print("Updated existing contact with ID", contact_id)
else:
    # Create a new contact with the associated address
    new_contact_data = {
        'name': 'shazan',  # You can provide a default name here
        'email': email_to_check,  # Use the provided email
        'phone': '1234567890',
        "is_company": True,
        # Create a list of addresses as child records
        'child_ids': [
            (0, 0, {
                "type": "delivery",
                "name": "Rohit",
                "street": "State Highway 5",
                "city": "Mumbai",
                "zip": "12345",
                "country_id": 104,  # Replace with the ID of the country (e.g., United States)
                "is_company": True,
            })
        ],
    }

    # Create the contact with the associated address
    contact_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [new_contact_data])
    print("Created a new contact with associated address with ID", contact_id)
