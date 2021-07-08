# POWER BY YAOYAO
# 已经对代码信息进行核查，如直接下载建议检查代码信息
# 潦草生成，面向谷歌编程，建议自行优化
# 可能触发微信反爬虫机制
# 文章列表获取方式请参考其他文章
# 建议根据情况修改同目录下"00_1_mainpro.py"中PubVar部分信息
# 仅建议在类Unix（darwin/Linux/FreeBSD/WSL）下使用
# b0.01.20210707-Beta
# pip3 / pip install bs4

import datetime
import bs4
import re
import os
import zipfile
import time
from a001mainpro import PubVar

dirname =  "./"+ PubVar.WXID +"/"

# Backup
f = zipfile.ZipFile('archive.zip','w',zipfile.ZIP_DEFLATED)

for dirpath, dirnames, filenames in os.walk(dirname):
    for filename in filenames:
        f.write(os.path.join(dirpath,filename))

print("BACKUP TO ARCHIVE.ZIP, NEXT STEP MAY DESTROY FILES IN THIS PATH")
time.sleep(10)
f.close()

num_files = len([f for f in os.listdir(dirname)if os.path.isfile(os.path.join(dirname, f))])

x = range(1,num_files+1)

for n in x:
    try:
        all_the_text = ''
        with open(dirname+str(n)+'.html', 'r', encoding='utf-8') as f:
            all_the_text = f.read()
        bs = bs4.BeautifulSoup(all_the_text,"lxml")
        oldfilename = str(n)+".html"
        print(n)
        ts = re.findall(r'\bvar\s+t=\"[0-9]+\",n=\"[0-9]+', all_the_text)[0][-10:]
        print(ts)
        date = datetime.datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d')
        print(date)
        title = bs.find_all(id = "js_panel_like_title")[0].text.strip()
        filename = str(n) + ' | ' + date + ' | ' + title + ".html"
        print(oldfilename, filename)
        os.rename(dirname+oldfilename, dirname+filename.replace('/', '_'))
    except:
        print(str(n)+".html", str(n)+".html")
        os.rename(dirname+oldfilename, dirname+filename.replace('/', '_'))
        
