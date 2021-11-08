from bs4 import BeautifulSoup
import requests
import lxml
import json
def take_usd():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
    }
    r = requests.get(url = 'https://www.banki.ru/products/currency/rub/' , headers = headers)
    with open('data/usd.html' , 'w') as file :
        temp = file.write(r.text)
    with open('data/usd.html' , 'r') as file :
        src = file.read()
    soup = BeautifulSoup(src , 'lxml')
    usd = soup.find(class_= 'currency-board__table').find('span',class_='currency-board__value').text
    oil = ''
    cours = {
        ' 1 долар =  ' : usd
    }
    with open('data/usd.json' , 'w') as file:
        json.dump(cours, file, indent=4 , ensure_ascii=False)


take_usd()