import mysql.connector

# Replace these values with your database credentials
database_host = "localhost"
database_user = "ktmehta"
database_password = "Kartik@123"

# Connect to the MySQL server
try:
    conn = mysql.connector.connect(
        host=database_host,
        user=database_user,
        password=database_password
    )

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # Create the database
    database_name = "maid_info"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

    # Select the database
    cursor.execute(f"USE {database_name}")

    # Create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS maids (
        id INT AUTO_INCREMENT PRIMARY KEY,
        maid_name VARCHAR(100) NOT NULL,
        contact_number VARCHAR(20) NOT NULL,
        available_slots VARCHAR(100),
        comments TEXT,
        cost_per_day DECIMAL(8, 2),
        cost_per_month DECIMAL(8, 2),
        sunday_availability VARCHAR(3),
        language VARCHAR(50)
    )
    """
    cursor.execute(create_table_query)

    print("Database and table created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
