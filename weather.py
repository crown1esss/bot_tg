from bs4 import BeautifulSoup
import requests
import lxml
import json
def take_weather():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
    }
    r = requests.get(url = 'https://www.mos.ru/lp/pogoda/' , headers = headers)
    with open('data/weather.html' , 'w') as file :
        temp = file.write(r.text)
    with open('data/weather.html' , 'r') as file :
        src = file.read()
    soup = BeautifulSoup(src , 'lxml')


    temperature  = soup.find('div' , class_='weather__now-info').find('p' , class_='weather__now-temperature').text
    feeling = soup.find('div' , class_='weather__now-info').find('p' , class_='weather__now-feel').text.split('\n').pop().strip()
    condition  = soup.find('div', class_='weather__now-info').find('p', class_='weather__now-cloudiness').text
    weather = {
        'Температура :' : temperature,
        'Ощущается как :' : feeling,
        'Над головой :' : condition
    }
    with open('data/weather.json' , 'w') as file:
        json.dump(weather , file, indent=4 , ensure_ascii=False)


take_weather()