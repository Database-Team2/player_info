#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql


# In[78]:


conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="0825",
        database="mydb",
        charset="utf8"
    )


# In[83]:


#경기장 업데이트

orig_name = input('경기장 업데이트할 대상 경기장의 클럽 이름:')
new_name=input('업데이트할 새로운 이름 입력:')
new_capacity=input('업데이트할 새로운 capacity 입력:')

curs = conn.cursor()

#expcet => 중복된 경기장 존재 x

        
sql="update stadium set Stadium_name='{0}',Capacity={1} where Stadium_name = '{2}'".format(new_name,new_capacity,orig_name)
curs.execute(sql)
                
conn.commit()


# In[58]:


# 클럽결과

curs = conn.cursor()

club1=input('업데이트할 클럽의 이름 입력:')
club2=input()


#스타디움 id 찾기
sql="select stadium_id from stadium where stadium_name = '{0}'".format(club1)
curs.execute(sql)
row=curs.fetchone()
club1_st_id = row[0]

sql="select stadium_id from stadium where stadium_name = '{0}'".format(club2)
curs.execute(sql)
row=curs.fetchone()
club2_st_id = row[0]

print('stadium id done')

#Club id 찾기
sql="select Club_id from club_info where Stadium = {0}".format(club1_st_id)
curs.execute(sql)
row=curs.fetchone()
club1_id = row[0]

sql="select Club_id from club_info where Stadium = {0}".format(club2_st_id)
curs.execute(sql)
row=curs.fetchone()
club2_id = row[0]

print('club id done')

points1,points2=input('points 순서대로입력:').split()
lost1,lost2=input('lost 순서대로입력:').split()
ga1,ga2=input('ga 순서대로입력:').split()
gf1,gf2=input('gf 순서대로입력:').split()

#업데이트 
sql="update club_result set points={0},lost={1},ga={2},gf={3} where Club_id = {4}".format(points1,lost1,ga1,gf1,club1_id)
curs.execute(sql)


sql="update club_result set points={0},lost={1},ga={2},gf={3} where Club_id = {4}".format(points2,lost2,ga2,gf2,club2_id)
curs.execute(sql)



conn.commit()


# In[63]:


#등번호 수정
curs = conn.cursor()

name=input('player 이름입력:')
num=input('수정할 번호 입력:')

sql="update player set Uniform_num={0} where Player_name = '{1}'".format(num,name)
curs.execute(sql)
conn.commit()


# In[73]:


conn.close()

