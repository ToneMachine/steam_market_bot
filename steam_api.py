import requests

app_id_inquiry = '232090'
item_name_inquiry = 'Horzine Supply Crate | Series #9'

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

item_hash_name = url_encoder(item_name_inquiry)

market_listing = get_market_listings(app_id_inquiry,item_hash_name)
lowest_price = market_listing.get('lowest_price')

print(lowest_price)