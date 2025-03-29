import requests

def convert_curency(amount, from_currency, to_currency): # Create a function to convert currency
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}" # Create a URL to get the exchange rate
    response = requests.get(url) # Get the response from the URL
    data = response.json() # Convert the response to JSON
    
    if to_currency in data['rates']:
        converted_amount = amount * data['rates'][to_currency] # Convert the currency
        return converted_amount
    else:
        return "Invalid Currency Code"

# Get data from the user
amount = float(input("Enter the amount: ")) # Get the amount from the user
from_currency = input("From Currency: ").upper() # Convert the currency to uppercase
to_currency = input("To Currency: ").upper() # Convert the currency to uppercase

# Call the function and print the result
print(f"Converted Amount: {convert_curency(amount, from_currency, to_currency)}") # Print the result using function