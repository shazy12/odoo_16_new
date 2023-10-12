import xmlrpc.client
# import xmlrpclib
# Odoo server information for localhost
# url = 'http://localhost:8069/xmlrpc/2/'
# db = 'odoo_16_new'
# username = 'ansarishazan48@gmail.com'  # Replace with your Odoo username
# password = 'admin'

url = "http://127.0.0.1:8069"
db = "odoo_16_new"
username = "ansarishazan48@gmail.com"
password = "admin"

# common = xmlrpc.client.ServerProxy('{}/common'.format(url))
# print("common", common)
# uid = common.authenticate(db, username, password, {})
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/object'.format(url))

def add_customer(new_contact_data):
    """
    Add a new contact (customer) to the res.partner model.
    :param new_contact_data: Dictionary with the new contact's data
    """
    # Check access rights for creating a partner (contact)
    if not models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['create'], {'raise_exception': False}):
        print("No create access rights for 'res.partner'")
        return

    # Create a new contact (customer)
    new_contact_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [new_contact_data])
    print("Customer added successfully. ID:", new_contact_id)

# Test the function
new_contact_data = {
    "name": "qwe Solutions",
    "email": "azsolutions@gmail.com",
    "phone": "+91 9876543210",
    "is_company": True,
    # Add more fields as needed
}

add_customer(new_contact_data)
