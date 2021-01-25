import time

from twilio.rest import Client
from random import seed
from random import randint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from dotenv import load_dotenv

from decouple import config

#setup twilio (replace with your credentials)
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


#Initiate the Browser
browser =webdriver.Chrome(ChromeDriverManager().install())

#url List
urls=['https://www.sigsauer.com/9mm-124gr-elite-ball-fmj.html',\
      'https://www.sigsauer.com/9mm-115gr-elite-ball-365-fmj.html',\
      'https://www.sigsauer.com/9mm-p-124gr-elite-ball-m17-fmj-box-50.html',\
      'https://www.sigsauer.com/9mm-147gr-elite-ball-fmj.html',\
      'https://www.sigsauer.com/9mm-115gr-elite-ball-fmj.html']
buyButton = False

x=0
while not buyButton:
        try:
                
                browser.get(urls[x])
                notificationform = browser.find_element_by_xpath("//form[@id='form-validate-stock']")
                print("Button isn't ready yet")
                time.sleep(randint(0,5))
                if x==(len(urls)-1):
                        x=0
                else:
                        x=x+1
        except:

                addToCartBtn = addButton = browser.find_element_by_id("product-addtocart-button")
                #addToCartBtn.click()
                print("Buy Available")
                message = client.messages.create(body='Sig 9mm Available '+urls[x],\
                            from_='+17816138682',to='+15128719350')
                print(message.sid)
                buyButton = True




