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
#地下城与勇士吧lol吧剑网3吧dota2吧天涯明月刀ol吧魔兽世界吧穿越火线吧英雄联盟吧梦幻西游吧太极熊猫吧战舰少女吧炉石传说吧fifaonline3吧剑灵
f = "qq飞车吧qq炫舞吧炫舞账号交易吧300英雄吧天天酷跑吧逆战吧minecraft吧codol吧坦克世界吧nba2kol吧崩坏学园2吧刀塔传奇吧反恐精英ol吧dota2国服交易吧问道吧ps4吧天谕吧暗黑3吧仙剑奇侠传吧艾欧尼亚吧三国杀吧天龙网游吧黑色玫瑰吧单机游戏吧倩女ol吧双梦镇吧舰队collection吧dota吧dnf剑魂吧魔兽玩家吧dnf红眼吧枪神纪吧奇迹暖暖吧神武逍遥外传吧风暴英雄吧暖暖环游世界吧唯满侠吧lol半价吧网络游戏吧梦幻西游手游吧dota2国服饰品交易吧竞技游戏吧冒险岛吧psv吧英魂之刃吧梦三国吧龙之谷吧boombeach吧奥比岛吧自由之战吧部落战争吧艾尔之光吧qq三国吧全民枪战吧天下3吧steam吧九阴吧炫舞吧洛奇英雄传吧比尔吉沃特吧dnf阿修罗吧御龙在天吧祖安吧少年三国志吧ff14吧斗战神吧全民飞机大战吧csgo饰品交易吧跑跑卡丁车吧德玛西亚吧炫舞时代吧上古卷轴吧minecraftpe吧街头篮球吧风中奇缘吧口袋妖怪吧仙剑6吧赛尔号吧乾坤一掷吧terraria吧诺克萨斯吧小花仙吧魔灵召唤吧dnf鬼泣吧激战2吧炫舞2吧galgame吧乱斗西游吧dnf商人吧风雨大姨妈吧csol2吧放开那三国吧dnf元素吧拳皇97吧dnf魔道吧3ds吧战争学院吧轩辕传奇吧皮卡剧吧lovelive国服吧eve吧csgo吧lol英雄联盟代练吧"
l = f.split("吧")
j = 0

for i in l:
    if not i.isnumeric():
        regu = "scrapy run " + i + " " +  "tieba" + str(j) + " -s -p 1 -f thread_filter"
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
