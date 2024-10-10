#### NOS / Specialistern project 
 
This project is a practical exercise aimed at enriching our company's geolocation data by providing additional information such as municipality (Concelho) and district (Distrito) for a given set of postal codes.

### Project Overview
The goal of this project is to develop a solution that complements a dataset with additional geolocation information, specifically municipality and district, based on a list of postal codes.

### Instructions
## 1. Input Data
. You will be provided with a CSV file containing a list of postal codes.

## 2. Task
. Using online resources such as postal code information websites, search tools, or publicly available APIs, find and append the corresponding municipality (Concelho) and district (Distrito) information for each postal code in the dataset.

## 3. Process
. Develop a script or program that automates the process of searching and enriching the postal code data.
. For each postal code in the provided CSV, append the municipality and district information.

## 4. Data Storage
. The final output should be stored in a database table (e.g., MySQL, MariaDB, PostgreSQL, etc.).
. The minimum table structure should include the following fields:
    . Postal Code
    . Municipality (Concelho)
    . District (Distrito)

## 5. Data Access
. In addition to SQL access to the final table, an API service should be implemented to allow other teams to access the data.

## 6. Deliverables
. Make the developed code available on GitHub and share the project link.
. Submit the enriched CSV file with the additional geolocation information.
. Provide a test report.

### Test Report
The test report should include:

. A list of designed test cases, identifying the functionality being tested, the actions to be executed, and the expected result.
. Identification of tests that have been executed, along with the result of each test (pass or fail).
. A list of any defects or non-conformities encountered during the tests, including the severity, description of the issue, and resolution status.

### Suggestion
. We recommend using Python for automation in this project.