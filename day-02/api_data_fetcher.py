import requests
import json

def fetch_public_holidays():
    # Taking inputs dynamically
    print("\n==========Inputs==========")
    year = int(input("Enter the year which you wish to see public holidays for(e.g.2020,2000,...etc):"))
    country_code = input("Enter the Country Code you wish to get public holidays for(e.g.GB,DE,AT):")

    # Storing the public sample api urls
    main_url = "https://date.nager.at/api/"
    varies_url = f"v3/publicholidays/{year}/{country_code}"

    # Combining both URLs
    print("\n==========Final URL==========")
    final_url = main_url + varies_url
    print(final_url)

    # Printing the response , we will be getting output as response code
    print("\n============Response with response code================")
    response = requests.get(url=final_url)
    print(response)

    # For getting the complete data present in api
    print("\n==============Data in JSON Form========================\n")
    print(response.json())

    # Knowing the type of the output data
    # type is of list so
    print("\n================Knowing the type of JSON Data================")
    print(type(response.json()))

    #storing it in holidays for ease use in further code
    holidays = response.json()

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
    json_data = json.dumps(public_holidays_list, indent=4)
    with open("output.json", "w") as file:
        file.write(json_data)
    print("Data is automatically gets saved in output.json")
    
#calling function
fetch_public_holidays()



