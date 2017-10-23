

#print(response.text)  # result of setp-1
#print(articles)  # result of setp-2 ''' '''
#print(articles2)


# import requests
# from bs4 import BeautifulSoup

# url='http://rate.bot.com.tw/xrt?Lang=zh-TW'
# response=requests.get(url)
# #print(response.text)
# soup=BeautifulSoup(response.text,'lxml')
# articles=soup.find_all('span','time')
# for d in articles:
#     print ('牌價最新掛牌時間：'+d.getText())
import requests
from bs4 import BeautifulSoup

url = 'http://rate.bot.com.tw/gold/chart/year/TWD'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
articles = soup.find_all('data-local')

for article in articles:
    meta = article.find('div', 'title').find('a')

    title = meta.getText().strip()
    link = meta.get('href')
    push = article.find('div', 'nrec').getText()
    date = article.find('div', 'date').getText()
    author = article.find('div', 'author').getText()

    print(push, title, date, author,article)  # result of setp-3
'''
import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1477267200")
    ).strftime('%Y-%m-%d %H:%M:%S')
)
'''