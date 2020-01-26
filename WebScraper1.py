import requests
import smtplib #this library enables emails to be sent

from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Google-Pixelbook-Chromebook-64GB-Black/dp/B07YMGQYP6/ref=sr_1_3?keywords=pixelbook&qid' \
      '=1579924237&sr=8-3&th=1 '

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.130 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")  #first soup tricks amazon's html written in Javascript

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")  #second soup actually loads the html

    title = soup2.find(id="productTitle").get_text()  #this pulls the title directly from amazon's html code
    price = soup2.find(id="priceblock_ourprice").get_text()  #this pulls the price directly from amazon's html code
    converted_price = float(price[1:4])  #this converts the string to a float for the price

    if (converted_price < 600):
        send_mail()
    print(converted_price)
    print(title.strip())

    if (converted_price < 600):  #this sends an email if the price falls below $600
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Ephillips2841@gmail.com', 'bwrpmuprnpwtlwhm')  #this is the email and the app password from google

    subject = 'Price Decrease!'
    body = 'Check the Amazon link https://www.amazon.com/Google-Pixelbook-Chromebook-64GB-Black/dp/B07YMGQYP6/ref' \
           '=sr_1_3?keywords=pixelbook&qid=1579924237&sr=8-3&th=1 '
    msg = f'Subject: {subject}\n\n{body}'  #what the email message will include

    server.sendmail(
        'Ephillips2841@gmail.com',
        'Grinder123089@aol.com',
        msg
    )
    print('Email Sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)  #how often to check the price
