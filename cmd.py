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
#激战2吧炫舞2吧galgame吧乱斗西游吧
f = "dnf商人吧风雨大姨妈吧csol2吧放开那三国吧dnf元素吧拳皇97吧dnf魔道吧3ds吧战争学院吧轩辕传奇吧皮卡剧吧lovelive国服吧eve吧csgo吧lol英雄联盟代练吧dnf枪神吧班德尔城吧火影ol吧dnf女大枪吧我的世界手机版吧奥比交易吧天天富翁吧音速交易吧机动战士敢达ol吧斗鱼tv吧梅露可物语吧手游先锋吧疾风之刃吧雷瑟守备吧代练吧qq音速吧大话西游2吧战争雷霆吧全民突击吧愤怒的小鸟吧"
f = "爵士舞吧法布雷加斯吧湖北绿茵吧南昌八一衡源吧莱科宁吧雷阿伦吧山西中宇吧洛杉矶快船吧丁宁吧米兰吧郭跃吧贵州人和吧英超吧维斯布鲁克吧山东金斯顿吧青岛双星吧范佩西吧王皓吧中国足球吧朗多吧成都谢菲联吧马里加吧卡特吧荷兰足球吧卡西利亚斯吧巴特尔吧动画培训吧舒马赫吧不来梅吧霍华德吧莎拉波娃吧库里吧格里芬吧上海东亚吧拉姆吧杰拉德吧悠悠球吧墨尔本曳步舞吧托马斯穆勒吧亨利吧拉丁舞吧沙尔克04吧法国队吧广东宏远吧冥想吧吉喆吧鬼步吧陕西宝荣吧户外吧巴黎圣日尔曼吧凯里欧文吧日本足球吧江苏南钢吧诺维茨基吧舍甫琴科吧皮克吧哈维吧卡配罗吧穆雷吧德国足球吧纽卡斯尔吧勒布朗·詹姆斯吧马布里吧公牛吧鲁尼吧掘金吧伊瓜因吧阿隆索吧皮尔洛吧重庆足球吧篮球孙悦吧皮耶罗吧伊涅斯塔吧希洪竞技吧kimi吧广州富力吧罗本吧利物浦队吧施魏因斯泰格吧邓肯吧"
l = f.split("吧")
j = 0

for i in l:
    if not i.isnumeric():
        regu = "scrapy run " + i + " " +  "tieba1" + " -gs -p 1 1 -f thread_filter"
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
