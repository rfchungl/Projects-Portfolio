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
   + [Country API](#Country-API)

    


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

<br>

**Code:** [`basket.py`](https://github.com/rfchungl/Projects-Portfolio/blob/main/MarketBasketAnalysis/basket.py)

**The Python code has comments on what does each line do for a better understanding of the program.**

**Description:** Using Excel and Python to analyze the data transactions from a bakery to understand the consumer behavior identifying what people buy and what they other item they usually pair with.

**What does this program do?** It first read the csv file named "basket.csv" then it runs association analysis through a few lines of codes using the mlxtend.frequent_patterns apriori and association_rules libraries.

**Things needed to run the Python code:**
- import pandas as pd
- from mlxtend.frequent_patterns import apriori
- from mlxtend.frequent_patterns import association_rules

<br>

### Part 1
**Analysis with Excel**

![image](https://user-images.githubusercontent.com/115122030/196620687-b6f18dc6-cafb-4b10-a3ae-dd32ac6993d6.png) <br>
*Capture 1*

First capture shows the top 5 items that are sold at Bread Basket. You can see that the undisputed top 1 is Coffee that almost quadruple the top 2 which is Tea.


![image](https://user-images.githubusercontent.com/115122030/196620755-c2e2432b-c6c1-40f6-8bc8-47e0a611bb6c.png) <br>
*Capture 2*

Second capture shows the years where Bread Basket was on operation. We clearly see that during 2016, December has the highest number of transactions. This could mean that because the winter season is cold, people tend to go and buy hot beverage to get warm. On the other hand, March of 2017 has the highest number of transactions which triples the amount in transactions from December of 2016. 


![image](https://user-images.githubusercontent.com/115122030/196620794-97d09767-4256-42bb-83a1-33bfec3c641d.png) <br>
*Capture 3*

Third capture shows a list of items ranked by margin gain. We can see that the top 5 most sold items in capture 1 are not as profitable as the one shown in the capture above. Although coffee and tea are within top 2 most sold, extra salami or feta and tartine get more margin.


![image](https://user-images.githubusercontent.com/115122030/196620841-bb6ec1df-4169-40d6-b64c-97354d8b4a4f.png) <br>
*Capture 4*

Last capture shows the time where the most sold items are bought. We can see that people tend to buy more tea between 2-3pm, cake between 2-3pm after lunch, sandwich between 1-2pm during lunch time, coffee between 10-1pm, and pastry between 10-11am. I thought that people would buy more coffee in the AM time but it seems that it’s very spread-out and the main time range are between 10-1pm.


### Part 2

![basket1](https://user-images.githubusercontent.com/115122030/196619281-acf26716-1593-4d0f-9b60-6fb53aaff9b3.png)
![basket2](https://user-images.githubusercontent.com/115122030/196619284-b262992c-c730-44cc-aeec-4e673f52e71f.png)

The association analysis using Python shows that the customer is 1.48 times more likely to buy toast then coffee than other customers. 

<br>

### Part 3

**Writing Recommendation**

To: Bread Basket Executives <br>
From: Ruben Chung, Data Analyst <br>
Subject: Break Basket Recommendations <br>

Based on the analyses performed, we found that the top 5 best-selling items are coffee, tea, cake, sandwich, and pastry. Coffee has by far the highest amount sold followed by tea. Interestingly, the time range where these two products are sold the most is between 10-1 pm for coffee and 2-3 pm for tea. Sandwich is best sold between 1-2 pm for lunchtime.


Although coffee and tea are not at the top when it comes to margin, they are good to draw customers when paired with other products such as cake, pastry, and bread, thus, increasing the amount spent by customers. We found that the highest pairing combo is coffee and pastry. On the other hand, we don’t recommend pairing tea and bread. In addition, we recommend discontinuing the sale of muffins as it has the least sale and customers don’t like them.


We recommend preparing enough coffee, tea, pastries, cakes, and sandwiches during the peak time using the time range to avoid stock out. Also, consider doing a marketing campaign that incentive customers to pair coffee or tea with any other products for a discount or loyalty points to increase Bread Basket’s revenue.


If you have any questions, please contact me at rfchungl@uark.edu. Your voice matters. 


Sincerely,


Ruben Chung







## Tutoring Statistics Visualization
<br>

**Visualization:** [`Click Here For Visualization`](https://datastudio.google.com/reporting/2004c153-b0d4-42e1-8bee-1f3c6eaa2fa8)

**Note:** The dataset was modified in order to protect the privacy of the tutors and students. The date of the sample dataset is from 08-23-2021 to 10-23-2021.

**Description:** Condensing all weekly CSV files from tutoring into a database and use it to feed the dashboard.

**Business Problem:** Because the administrator in charge to maintain the booking systems at the university left, nobody was in charge to maintain it. The database would break by itsel on days where a lot of web traffics happen. In order to prevent a disaster, the tutoring director decided to save the information of the booking appointments every week resulting in many CSV files. When there is a need to know something about tutoring, how many students came, what class was requested the most, etc, the director had to merge all the CSV files taking a lot of time just to get an answer. 

In order to reduce the time, I decided to condense all the CSV files into a database. In this case, I used free softwares to do that due to this being something that I purely wanted to do...not that I was required. Therefore, I chose the Google Analytics pack as the tools and used BigQuery to centralize all the booking informations and use DataStudio (Looker Studio) to provide visibility. Throughout my time working as a Graduate Assistant, I updated weekly the database once I was able to get to the CSV file.

## PROCEDURE ##

I could have done it two ways: <br>
  1- Merge all the CSV files into Excel file and upload it to BigQuery <br>
  2- Upload weekly CSV file into BigQuery <br>

To show the full functionality of how I maintained a database, I am going to showcase method #2.

### Part I ###

I created a bucket to save the CSV file digitally. Due to BigQuery being a web-based database, it cannot use your own desktop to find the path to the file you are going to upload.

![bucket](https://user-images.githubusercontent.com/115122030/197105095-d1c834f0-5db3-46f6-8b57-dabd267ed68f.JPG)

I was able to start the database with three weeks of data sample. After that, every week when I got the CSV file from the director, I would upload it into the bucket.

### Part II ###

Creating the database and setting up the schema.

![bigquery](https://user-images.githubusercontent.com/115122030/197105405-42d1f751-cdd6-42be-948f-881eaaa1f00e.JPG)

After creating the database in BigQuery, you can upload your first CSV file as the schema automatically or you can write by yourself.

### Part III ###

In order to maintain it, I had to do a weekly BigQuery update to load the weekly report from the director. 

[`Click Here For Queries`](https://github.com/rfchungl/Projects-Portfolio/blob/main/GoogleAnalytics/Load%20query.txt)


### Part IV ###

Finally, after having the database, I used Google DataStudio *(Locker Studio)* to visualize what we have about booking appointments.

![database](https://user-images.githubusercontent.com/115122030/197105946-446a7fe3-8e9f-4916-a0fb-35874e92f74a.JPG)

When selecting the source of the data in DataStudio, select BigQuery as the database and choose the path of your dataset. In this case, I already created it on Part II.

### Final Result ###

![image](https://images.squarespace-cdn.com/content/v1/6301adc291fbaf2a00843f8f/976c7dfb-22d3-461c-8599-d67442d20e2f/fall2021.PNG?format=1000w)




## Tableau Visualization

![image](https://user-images.githubusercontent.com/115122030/197111169-f2b55ce3-d415-4eea-a218-f8f9336b1513.png)

![image](https://user-images.githubusercontent.com/115122030/197111182-05ca7156-cb8e-4499-aa2f-1f24f04cfe04.png)

## Razorbacks Food Recovery

**Visualization:** [Click Here](https://datastudio.google.com/reporting/7e07a668-6ba8-48b5-ba8f-66a59e632d09)

**Description:** The RFR program works with Chartwells Dining Service on campus to recover unused food from the dining halls and retail locations on campus and donate the recovered food to local non-profit organizations in the Fayetteville Area. By tracking the amount of food waste generated by various dining halls and food types and communicating this information to Chartwells, RFR aim to reduce food waste at the source while alleviating food insecurity in the community. By utilizing and manipulating this data, RFR and Chartwells hope to find significant results, which will improve the inventory forecasting accuracy and food preparation for the Chartwells Organization.

**Challenges:**
  + **Messy data:** 19,000+ rows of transactions which around 18,000 are similar type with different wordings. For example: <br>
    - Row 1 - chicken with pasta <br> 
    - Row 2 - pasta with chicken
  + **Inconsistent recollection of data:** They gather the information through a Google form. However, the selections are typed leading into data inconsistensy.
  + **Inconsistent gathering:** They do not have a specific time to gather and recover food due to lack of volunteers.

  
  **Resolve:** I am going to provide solution to the first two main points.
  
  ### PROCEDURE ###
  
  **Dataset At First Glance:**
  
  ![image](https://user-images.githubusercontent.com/115122030/197115533-7cecebc8-723d-4bab-8b5a-5c22e7184ae0.png)

As you can see on row 59 and 60 they are basically the same, however, because different volunteers type differently, it may have slight difference in the information entered (the same between vegetables and vetagatables row 73 and 74). You can see this issue in the 19,000+ rows of transactions due to not having a standard or rules when inputting the information.

**Data Cleansing**

I used two ways to cleanse the dataset and I worked by block. By that I mean I categorized them by food group then worked on standardizing the food names based on the food group. I some part I used Excel to create the food category and some part I used SAS EG to do the big bulk of cleansing. <br>

[You can see my work here](https://github.com/rfchungl/Projects-Portfolio/blob/main/datamanagementplan.txt)

Cleansing and formatting was the toughest part of the project. Once I was done with this, the rest was a walk in the park.

**Exploratory Analysis**

![image](https://user-images.githubusercontent.com/115122030/197117003-07605f1c-7f1e-4115-9f1f-64b342326d9d.png)

Once I knew that the formatting was good and everything was clean, I played around to see if what I did made sense. Afterwards, it was time to move to the second business problem which was to standardize their data collection.

**Data Standardization**

Since RFR works with volunteers and they prefer using Google form, I thought of using it as the database to get live visualization as soon as they input the information. In order to do that, I asked them for their Google form, and I revamped that using multiple choices to avoid typos and duplicates. Because Google form cannot be a database, I connected the Google sheets file that collect the information from the form to connect to Google DataStudio and added the cleaned dataset on it.

[Click here to see the form](https://docs.google.com/forms/d/e/1FAIpQLSdoHmsIy-Mq_2_qBD71eGjgNKaG16-A_lFXSNpRhqCYIhi8KQ/viewform)

**How Does It Work?**

Once the volunteer inputs the information in the Google form, it will be capture in the sheets combining it with the cleaned dataset.

![form](https://user-images.githubusercontent.com/115122030/197118479-9fc8c8f4-0440-457a-a717-88de79433565.JPG)

**Result**

The result is that once a form is introduced, it will be shown in the dashboard. Cleaning the dataset and standardizing the way the data is capture will make it easier for RFR spend their time to analyze the trends instead of spending time cleansing.



## Country API
<br>

**Code:** [`API.ipynb`](https://github.com/rfchungl/Projects-Portfolio/blob/main/API/API.py)

**The Python code has comments on what does each line do for a better understanding of the program.**

**Description:** Using API and JSON library to create a Python program.

**What does this program do?** The Python code is based on an API that shows you the college names based on the country you type. Once the user type the country name, it asks the API to retrieve the college names, in order to save them, we gather the results in JSON then use python dictionary to print the results.

**Things needed to run the Python code:** <br>
import urllib.request <br>
import json <br>

<br>

**OUTPUT**

![image](https://user-images.githubusercontent.com/115122030/197109556-754f44ee-aded-4dd7-84c3-ba5494afdacc.png)




