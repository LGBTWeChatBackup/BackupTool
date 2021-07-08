# POWER BY YAOYAO
# 已经对代码信息进行核查，如直接下载建议检查代码信息
# 潦草生成，面向谷歌编程，建议自行优化
# 可能触发微信反爬虫机制
# 文章列表获取方式请参考其他文章
# 建议根据情况修改同目录下"00_1_mainpro.py"中PubVar部分信息
# 仅建议在类Unix（darwin/Linux/FreeBSD/WSL）下使用
# b0.01.20210707-Beta
# pip3 / pip install bs4
# pip3/pip install pdfkit
# NEED wkhtmltopdf TO RUN (GET IT FROM HTTPS://wkhtmltopdf.org)

import pdfkit 
import os
import time
from a001mainpro import PubVar

dirname =  "./"+ PubVar.WXID +"/"
pdfdir = "pdf/"
if not os.path.exists(pdfdir):
    os.makedirs(pdfdir)

options = {
  "enable-local-file-access": None
}


for f in os.listdir(dirname):
    if os.path.isfile(os.path.join(dirname, f)):
        print(f)
        try:
            pdfkit.from_file(os.path.join(dirname, f), os.path.join(pdfdir, f.replace("html","pdf")),options=options) 
        except:
        	pass
