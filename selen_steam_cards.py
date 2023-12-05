from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# waits for element to load
def wait_for(element,elem_name,time = 30):
    WebDriverWait(driver,time).until(EC.presence_of_element_located((element,elem_name)))

# opens webpage
driver = webdriver.Chrome(service=ChromeService())
url = 'https://store.steampowered.com/login/?steamtv'
driver.get(url)
driver.maximize_window()

# login
time.sleep(2)
user = driver.find_element(By.CLASS_NAME,'newlogindialog_TextInput_2eKVn')
user.send_keys(user) # input(user name)
password = driver.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
password.send_keys(password,Keys.ENTER) # input(password)

# inventory
wait_for(By.XPATH,'//*[@id="global_header"]/div/div[2]/a[3]',180)
driver.find_element(By.XPATH,'//*[@id="global_header"]/div/div[2]/a[3]').click()
driver.find_element(By.XPATH,'//*[@id="friendactivity_right_column"]/div/div[3]/div[7]/a/span').click()
driver.find_element(By.ID,'inventory_link_753').click() # input(which game)
time.sleep(2)

# cycles items
tos = True
css_sel = '#inventory_76561198213304301_753_6 > div:nth-child(1) > div:nth-child(2)'

while True:
    wait_for(By.CSS_SELECTOR,css_sel)
    driver.find_element(By.CSS_SELECTOR,css_sel).click()
    wait_for(By.CLASS_NAME,'item_market_actions') 
    tags = driver.find_element(By.ID,'iteminfo1_item_tags_content').text.split(',')

    # checks tags
    for tag in tags:

            # turning cards into gems is buggy
        # if tag == ' Not Marketable':
    
        #     wait_for(By.ID,'iteminfo0_item_scrap_link')
        #     time.sleep(2)
        #     driver.find_element(By.PARTIAL_LINK_TEXT,'Turn into Gems...').click() # turns items into gems
        #     time.sleep(30)
        #     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[2]/div[1]').click()
        #     time.sleep(3)
        #     driver.find_element(By.CSS_SELECTOR,'body > div.newmodal > div.newmodal_content_border > div > div.newmodal_buttons > div').click()

        if tag == ' Trading Card': # input(what items to sell)

            # gets price of item
            wait_for(By.PARTIAL_LINK_TEXT,'Sell')
            driver.find_element(By.PARTIAL_LINK_TEXT,'Sell').click() # sell button
            time.sleep(2)
            wait_for(By.CSS_SELECTOR,'#pricehistory > div.jqplot-axis.jqplot-yaxis > div:nth-child(2)')
            driver.find_element(By.CLASS_NAME,'zoomopt').click() # clicks on week
            value = driver.find_element(By.CSS_SELECTOR,'#pricehistory > div.jqplot-axis.jqplot-yaxis > div:nth-child(2)').text
            value = value.strip('$')
            buyer = driver.find_element(By.ID,'market_sell_buyercurrency_input')
            time.sleep(2)
            buyer.send_keys(value)
            wait_for(By.ID,'market_sell_dialog_accept')

            # confrims sell
            if tos: # check if tos is clicked    
                driver.find_element(By.ID,'market_sell_dialog_accept_ssa').click()
                tos = False  

            driver.find_element(By.ID,'market_sell_dialog_accept').click()
            time.sleep(2)
            driver.find_element(By.PARTIAL_LINK_TEXT,'OK').click()
            time.sleep(3)

time.sleep(300)
