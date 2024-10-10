import csv
import requests
import time
from database import insert_data_into_database


# ------ API -------
# API: https://www.cttcodigopostal.pt/api/v1/4074c2cf8cc941e9baafa631a4dac171/8005-127
# API-KEY: 4074c2cf8cc941e9baafa631a4dac171
# ALTERNATIVE: https://www.codigo-postal.pt/?cp4={cp4}&cp3={cp3}


# Define a function to read data from a CSV file
def read_csv(file_name):
    data = []
    # Open the input CSV file
    with open(file_name, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row["cp7"])
    return data
 

# Define a function to make API requests and fetch data
def fetch_data(api_url, api_key, postal_codes):
    # List to save responses from API
    api_responses = []
    count = 0
    for cp in postal_codes:
        try:
            count = count + 1
            if count > 28:
                print("RATELIMIT. Please wait...")
                time.sleep(59) # 30 requests per minute limit
                count = 0

            # Make request to API in https://www.cttcodigopostal.pt/api with postal code
            response = requests.get(f"{api_url}/{api_key}/{cp}")

            # Check if response is OK (Code 200)
            if response.status_code == 200:
                api_responses.append(response.json())
                print("Response OK")
            else:
                print(f"Error: {response.status_code} - {response.reason}")

        except ValueError:
            print(f"Invalid postal code format")
    return api_responses

# Define a function to write data to a CSV file
def fill_csv(file_name, data):
    # Write data to CSV file (structure: cp7,concelho,distrito)
    with open(file_name, "w", newline="") as csvfile:
        print("CSV opened, atempting to write...")

        # Starting to write with header
        writer = csv.DictWriter(csvfile, fieldnames=["cp7", "concelho", "distrito"])
        writer.writeheader()

        # Cycling through each response to write each row
        for api_response in data:

            # If response is not empty
            if len(api_response) > 0:

                # Get each relevant field to write to CSV
                writer.writerow(
                    {
                        "cp7": api_response[0].get("codigo-postal"),
                        "concelho": api_response[0].get("concelho"),
                        "distrito": api_response[0].get("distrito"),
                    }
                )
        print("\nCSV is filled with data.")


# Define the main function
def main():
    api_url = "https://www.cttcodigopostal.pt/api/v1"
    api_key = "4074c2cf8cc941e9baafa631a4dac171"
    file_name = "codigos_postais.csv"
    output_file_name = "codigos_postais_filled.csv"
    
    postal_codes = read_csv(file_name)
    api_responses = fetch_data(api_url, api_key, postal_codes)
    fill_csv(output_file_name, api_responses)
    insert_data_into_database(api_responses)
    print("\n~ The End ~")

# Call the main function to start the program
main()