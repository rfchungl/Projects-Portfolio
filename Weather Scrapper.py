# module to schedule 
import schedule
# requests module to get API or links
import requests
# module to extract data from html and xml
from bs4 import BeautifulSoup
# module to run sms
from twilio.rest import Client

# things needed to get my sms going
account_sid = "AC20670c5474b8ea4fef73615b2882c7d8"
auth_token  = "478fc6b2f03de7a329eb6f3330f92c3e"
# authenticator to get to twilio
client = Client(account_sid, auth_token)

# defining the block of code as weathercondition
def weathercondition():
	# weather city
	city = "Fayetteville"
		
	# creating url and requests instance
	soup = BeautifulSoup(requests.get(f'https://www.google.com/search?q=weather+in+{city}').text, "html.parser")
	#print(soup.prettify())
	
	# catching what I need from beautiful soup and defining my variables
	temperature = soup.find('div', class_= 'BNeawe iBp4i AP7Wnd').text # BNeawe iBp4i AP7Wnd is obtained by inspecting and finding the line that contains the temperature
	region = soup.find('span', class_= 'BNeawe tAd8D AP7Wnd').text # BNeawe tAd8D AP7Wnd is obtained by inspecting and finding the line that contains the region (Fayetteville, AR)
	day_and_weather = soup.find('div', class_= 'BNeawe tAd8D AP7Wnd').text # BNeawe iBp4i AP7Wnd is obtained by inspecting and finding the line that contains the day and type of weather

	# day_and_weather will print the day, hour, and the type of weather...I only need the weather condition so I split and print index 1
	condition = day_and_weather.split('\n')[1]

	# these lines were used to check if it would print what I wanted
	# print(temperature.text)
	# print(region.text)
	# print(day_and_weather.text)

	# here is the condition needed to send me the sms. As long as the condition type is not 0, it will always send me a sms with the weather condition
	# alternatively, if I wanted it to send me a sms when on rainy days, I could do that too
	# unfortunately, if you want to change the number to sent, you will have to pay as this is a free trial
	if condition != 0:
		message = client.messages.create(to="+14795026472", from_="+16084475947", body=f"Good morning, Ruben!\nWeather condition for today is {condition} and temperature is {temperature} in {region}.")
		print(message.sid)
		print("Message Sent!")

# every day at a specific time will send me a sms reminder of the weather and weathercondition() is called. In my case, I will set it up when I wake up at 7:00AM
schedule.every().day.at("07:00").do(weathercondition)
# as long as the condition is true, it will run
while True:
	schedule.run_pending()

