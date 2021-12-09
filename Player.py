#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import re

options = webdriver.ChromeOptions()
options.add_argument('disable-gpu')
options.add_argument('headless')
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',chrome_options=options)


pl=[]
players = {}
players['info']=[]


url = 'https://www.premierleague.com/tables'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
targets = soup.select('.team > a')
front_url = 'https://www.premierleague.com'

for j in range(20):
    print(j)
    club_detail_url = re.sub(r'overview', 'squad', front_url + targets[j]['href'])
    driver.get(club_detail_url)
    p2=driver.find_elements_by_xpath('//*[@id="mainContent"]/div[3]/div/ul/li')#선수 숫자 저장
    print(club_detail_url)


    for i in range(1,len(p2)+1):
        he = driver.find_element_by_xpath("//*[@id='mainContent']/div[3]/div/ul/li[{0}]/a[@href]".format(i)) #선수주소 가져오기
        #print(he.get_attribute("href"))#선수주소
    
        response = requests.get(he.get_attribute("href"))
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all(class_='info')

        #print(title[1].text) #포지션
        #print('/'.join(title[3].text.replace(' ','')[1:11].split('/')[::-1]).replace('/','')) #생일
        
        title2 = soup.find_all(class_='playerDetails')
        numname=[x for x in title2[0].text.split('\n') if x] #번호, 이름
        #print(numname[0])#번호
        try:
            numname[0]=int(numname[0])#번호 Null이면  numname[0]에 이름저장
        except:
            numname.append(numname[0])
            numname[0]=None
            #print(numname[1])
        
        for i in range(len(club_detail_url.split('/'))):
            if re.sub(r'[^0-9]','',club_detail_url.split('/')[i]) is not '':
                club_id = int(club_detail_url.split('/')[i])
                break

        for i in range(len(he.get_attribute("href").split('/'))):
            if re.sub(r'[^0-9]','',he.get_attribute("href").split('/')[i]) is not '':
                player_id = int(he.get_attribute("href").split('/')[i])
                break

        #print(club_id)
        #print(player_id)
        infom ={'Player_id': int(player_id),'Club_id':int(club_id),'Player_name':numname[1],'Uniform_num':numname[0],'Date_of_birth':'/'.join(title[3].text.replace(' ','')[1:11].split('/')[::-1]),'position':title[1].text}
        pl.append(infom)


# In[2]:


import json

with open('./sample.json','w',encoding='utf8') as outfile:
    json.dump(pl,outfile,ensure_ascii=False)

