import os

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ST_APIKEY = os.environ["stock_api_key"]
NEWS_APIKEY = os.environ["news_api_key"]
ACCOUNT_SID = os.environ["account_sid"]
AUTH_TOKEN = os.environ["auth_token"]


def check_percent():
    st_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ST_APIKEY,
    }
    close_data = []
    response = requests.get(url="https://www.alphavantage.co/query", params=st_parameters)
    data = response.json()["Time Series (Daily)"]
    for i in data:
        if len(close_data) < 2:
            close_data.append(data[i])

    yesterday_data = float(close_data[0]["4. close"])
    before_yesterday_data = float(close_data[1]["4. close"])
    return round(((yesterday_data - before_yesterday_data) / yesterday_data) * 100, 2)


def stock_has_extra_activity(number):
    if -5 >= number >= 5:
        return True


def get_news():
    news_parameters = {
        "apiKey": NEWS_APIKEY,
        "q": COMPANY_NAME,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3,
    }
    headlines = []
    breifs = []
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()
    news_slice = news_data["articles"][:3]
    sms_body = ""
    if percent > 0:
        sms_body = f"{STOCK}: 🔺{percent}\n"
    elif percent < 0:
        sms_body = f"{STOCK}: 🔻{abs(percent)}\n"
    for i in range(3):
        headlines.append(news_slice[i]["title"])
        breifs.append(news_slice[i]["description"])
    for i in range(3):
        sms_message = f"Headline:{headlines[i]}\n" \
                      f"Brief: {breifs[i]}\n\n"
        sms_body += sms_message
    return sms_body


def send_sms(text):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body=f"{text}",
        from_='+15312344611',
        to='+358449181656'
    )
    print(message.status)


percent = check_percent()
if stock_has_extra_activity(percent):
    sms_text = get_news()
    send_sms(sms_text)
