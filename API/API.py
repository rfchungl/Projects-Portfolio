# import library to request info from an API
import urllib.request
# import JSON module
import json

print('BROWSE UNIVERSITIES FROM DIFFERENT COUNTRIES')
# as long as the user doesn't type x then this program will keep running
while True:
    # ask user to enter a country
    country = input('Enter country or enter "x" to exit: ')
    # if user inputted letter x then end the program
    if country == 'x': 
        quit() 

    # url of the API + the input of what the user typed. In this case, the name of the country
    url = "http://universities.hipolabs.com/search?country=" + country

    # url can't have space, I added this so that the user can input countries with space in between such as United States, United Kingdom, Saudi Arabia, United Arab Emirates, etc
    urlreplace = url.replace(" ","%20")
    
    # requesting JSON data from the API
    json_data = urllib.request.urlopen(urlreplace)
    
    # convert the JSON to Python Dictionary
    data = json.loads(json_data.read()) 

    # if user doesn't type the country name correctly, it will keep prompting "Please enter a valid country"
    if len(data) == 0:
        print('Please enter a valid country!')
    else:
        for item in data:
            print(item['name'])