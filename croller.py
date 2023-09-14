from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

option = Options()
option.add_argument('--headless')
option.add_argument('--window-size=1890,1030')
service = Service()
chromedriver_version = "114.0.5735.16"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager(version=chromedriver_version).install()), options=option)

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://ogqmarket.naver.com/artworks/sticker?categoryId=all")

before_h = browser.execute_script("return window.scrollY")

while True:
    # 맨 아래로 스크롤
    browser.find_element(By.CSS_SELECTOR, value="body").send_keys(Keys.END)
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    # 더 스크롤이 생성되지 않는다면, 멈추기
    if after_h == before_h: break

    before_h = after_h
    
import os

links_hb = []
tags = browser.find_elements(By.CLASS_NAME, 'card_wrap')
for i in tags:
    try:
        links = i.find_element(By.CSS_SELECTOR, 'div > div.box > a').get_attribute('href')
        print(links)
        if links == None:
            pass
        else:
            links_hb.append(links)
    except:
        pass
    
for j in links_hb:
    try:
        browser.get(j)
        base = browser.find_element(By.CSS_SELECTOR, '#__layout > div > div.modal-detail-mask > section > div > div > div.artwork-detail-content > div.artwork-detail-content-body-outer > div.artwork-detail-content-body > div.sticker-sub-images-container')
        ac = base.find_elements(By.CLASS_NAME, 'image-container')
        os.chdir('C:\\Users\\user\\Documents\\GGNIMC\\croll')
        import uuid
        uuids = uuid.uuid4()
        os.mkdir(str(uuids))
        os.chdir(f'C:\\Users\\user\\Documents\\GGNIMC\\croll\\{uuids}')
        for k in ac:
            url = k.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
            import wget
            wget.download(url)
    except:
        pass
            
        
        
    
    
    
        
    
    