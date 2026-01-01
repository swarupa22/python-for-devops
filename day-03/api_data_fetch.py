import requests
import json

def fetch_public_holidays():
    print("\n==========Inputs==========")
    
    # Using try block here as the inputs might cause an exception if user gives any negative ,alphabet or special character values
    try:
        year = int(input("Enter the year which you wish to see public holidays for(e.g.2020,2000,...etc):"))

       
        # Using raise for raising exceptions on certain inputs
        if year<=0 or len(str(year))!=4:
            raise ValueError("Year have to be positive & 4 digits")
        
        country_code = input("Enter the Country Code you wish to get public holidays for(e.g.GB,DE,AT):").upper()
        
        if not country_code.isalpha() or len(country_code)!=2 :
            raise ValueError("Country Code should contains 2 alphabetical values")

    except ValueError as ve:
        print("Value Error Exception Raised :",ve)
        print(print("Invalid ! Please type correct values again\n"))
        return
        
    main_url = "https://date.nager.at/api/"
    varies_url = f"v3/publicholidays/{year}/{country_code}"
    print("\n==========Final URL==========")
    final_url = main_url + varies_url
    print(final_url)
    
    print("\n============Response================")
    
    # Using try block here as the response might cause an exception if api request got timed out , failed connection
    try:
        response = requests.get(url=final_url, timeout = 10)
        response.raise_for_status()
        
    except requests.exceptions.Timeout as to:
        print("API Exception raised:",to)
        return

    except requests.exceptions.ConnectionError as ce:
        print("API Exception raised:",ce)
        return

    except requests.exceptions.RequestException as re:
        print("API Exception raised:", re)
        return
    
    print("\n============Response with response code================")
    print("Status Code:", response.status_code)
        
    print("\n==============Data in JSON Form========================\n")
    
    # Using try block here as the response might cause an exception of not retrieving the data
    try:
        holidays = response.json()
    except ValueError:
        print("Failed to parse JSON data")
        return

    # created a list for storing all public holidays
    public_holidays_list = []
    print("\n ===============Public Holidays==================")

    for hd in holidays:
        data = {
            "Date" : hd["date"],
            "Local_Holiday_Name" : hd["localName"],
            "Holiday_Name" : hd["name"],
            "Country" : hd["countryCode"]
            }
        public_holidays_list.append(data)

    # Saving the processed data into JSON file using file write
    print("\n ===============FILE WRITE==================")
    
    # Using try block here it might cause an exception if file is not found for writing
    try:
        json_data = json.dumps(public_holidays_list, indent=4)
        with open("output.json", "w") as file:
            file.write(json_data)
        print("Data is automatically gets saved in output.json")
    
    except FileNotFoundError as fe:
        print("FileNotFound Exception raised:",fe)
    
#calling function
fetch_public_holidays()

