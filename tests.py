
############### Test cases: ###############
# Test 1: CSV file reading                #
# Test 2: API request                     #
# Test 3: CSV file writing                #
# Test 4: Database integration            #
###########################################

import unittest
from unittest.mock import patch, mock_open
import csv
import requests     # for API requests
import json
from io import StringIO

# Mock function to be tested: Fetches data from API
def fetch_geolocation_data(api_url, cp):
    try:
        cp4, cp3 = cp.split('-')
        response = requests.get(f'{api_url}/{cp4}/{cp3}')
        if response.status_code == 200:
            # Error ----
            return response.json().get('concelho', 'N/A'), response.json().get('distrito', 'N/A')
            # ----------
        return None, None
    except ValueError:
        return None, None

# Test cases
class TestGeolocationEnrichment(unittest.TestCase):
    
    # Test 1: CSV file reading
    @patch("builtins.open", new_callable=mock_open, read_data="cp7\n1000-001\n")
    def test_csv_read(self, mock_open_file):
        with open("codigos_postais.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            codigo_postal = [row["cp7"] for row in reader]
        
        self.assertEqual(codigo_postal, ["1000-001"])


    # Test 2: API request
    @patch('requests.get')
    def test_api_request(self, mock_get):
        # Mock a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"codigo-postal": "1000-001", "concelho": "Lisboa", "distrito": "Lisboa"}
        
        api_response = fetch_geolocation_data("https://www.cttcodigopostal.pt/api/v1/4074c2cf8cc941e9baafa631a4dac171", "1000-001")

        self.assertEqual(api_response[0], "Lisboa")
        self.assertEqual(api_response[1], "Lisboa")


    # Test 3: CSV file writing
    @patch("builtins.open", new_callable=mock_open)
    @patch("csv.DictWriter")
    def test_csv_file_writing(self, mock_csv_writer, mock_open_file):
        api_responses = [{'cp7': '1000-001', 'concelho': 'Lisboa', 'distrito': 'Lisboa'}]

        with open("codigos_postais_filled.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["cp7", "concelho", "distrito"])
            # fail ----
            writer.writeheader()
            for api_response in api_responses:
                writer.writerow(api_response)

        mock_open_file.return_value.write.assert_called()  # Ensure write was called
        # -------------

    # Test 4: Database integration (Mock database insert)
    @patch("mysql.connector.connect")
    def test_database_integration(self, mock_connect):
        # Assume we are inserting a single row into the database
        codigo_postal = '1000-001'
        concelho = 'Lisboa'
        distrito = 'Lisboa'

        # Simulate database connection and insertion
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # SQL command
        sql_query = f"""
            INSERT INTO cp_dist_conc (codigo_postal, concelho, distrito)
            VALUES ('{codigo_postal}', '{concelho}', '{distrito}')
        """

        mock_cursor.execute.return_value = None  # Simulate success

        # Perform the operation
        mock_cursor.execute(sql_query)

        # Assert that the SQL insert was called
        mock_cursor.execute.assert_called_once_with(sql_query)

if __name__ == "__main__":
    unittest.main()
