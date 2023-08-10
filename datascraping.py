import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.flipkart.com/search?q=noise+earbuds&sid=0pm%2Cfcn%2C821%2Ca7x%2C2si&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=noise+earbuds%7CTrue+Wireless&requestId=3ae55b05-f091-44ad-8a1b-8f6f8b7e5176&p%5B%5D=facets.price_range.from%3D600&p%5B%5D=facets.price_range.to%3D10000'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")  # Using "html.parser" instead of "lxml"

names = soup.find_all("a", class_="s1Q9rs")
prices = soup.find_all("div", class_="_30jeq3")

# Create a CSV file and write the data into it
with open('noiseearbuds_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price'])  # Write header

    for name, price in zip(names, prices):
        name_text = name.text.strip()
        price_text = price.text.strip()

        writer.writerow([name_text, price_text])

print("Data scraped and saved to tablet_data.csv")
