# use python 3.10
from bs4 import BeautifulSoup
import requests

url = "https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730"

result = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(result.text, 'html.parser')

# Find all the items
items = soup.find_all('div', class_="market_listing_row market_recent_listing_row market_listing_searchresult")

# Print item name and price on the same line
for item in items:
    item_name = item.find('span', class_="market_listing_item_name").text
    item_price = item.find('span', class_="normal_price").text
    strip_item_price = item_price.strip()
    print(f"{item_name}:\n{strip_item_price}")