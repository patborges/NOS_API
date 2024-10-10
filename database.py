import mysql.connector
from mysql.connector import Error

def connect_to_database():
    mydb = mysql.connector.connect(
            host="localhost",
            user="user",
            password="example-password",
            database="geoloc",
            ssl_disabled=True
        )
    return mydb

def insert_data_into_database(api_responses):
    try:
        print("Connecting to database...")

        # Establishing the connection to MySQL
        mydb = connect_to_database()

        print("\nConnected to database!")
        cursor = mydb.cursor()
        
        # Prepare the SQL query for inserting data
        query = """
            INSERT IGNORE INTO cp_dist_conc (codigo_postal, concelho, distrito)
              VALUES (%s, %s, %s)
        """
        
        # Prepare data for batch insert
        data_to_insert = [
            (api_response[0].get("codigo-postal"),
              api_response[0].get("concelho"),
              api_response[0].get("distrito"))
            for api_response in api_responses if len(api_response) > 0
        ]

        # Perform batch insert if there is data to insert
        if data_to_insert:
            cursor.executemany(query, data_to_insert)
            mydb.commit()
            print(f"{cursor.rowcount} records inserted successfully!")
        else:
            print("No valid data to insert.")

    except Error as e:
        print(f"The error '{e}' occurred while inserting data.")
    finally:
        print("Database operation completed.")

def query_database_for_postal_code(postalcode):
    try:
        print("Connecting to database...")

        # Establishing the connection to MySQL
        mydb = connect_to_database()

        print("\nConnected to database!")
        cursor = mydb.cursor() 
        
        sql = "SELECT * FROM `geoloc`.`cp_dist_conc` WHERE codigo_postal = %s"
        cursor.execute(sql, [postalcode])

        result = cursor.fetchall()

        return result

    except Error as e:
        print(f"The error '{e}' occurred while inserting data.")
    finally:
        print("Database operation completed.")
        #print()