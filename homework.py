import requests

url = "https://eubank.kz/exchange-rates/?lang=en"

response = requests.get(url)

if(response.status_code == 200):
    print("Успешное подключение")
else:
    print("Не удалось подключиться", response.status_code)


from bs4 import BeautifulSoup

html = response.text

soup = BeautifulSoup(html, 'html.parser')

print("Курс валют, введите свою валюту")
value = input() #USD, EUR, RUB, GBP(Pound Sterling), CHF(Swiss Frank), CNY(Chinese Yuan), KGS(Kyrgyz Som)


rows = soup.findAll("td")

for row in rows[0:7]:
    name_tag = row.find("span", class_= "exchange-table__title")
    price_tag = row.find("span", class_="exchange-table__value")
    if(value == name_tag.text):
        print(f"{price_tag.text} тенгe")