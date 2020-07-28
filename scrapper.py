import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.instant-gaming.com/es/2060-comprar-key-steam-dark-souls-3-deluxe-edition/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.75"}

def check_price():
    # This is the website 
    page = requests.get(URL, headers=headers)

    soup1= BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
    # Title of product
    title = soup2.find('h1').get_text()
    title = title.strip()
    
    # Price to float
    price = soup2.find("div", class_="price").get_text()
    price = price.strip()
    converted_price = float(price[:-1])

    # Check if it's lower than what I want
    desired_price = 12
    if converted_price < desired_price:
        send_mail(desired_price, title) 

def send_mail(price, title):
    
    # Establishing connection with gmail server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    
    # Encrypt connection
    server.starttls()
    server.ehlo()
    
    # Login with the custom password
    server.login("xilacai1@gmail.com", "xidxkzaobqvboxms")
    
    # The mail
    subject = "Price fell down from " + str(price) + "€! " + title
    body = "Check the amazon link: " + URL
    
    msg = f'Subject: {subject}\n\n{body}'
    
    # Sending the mail
    server.sendmail(
        "xilacai1@gmail.com",
        "xilacai1@gmail.com",
        msg.encode('utf-8')
    )
    print("HEY EMAIL HAS BEEN SENT!")
    
    # Closing connection to server
    server.quit()

while True:
    check_price()
    time.sleep(86400)