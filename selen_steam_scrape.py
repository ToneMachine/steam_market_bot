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
user.send_keys("brickjohson")
password = driver.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
password.send_keys("Honda93Lube!",Keys.ENTER)
time.sleep(30)

# inventory
driver.find_element(By.XPATH,'//*[@id="global_header"]/div/div[2]/a[3]').click()
driver.find_element(By.XPATH,'//*[@id="friendactivity_right_column"]/div/div[3]/div[7]/a/span').click()

# inventory sort
driver.find_element(By.ID,"inventory_link_730").click()
driver.find_element(By.ID,"filter_tag_show").click()
time.sleep(2)
driver.find_element(By.NAME,'tag_filter_730_2_Type_CSGO_Type_WeaponCase').click()

# inventory
pages = driver.find_element(By.ID,"pagecontrol_max").text
pages = int(pages)

driver.find_element(By.ID,"730_2_34495355779").click()
case_name = driver.find_element(By.ID,"iteminfo1_item_name").text


print(case_name)


time.sleep(300)