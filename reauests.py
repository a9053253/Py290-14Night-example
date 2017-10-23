import requests
from bs4 import BeautifulSoup

url='http://rate.bot.com.tw/xrt?Lang=zh-TW'
response=requests.get(url)
#print(response.text)
soup=BeautifulSoup(response.text,'lxml')
articles=soup.find_all('span','time')
for d in articles:
    print ('牌價最新掛牌時間：'+d.getText())
table=soup.find('table','table table-striped table-bordered table-condensed table-hover').find('tbody').find_all('tr')

for data in table:
    money_name=data.find('div','visible-phone print_hide').getText().strip()
    cash_in=data.find('td',attrs={'data-table': '本行現金買入'}).getText()
    cash_out=data.find('td',attrs={'data-table': '本行現金賣出'}).getText()
    now_in=data.find('td',attrs={'data-table': '本行即期買入'}).getText()
    now_out=data.find('td',attrs={'data-table': '本行即期賣出'}).getText()
    print(money_name+'  '+cash_in+'  '+cash_out+'  '+now_in+'  '+now_out)
