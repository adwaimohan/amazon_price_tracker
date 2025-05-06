import requests
from bs4 import BeautifulSoup
import lxml
import json
from plyer import notification

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

with open('C:/Users/KIIT0001/Desktop/work/projects/amazon_price_tracker/product.json') as f:

    products = json.load(f)

def check_price(product):
    try:
        url = product['url']
        target = product['desired_price']
        name = product['name']
    except KeyError as e:
        print(f"Missing key {e} in product: {product}")
        return

    response = requests.get(url, headers=HEADERS)
    
    
    soup = BeautifulSoup(response.content, 'lxml')

    title = soup.find('span', id='productTitle').get_text(strip=True)

    
    price_element = soup.find('span', class_='a-price-whole')
    if price_element:
        price = price_element.get_text().replace(',', '')
        try:
            act_price = float(price)
        except ValueError:
            print(f"Failed to convert price for {name}. Price found: {price}")
            return
    else:
        print(f"Price element not found for {name}. Skipping.")
        return

    if act_price <= target:
        message = f"{name}\nCurrent Price: ₹{act_price}"
        print(f"✅ Price drop for {name}! Current price: ₹{act_price}")
        notification.notify(
            title="📢 Amazon Price Drop Alert!",
            message=message,
            timeout=10
        )

for product in products:
    check_price(product)
