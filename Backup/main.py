import csv
import requests
import time
from database import insert_data_into_database


# ------ API -------
# API: https://www.cttcodigopostal.pt/api/v1/4074c2cf8cc941e9baafa631a4dac171/8005-127
# API-KEY: 4074c2cf8cc941e9baafa631a4dac171
# ALTERNATIVE: https://www.codigo-postal.pt/?cp4={cp4}&cp3={cp3}

api_url = "https://www.cttcodigopostal.pt/api/v1"
api_key = "4074c2cf8cc941e9baafa631a4dac171"

# List to save responses from API
api_responses = []


# Open the input CSV file
with open("codigos_postais.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    count = 0

    # Extract postal code (CP7)
    for row in reader:
        cp = row["cp7"]
        print(row)

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

# Write data to CSV file (structure: cp7,concelho,distrito)
with open("codigos_postais_filled.csv", "w", newline="") as csvfile:

    print("CSV opened, atempting to write...")

    # Starting to write with header
    writer = csv.DictWriter(csvfile, fieldnames=["cp7", "concelho", "distrito"])
    writer.writeheader()

    # Cycling through each response to write each row
    for api_response in api_responses:

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


# Write data to MySQL database
insert_data_into_database(api_responses)


print("\n~ The End ~")

