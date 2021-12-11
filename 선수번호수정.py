#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pymysql

conn = pymysql.connect(
        host="",
        port=,
        user="",
        password="",
        database="",
        charset="utf8"
    )



#등번호 수정
curs = conn.cursor()

name=input('player 이름입력:')
num=input('수정할 번호 입력:')

sql="update player set Uniform_num={0} where Player_name = '{1}'".format(num,name)
curs.execute(sql)
conn.commit()

conn.close()

