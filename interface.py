from database import query_database_for_postal_code

# 1º Define a function to ask the user for input
def ask_input():
    return input("Choose a postal code: ")

# 2º Define a function to search for the input in the database
def search_postal_cod(input):
    return query_database_for_postal_code(input)

# 3º Define a function to print the search result
def print_results(result): # [ (213, '7750-104', 'Mértola', 'Beja') ]
    if result is None or len(result) <= 0:
        print("Couldn't find CP")
    else:
        print("id:", result[0][0]) 
        print("codigo postal:", result[0][1])
        print("concelho:", result[0][2])
        print("distrito:", result[0][3])

# Define the main function
def main():
    input = ask_input()
    result = search_postal_cod(input)
    print_results(result)
    print("\n~ The End ~")

# Call the main function to start the program
main()
# 7750-104  <-- example code 