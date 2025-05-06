
# 📉 Amazon Price Tracker

A simple Python-based tool to monitor product prices on Amazon and alert you when prices drop below your desired threshold.

---

## 🗂️ Project Structure

- `price_tracker.py` - Main script that scrapes Amazon product pages and sends notifications.
- `product.json` - Contains product details including name, Amazon URL, and your desired price.

---

## ⚙️ Features

- ✅ Track multiple products
- 🔎 Scrape live prices from Amazon
- 🔔 Get desktop notifications when price drops
- 📝 Easy-to-edit JSON configuration

---

## 🧰 Requirements

Make sure you have Python 3 installed. Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

Dependencies include:

- `requests`
- `beautifulsoup4`
- `lxml`
- `plyer`

---

## 📁 Sample `product.json`

```json
[
    {
        "name": "Iphone 15",
        "url": "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY",
        "desired_price": 30000
    },
    {
        "name": "Samsung Galaxy M35",
        "url": "https://www.amazon.in/Samsung-Thunder-Storage-Corning-Gorilla/dp/B0D7Z8CJP8",
        "desired_price": 15000
    }
]
```

---

## 🚀 How to Use

1. Add your products and target prices to `product.json`.
2. Run the script:

```bash
python price_tracker.py
```

3. If any product price is at or below your desired price, you’ll receive a system notification.

---

## 🧠 Notes

- This tool depends on Amazon’s current webpage structure. If the site layout changes, selectors may need to be updated.
- Use responsibly. Frequent scraping may result in IP bans from Amazon.

---

