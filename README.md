# Ruben Chung - Data Analyst Portfolio

## About Me

Hi, my name is Ruben Chung and I am an aspiring data analyst with a background in business as having direct exposure working in my family business. I hold an undergraduate degree in Supply Chain Management and a master's degree in Applied Business Analytics both from the University of Arkansas. I enjoy working with data to answer your business questions. I have experience that ranges from ETL processes, data visualization, data mining, advanced Excel, and Python. In addition to that, my domain expertise also involves sales, management, operations, transportation, and customer service.

This is a repository to showcase skills learned through academic, work, hobby, and internships.

## Table of Contents
- [About Me](#About-me)
- [Projects](#Projects)
   + [Automated Weather SMS](#Automated-Weather-SMS)
   + [Market Basket Analysis](#Market-Basket-Analysis)
   + [Tutoring Statistics Visualization](#Tutoring-Statistics-Visualization)
   + [Tableau Visualization](#Tableau-Visualization)
   + [Razorbacks Food Recovery](#Razorbacks-Food-Recovery)

    


## Projects
In this section I will list all my relevant projects with a brief description on what I did, the process behind that, and what I learned.

## Automated Weather SMS

<br>

**Code:** [`Weather_Scrapper.ipynb`](https://github.com/rfchungl/Projects-Portfolio/blob/main/Weather_Scrapping/Weather_Scrapper.py)

**The Python code has comments on what does each line do for a better understanding of the program.**

**Description:** When I arrived to the United States, there were days when I wore a sweater and jacket, and the day was not that cold. I felt very dumb walking down to my classes while other students were wearing t-shirts, shorts, and sandals. 
I know that we can check the weather on our cellphones. However, there is too much information like humidity, water density, weather variation between hours, air quality, etc. I wanted something simpler that could just tell me the weather condition and the temperature. I do not check my emails first thing in the morning, so I did not want them to be sent to my email. Instead, I wanted something quick like an SMS. 

**What does this program do?** This Python program scrap the weather data from Google depending on the location you put and is gathered through a few lines of Python code using the BeautifulSoup library. Then, it is send to your phone through a SMS service (A token is needed for this).

**Things needed to run the Python code:**
- import schedule
- import requests
- from bs4 import BeautifulSoup
- from twilio.rest import Client
- Token from Twilio (They offer 15 days trial)

<br>



**OUTPUT**

*The end result is once you have the program running, everyday at 7:00 AM in the morning will send you a SMS stating how is the weather condition and what you need to wear depending on how you coded it.*

![output](https://user-images.githubusercontent.com/115122030/196613363-0caf92c0-1be7-43bc-9597-c05c4fc980a7.PNG)





[Click here to get to the folder](https://github.com/rfchungl/Projects-Portfolio/tree/main/Weather_Scrapping)

## Market Basket Analysis
## Tutoring Statistics Visualization
## Tableau Visualization
## Razorbacks Food Recovery
