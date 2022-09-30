from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import json
import time

browser=webdriver.Chrome()
url="https://www.amazon.jobs/en-gb/job_categories/software-development"
browser.get(url)



#to save data to json file

with open("flipcart_data.json","w") as f:
    json.dump([],f)

def save_to_json(new_data,file_name="flipcart_data.json"):
    with open(file_name,"r+") as f:
        file_data=json.load(f)
        file_data.append(new_data)
        f.seek(0)
        json.dump(file_data,f,indent=4)

# for pagination 
isBtnDisabled=False
count=0
while not isBtnDisabled:

    # To get data

    div=[elements for elements in WebDriverWait(browser,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'div[class="job"]')))]
    for item in div:
        job_title=item.find_element(By.CSS_SELECTOR,'h3[class="job-title"]').text
        location_id=item.find_element(By.CSS_SELECTOR,'p[class="location-and-id"]').text
        posted_time=item.find_element(By.CSS_SELECTOR,'h2[class="posting-date"]').text
        updated_time=item.find_element(By.CSS_SELECTOR,'p[class="meta time-elapsed"]').text
        save_to_json({
            "job_title":job_title,
            "location_id":location_id,
            "posted-time":posted_time,
            "updated-time":updated_time
        })


    # to find the button
    Button=WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,'//div/button[@class="btn circle right"]')))
    next_class=Button.get_attribute('class')
    if 'circle disabled right' in next_class:
        isBtnDisabled=True
        break
    browser.find_element(By.XPATH,'//div/button[@class="btn circle right"]').click()
    time.sleep(1)

time.sleep(4)
browser.close()
