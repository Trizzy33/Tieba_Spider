# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import time
from datetime import datetime
#df = pd.read_excel (r'C:\Users\xiaok\Desktop\Book1.xlsx')
"""

c =  ""
for indexs in df.index:
    a = df.loc[indexs].values[0:-1]
    a = np.array2string(a,
                      suppress_small=True)
    a.replace(" ", "")
    c += a
c = c.replace(" ", "")
c = c.replace("[", "")
c = c.replace("]", "")
c = c.split("'")

c = [i for i in c if i]

for i in range(6, 100):
    regu = "scrapy run " + c[i] + " tieba" + str(i) + " -gs -p 1 1"
    print(regu)
    os.system(regu)
    time.sleep(50)
    if i % 10 == 0:
        time.sleep(200)
    os.system("echo executed")

"""
#激战2吧炫舞2吧
f = "galgame吧乱斗西游吧dnf商人吧风雨大姨妈吧csol2吧放开那三国吧dnf元素吧拳皇97吧dnf魔道吧3ds吧战争学院吧轩辕传奇吧皮卡剧吧lovelive国服吧eve吧csgo吧lol英雄联盟代练吧dnf枪神吧班德尔城吧火影ol吧dnf女大枪吧我的世界手机版吧奥比交易吧天天富翁吧音速交易吧机动战士敢达ol吧斗鱼tv吧梅露可物语吧手游先锋吧疾风之刃吧雷瑟守备吧代练吧qq音速吧大话西游2吧战争雷霆吧全民突击吧愤怒的小鸟吧"
l = f.split("吧")
j = 0

for i in l:
    if not i.isnumeric():
        regu = "scrapy run " + i + " " +  "tieba0" + " -gs -p 1 2 -f thread_filter"
        print(regu)
        os.system(regu)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        
        time.sleep(60)

        if j%5 == 0:
            time.sleep(300)
        j = j+1
        os.system("echo executed")
        

#for i in range(1,100):
