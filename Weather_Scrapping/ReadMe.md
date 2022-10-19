## Automated Weather SMS

<br>
**Code:** [`Weather_Scrapper.ipynb`](https://github.com/rfchungl/Projects-Portfolio/blob/main/Weather_Scrapping/Weather_Scrapper.py)

**Description:** When I arrived to the United States, there were days when I wore a sweater and jacket, and the day was not that cold. I felt very dumb walking down to my classes while other students were wearing t-shirts, shorts, and sandals. 
I know that we can check the weather on our cellphones. However, there is too much information like humidity, water density, weather variation between hours, air quality, etc. I wanted something simpler that could just tell me the weather condition and the temperature. I do not check my emails first thing in the morning, so I did not want them to be sent to my email. Instead, I wanted something quick like an SMS. 

**What does this program do?** This Python program scrap the weather data from Google depending on the location you put and is gathered through a few lines of Python code using the BeautifulSoup library. Then, it is send to your phone through a SMS service (A token is needed for this).

**Things needed to run the Python code:**
- import schedule
- import requests
- from bs4 import BeautifulSoup
- from twilio.rest import Client

# First

