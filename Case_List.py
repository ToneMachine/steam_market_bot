import requests
import time

case_list = "Revolution Case,Recoil Case,Dreams & Nightmares Case,Operation Riptide Case,Snakebite Case,Operation Broken Fang Case,Fracture Case,Prisma 2 Case,Shattered Web Case,CS20 Case,Prisma Case,Danger Zone Case,Horizon Case,Clutch Case,Spectrum 2 Case,Operation Hydra Case,Spectrum Case,Glove Case,Gamma 2 Case,Gamma Case,Chroma 3 Case,Operation Wildfire Case,Revolver Case,Shadow Case,Falchion Case,Chroma 2 Case,Chroma Case,Operation Vanguard Weapon Case,Operation Breakout Weapon Case,Huntsman Weapon Case,Operation Phoenix Weapon Case,Winter Offensive Weapon Case"
case_list = case_list.split(',')

app_id_inquiry = '730'

# encodes the url
def url_encoder(original_string):

    # Replace each space with %20
    characters_to_replace = ' '
    replacement_char = '%20'

    for char in characters_to_replace:
        original_string = original_string.replace(char, replacement_char)

    # Replace each "|" with %C7
    characters_to_replace = '|'
    replacement_char = '%C7'

    for char in characters_to_replace:
        original_string = original_string.replace(char, replacement_char)

    # Replace each "&" with %26
    characters_to_replace = '&'
    replacement_char = '%26'

    for char in characters_to_replace:
        original_string = original_string.replace(char, replacement_char)

    return original_string

def get_market_listings(app_id,market_hash_name):
    
    url = f'http://steamcommunity.com/market/priceoverview/?currency=1&appid={app_id}&market_hash_name={market_hash_name}'
    response = requests.get(url)
    data = response.json()

    return data

for item_name in case_list:

    try:
    
        item_hash_name = url_encoder(item_name)
        market_listing = get_market_listings(app_id_inquiry,item_hash_name)

        lowest_price = market_listing.get('lowest_price')

        print(item_name,lowest_price)

    except:

        item_hash_name = url_encoder(item_name)
        time.sleep(5)
        market_listing = get_market_listings(app_id_inquiry,item_hash_name)

        lowest_price = market_listing.get('lowest_price')

        print(item_name,lowest_price)        