#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import re

Stadium = {}
Stadium['Stadium_info'] = []
st=[]


options = webdriver.ChromeOptions()
options.add_argument('disable-gpu')
#options.add_argument('headless')
url = 'https://www.premierleague.com/clubs'
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',chrome_options=options)
driver.get(url)
#클럽창 열기
id=1

driver.implicitly_wait(30)
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[5]/button[1]')))
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/button[1]').click()
driver.implicitly_wait(15)
#쿠키 수집창 제거


#테이블에서 받아야하는 row 길이를 받아옴

for i in range(1,21):
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/div[1]/div/ul/li[{0}]/a'.format(i)).send_keys(Keys.CONTROL+'\n')
    driver.implicitly_wait(15)
    driver.switch_to_window(driver.window_handles[1])
    driver.implicitly_wait(15)
    driver.find_element_by_xpath('//*[@id="mainContent"]/nav/ul/li[7]/a').send_keys(Keys.ENTER)
    driver.implicitly_wait(15)
    
    name = driver.find_element_by_xpath('//*[@id="mainContent"]/header/div[2]/div/div/div[2]/h1')
    print(name.text)
    name = name.text
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[2]/div/ul/li[2]').send_keys(Keys.ENTER)
    #새로운 탭을 띄워서 스타디움 capacity가 있는 위치로 이동
    time.sleep(1)
    #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div[3]/div[3]/div[2]/p[1]')))
    capacity = driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[3]/div[2]/p[1]')
    cap = int(re.sub(r'[^0-9]','',capacity.text.replace(' ','').split(':')[1]))
    #cap=int(capacity.text.replace(' ','').replace(',','').split(':')[1])
    print(cap)
    #capacity 추출
    
    driver.close()
    driver.implicitly_wait(15)
    driver.switch_to_window(driver.window_handles[0])
    driver.implicitly_wait(15)
    #탭을 닫은후 처음창으로 이동시킴
    doc ={'Stadium_id':id, 'Stadium_name': name,'Capacity':cap}
    Stadium['Stadium_info'].append(doc)
    id+=1
driver.close()

'''
sibal = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/div[3]/div/table/tbody/tr[1]/td[2]')
ssibal = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/div[3]/div/table/tbody')
ssibal2 = driver.find_elements_by_tag_name('tr')
print(ssibal2)
'''


#soup = BeautifulSoup(driver.page_source, 'lxml')



#title = soup.select_one('#mainContent > div.clubIndex > div > div > div:nth-child(3) > div > table > tbody > tr:nth-child(3)')
#a = title
#print(a)


# In[14]:


import json

with open('./Stadium.json','w',encoding='utf8') as outfile:
    json.dump(Stadium,outfile,ensure_ascii=False)

