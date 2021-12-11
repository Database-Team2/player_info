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

# 클럽결과

curs = conn.cursor()

club1=input('업데이트할 클럽의 이름 입력:')
club2=input()
points1,points2=input('points 순서대로입력:').split()
lost1,lost2=input('lost 순서대로입력:').split()
ga1,ga2=input('ga 순서대로입력:').split()
gf1,gf2=input('gf 순서대로입력:').split()


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

#업데이트 
sql="update club_result set points={0},lost={1},ga={2},gf={3} where Club_id = {4}".format(points1,lost1,ga1,gf1,club1_id)
curs.execute(sql)


sql="update club_result set points={0},lost={1},ga={2},gf={3} where Club_id = {4}".format(points2,lost2,ga2,gf2,club2_id)
curs.execute(sql)

print('update done')

conn.commit()
conn.close()

