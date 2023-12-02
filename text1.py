'''
import requests
from bs4 import BeautifulSoup
import time
stock=["1101","5009"]

for i in range(len(stock)):
  stockid=stock[i]
  url='https://tw.stock.yahoo.com/quote/'+stockid+'.TW'
  r=requests.get(url)
  soup=BeautifulSoup(r.text,'html.parser')
  price=soup.find('span',class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])

  if price==None:
    url='https://tw.stock.yahoo.com/quote/'+stockid+'.TWO'
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    price=soup.find('span',class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])
  price=price.getText()

message="股票"+stockid+"及時股價"+price
token='6867474346:AAFwTNDldNsLxX10jhI-G6zWxER1q4QLxnk'
chat_id='6431659328'
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
requests.get(url)
time.sleep(3)
'''
