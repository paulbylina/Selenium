from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import random
import openpyxl

def get_random_int_dec(integer):
    random_delay = integer + random.random()
    return random_delay

# START DRIVER
driver = webdriver.Chrome()
driver.maximize_window()

# wiki URL
wiki_url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_Europe_by_revenue"

# LOAD PAGE
driver.get(wiki_url)
sleep(get_random_int_dec(2))

elem = driver.find_element(By.TAG_NAME,'table')
head = elem.find_element(By.TAG_NAME,'thead')
body = elem.find_element(By.TAG_NAME,'tbody')

list_headers = []
list_rows = []

# GET HEADERS
for HEADER in head.find_elements(By.TAG_NAME,'tr'):  # Rows
    column_items = []
    for item in HEADER.find_elements(By.TAG_NAME,'th'):  # Column 1 Rank
        list_headers.append(item.text)


# GET COLUMNS
for ROW in body.find_elements(By.TAG_NAME,'tr'):  # Rows
    list_items = []
    for item in ROW.find_elements(By.TAG_NAME,'th'):  # Column 1 Rank
        list_items.append(item.text)
        for item in ROW.find_elements(By.TAG_NAME,'td'):  # Other columns
            removed_white_space = item.text.strip()
            list_items.append(removed_white_space)
    list_rows.append(list_items)

# print(list_headers)
# for row in list_rows:
#     print(row)


breakdown_by_country_DF = pd.DataFrame(columns=list_headers, data=list_rows)
print(breakdown_by_country_DF)
# SAVE DF
breakdown_by_country_DF.to_excel(r'Breakdown_By_Country.xlsx')

# 100 LARGEST EU COMPANIES
# FIND MAIN ELEMENTS
# region_list_element = driver.find_element(By.CSS_SELECTOR, '#mw-content-text > div.mw-content-ltr.mw-parser-output > table:nth-child(10)')  # class=
sleep(get_random_int_dec(2))
elem = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]')
head = elem.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]/thead')
body = elem.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]/tbody')

list_headers = []
list_rows = []

# GET HEADERS
for HEADER in head.find_elements(By.TAG_NAME,'tr'):  # Rows
    column_items = []
    for item in HEADER.find_elements(By.TAG_NAME,'th'):  # Column 1 Rank
        list_headers.append(item.text)
# print(list_headers)

# GET COLUMNS
for ROW in body.find_elements(By.TAG_NAME,'tr'):  # Rows
    list_items = []
    for item in ROW.find_elements(By.TAG_NAME,'td'):  # Other columns
        removed_white_space = item.text.strip()
        list_items.append(removed_white_space)
    list_rows.append(list_items)

# print(list_headers)
# for row in list_rows:
#     print(row)


top_100_companies_DF = pd.DataFrame(columns=list_headers, data=list_rows)
print(top_100_companies_DF)
# SAVE DF
top_100_companies_DF.to_excel(r'Top_100_EU_Companies_By_Revenue.xlsx')

driver.close()

