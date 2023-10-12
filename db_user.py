import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',  # Change to your PostgreSQL host if necessary
    'port': '5432',       # Change to your PostgreSQL port if necessary
}
print(db_params)
# User information
new_username = 'odoo_16_new'
new_password = 'admin'

try:
    # Connect to the PostgreSQL database as a superuser
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True  # Set autocommit to True to execute CREATE USER statement

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the CREATE USER statement
    cursor.execute(f"CREATE USER {new_username} WITH PASSWORD '{new_password}'")

    print(f"User '{new_username}' created successfully.")

except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
