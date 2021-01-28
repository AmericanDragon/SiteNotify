import requests
from bs4 import BeautifulSoup
import time
from random import seed
from random import random
seed(1)
from twilio.rest import Client

from decouple import config

from datetime import datetime

#list of URLs of ammo pages you'd like to check on federal's website. default is all 9mm practice ammo. change as needed to your preferred ammo.
urls=['https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun/11-AE9AP.html',\
          'https://www.federalpremium.com/handgun/federal-target/champion-training/11-WM5199.html',\
          'https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun/11-AE9DP100.html',\
          'https://www.federalpremium.com/handgun/syntech/syntech-action-pistol/11-AE9SJAP1.html',\
          'https://www.federalpremium.com/handgun/syntech/syntech/11-AE9SJ2.html',\
          'https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun/11-AE9DP.html',\
          'https://www.federalpremium.com/handgun/premium-personal-defense/practice-and-defend/11-P9HST1TM100.html',\
          'https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun/11-AE9FP.html',\
          'https://www.federalpremium.com/handgun/american-eagle/american-eagle-indoor-range-training-lead-free/11-AE9LF1.html',\
          'https://www.federalpremium.com/handgun/train-protect/train-protect/11-TP9VHP1.html',\
          'https://www.federalpremium.com/handgun/syntech/syntech/11-AE9SJ1.html',\
          'https://www.federalpremium.com/handgun/american-eagle/american-eagle-indoor-range-training/11-AE9N1.html',\
          'https://www.federalpremium.com/handgun/american-eagle/american-eagle-indoor-range-training/11-AE9N2.html',\
          'https://www.federalpremium.com/handgun/syntech/syntech-training-match/11-AE9SJ4.html',\
          'https://www.federalpremium.com/handgun/syntech/syntech-training-match/11-AE9SJ3.html',\
          'https://www.federalpremium.com/handgun/premium-personal-defense/practice-and-defend/11-P9HST2TM100.html',\
          'https://www.federalpremium.com/handgun/syntech/syntech-pcc/11-AE9SJPC1.html',\
          'https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun-suppressor/11-AE9SUP1.html'
          ]

#main function to check each URL in sequence and text if "available"
def rotate(urls):
    #setup twilio (replace with your credentials)
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
     
    buyButton=False
    counter=0
    while buyButton==False:
            page=requests.get(urls[counter])
            soup = BeautifulSoup(page.content,features="html.parser")
            content = soup.find("div", {"class": "label-1"})
            text=content.text.strip()
            print (urls[counter]+' '+text)
			
			#code below is to text via twilio to you for notification. replace numbers with your own.
            if text=='Available':
                message = client.messages.create(body='Federal 9mm Available '+urls[counter],\
                                from_='TWILIO GIVEN NUMBER',to='YOUR NUMBER')
                print(message.sid)
				#uncomment below code to stop from running once available ammo is found. otherwise, code will continue to notify
				#buyButton=True
            if counter==(len(urls)-1):
                counter=0
            else:
                counter=counter+1
			#default is to wait 1-3 secs between requests. can change to faster or slower
            time.sleep(1+(random()*2))
def main():
	#try catch block to sleep when connection times out. currently set to sleep for 30-40 seconds before retrying. change if not working
    try:
        rotate(urls)
    except:
        now = datetime.now()
        print("error occured at "+now.strftime("%m/%d/%Y %H:%M:%S")+", sleeping for 30-40 seconds")
        time.sleep(30+(random()*10))
        rotate(urls)

main()






