import requests
from bs4 import BeautifulSoup
import time
from random import seed
from random import random
seed(1)
from twilio.rest import Client
import os
from decouple import config

#setup twilio (replace with your credentials)
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

#url List
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
buyButton = False
counter=0
while buyButton==False:
    page=requests.get(urls[counter])
    soup = BeautifulSoup(page.content,features="html.parser")
    content = soup.find("div", {"class": "label-1"})
    text=content.text.strip()
    print (urls[counter]+' '+text)
    

    if text=='Available':
        message = client.messages.create(body='Federal 9mm Available '+urls[counter],\
                            from_='+17816138682',to='+15128719350')
        print(message.sid)
        #buyButton=True
    if counter==(len(urls)-1):
        counter=0
    else:
        counter=counter+1
    time.sleep(1+(random()*2))
        




