from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setting import account
from setting import password
import time
import requests

driver = webdriver.Chrome(service=ChromeService())
url = 'https://store.steampowered.com/login/?steamtv'
tos = True
page = 1
pos = 1

account_name = account
account_password = password

# waits for element to load
def wait_for(element,elem_name,time = 30):
    WebDriverWait(driver,time).until(EC.presence_of_element_located((element,elem_name)))

# gets starting price for item
def get_market_listings(string):

    # Replace each space with %20
    characters_to_replace = ' '
    replacement_char = '%20'

    for char in characters_to_replace:
        string = string.replace(char, replacement_char)

    # Replace each "|" with %C7
    characters_to_replace = '|'
    replacement_char = '%C7'

    for char in characters_to_replace:
        string = string.replace(char, replacement_char)

    # Replace each "&" with %26
    characters_to_replace = '&'
    replacement_char = '%26'

    for char in characters_to_replace:
        string = string.replace(char, replacement_char)
    
    url = f'http://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name={string}'
    response = requests.get(url)
    data = response.json()

    return data.get('lowest_price').strip('$')

# opens webpage
driver.get(url)
driver.maximize_window()

# login
time.sleep(2)
user = driver.find_element(By.CLASS_NAME,'_2eKVn6g5Yysx9JmutQe7WV')
user.send_keys(account_name) # input(user name)

pw = driver.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
pw.send_keys(account_password,Keys.ENTER) # input(password)

# inventory
wait_for(By.XPATH,'//*[@id="global_header"]/div/div[2]/a[3]',180)
driver.find_element(By.XPATH,'//*[@id="global_header"]/div/div[2]/a[3]').click()
driver.find_element(By.XPATH,'//*[@id="friendactivity_right_column"]/div/div[3]/div[7]/a/span').click()
driver.find_element(By.ID,'inventory_link_730').click() # input(which game)
time.sleep(2)

# sells inventory
while True:
    
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,f'#inventory_76561198213304301_730_2 > div:nth-child({page}) > div:nth-child({pos})').click()
    wait_for(By.ID,'iteminfo1_item_tags_content') 
    tags = driver.find_element(By.ID,'iteminfo1_item_tags_content').text.split(',')

    if 'Container' in tags:
        
        # gets price of item
        time.sleep(2)
        case = driver.find_element(By.ID,'iteminfo1_item_name').text
        price = get_market_listings(case)
        wait_for(By.PARTIAL_LINK_TEXT,'Sell')
        driver.find_element(By.PARTIAL_LINK_TEXT,'Sell').click()
        sell = driver.find_element(By.ID,'market_sell_buyercurrency_input')
        time.sleep(2)
        sell.send_keys(price)
        
        # confrims sell
        if tos: # check if tos is clicked    
            driver.find_element(By.ID,'market_sell_dialog_accept_ssa').click()
            tos = False

        driver.find_element(By.ID,'market_sell_dialog_accept').click()
        time.sleep(2)
        driver.find_element(By.PARTIAL_LINK_TEXT,'OK').click()
        time.sleep(3)

    # updates next item
    else:
        pos += 1
        
        # next page
        if pos > 25:
            page += 1
            pos = 1
            driver.find_element(By.ID,'pagebtn_next').click()

time.sleep(30)