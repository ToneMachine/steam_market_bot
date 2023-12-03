from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

#opens webpage
driver = webdriver.Chrome(service=ChromeService())
url = 'https://store.steampowered.com/login/?steamtv'
driver.get(url)
driver.maximize_window()

# login
time.sleep(2)
user = driver.find_element(By.CLASS_NAME,"newlogindialog_TextInput_2eKVn")
user.send_keys("#user")
password = driver.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
password.send_keys("#password",Keys.ENTER)
time.sleep(30)

# inventory
driver.find_element(By.XPATH,'//*[@id="global_header"]/div/div[2]/a[3]').click()
driver.find_element(By.XPATH,'//*[@id="friendactivity_right_column"]/div/div[3]/div[7]/a/span').click()

# inventory sort
driver.find_element(By.ID,"inventory_link_730").click()
# driver.find_element(By.ID,"filter_tag_show").click()
# time.sleep(2)
#driver.find_element(By.NAME,'tag_filter_730_2_Type_CSGO_Type_WeaponCase').click()

# inventory
pages = driver.find_element(By.ID,"pagecontrol_max").text
pages = int(pages)

time.sleep(2)

items = driver.find_element(By.XPATH,'//*[@id="inventory_link_730"]/span[3]').text
items = items.strip('()')
items = int(items)
print(items)

for num in range (0,26):
    case_name = driver.find_element(By.CLASS_NAME,"hover_item_name").text
    price = driver.find_element(By.ID,'iteminfo0_market_content').text
    
    page = 1
    num += 1
    css_sel = f'#inventory_76561198213304301_730_2 > div:nth-child({page}) > div:nth-child({num})'

    if num % 25 != 0:
        driver.find_element(By.CSS_SELECTOR,css_sel).click()
        # print(css_sel,"\n")

        # print(case_name)
        # print(price,"\n")

    else:
        num += 1
        driver.find_element(By.CSS_SELECTOR,css_sel).click()
        print(css_sel,"first")
        css_sel = f'#inventory_76561198213304301_730_2 > div:nth-child({page +1}) > div:nth-child({num -25})'    
        driver.find_element(By.ID,'pagebtn_next').click()
        print(css_sel,"second")
        time.sleep(3)

    print(css_sel)
    

time.sleep(300)
