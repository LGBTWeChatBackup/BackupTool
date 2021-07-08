# POWER BY YAOYAO
# 部分参考GitHub：LeLe86/vWeChatCrawl
# 已经对代码信息进行核查，如直接下载建议检查代码信息
# 潦草生成，面向谷歌编程，建议自行优化
# 可能触发微信反爬虫机制
# 文章列表获取方式请参考其他文章
# 建议根据情况修改PubVar部分信息
# 仅建议在类Unix（darwin/Linux/FreeBSD/WSL）下使用
# b0.01.20210707-Beta
# pip3 / pip install bs4
# 20210707版本未加入CSV功能，下一版本加入。使用CSV，请自行处理好文件格式与编码；CSV方式下未处理Rename.py相关操作，强烈建议非必要不要使用


import os
import requests
from bs4 import BeautifulSoup
from time import sleep

class PubVar:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'http://mp.weixin.qq.com/'
    }
    WXID = "UNDEFINE"  #更改为微信号
    SleepTime = 3 # 中间间隔时间，最低应设置为3s，图片较多的情况10s可能也会被限制，可以使用代理（下一版本添加功能）
    ListType = 1 # 1: 为从该文件中URLList读取，新Html文件名为数字结构; 2: 为从以下CSVFile中读取，请注意文件编码，建议UTF-8并Excel编辑
    URLList = [
        "https://mp.weixin.qq.com/s?src=11&timestamp=1625673601&ver=3176&signature=9ZU*LrxWeulvoAjy7Ctvf*5xcZr8sI7JO902GI6wKelbUgpSjyEuw*Ff7DBHpR*NUkdIwofzdlijMWxLT1zctE8zGPmBY71C7JJobZexkUfjPvvT6njwdZBOC9v-OXHD&new=1",
        "https://mp.weixin.qq.com/s?src=11&timestamp=1625673601&ver=3176&signature=KMPWy9Gh35tmBI5dY0F9tvt4mkRl9r-fBWGKIlBvg06bztb*UCrRfyL*S*U8sGKmW8qzNbZ31xKee5a1ilryCN*4wiT14ucZHfCIUeOr96yMppngaP1roeTuFkfpuxXn&new=1",
        "https://mp.weixin.qq.com/s?src=11&timestamp=1625673601&ver=3176&signature=qMZdzrbey7hFXJ0q-3jbZmT1yCFuRf702lc-CCba-EX2c4N800joEp*m6v6q4aPzwpXkiO5imlRSpjVjhpK4rQ-tJhfrM9LU0DmpLKSv3IUgq5VjHSHdwrjtOyeZine2&new=1",
        "https://mp.weixin.qq.com/s?src=11&timestamp=1625673601&ver=3176&signature=PA-dJqdhMs6iP2EowGRY4lEkfpuhSk4FsULkywK5z8-HjBlKQHGkH*InQDpqWb9cqGehQz6xRQ9edjV3IzF9htkyxo-WwxRJUaGEJBpWy10*udnmpy354-KFqqX9hFBH&new=1"
    
    ]
    
    # 未完成部分
    CSVFile = "./CSVTable1.csv" #FileNumber仅供参考 URL为微信文章URL Name为文章名称
    # CSVFile = "./CSVTable2.csv" #FileNumber仅供参考 URL为微信文章URL Name为文章名称，不填写，自动数字命名


def SaveFile(fpath, fileContent):
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(fileContent)


def ReadFile(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        all_the_text = f.read()
    return all_the_text

def Downloader(URLList, HtmlDir):
    idx = 0
    for url in URLList:
        idx += 1
        HtmlName = idx
        HtmlFileName = str(HtmlName) + ".html"
        HtmlFilePath = HtmlDir+"/"+HtmlFileName
        print(idx, HtmlFileName, url)
        if os.path.exists(HtmlFilePath):
            print("exists", HtmlFilePath)
            continue
        headers = PubVar.headers
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url, headers=headers, proxies=None, verify=False)
        if response.status_code == 200:
            HtmlData = response.text 
        else:
            print("ERROR")
        HtmlDataBS4ED = BeautifulSoup(HtmlData, "lxml") 
        imgList = HtmlDataBS4ED.findAll("img")
        imgindex = 0
        for img in imgList:
            imgindex += 1
            originalURL = ""
            if "data-src" in img.attrs: 
                originalURL = img.attrs['data-src']
            elif "src" in img.attrs: 
                originalURL = img.attrs['src']
            else:
                originalURL = ""
            if originalURL.startswith("//"): 
                originalURL = "http:" + originalURL
            if len(originalURL) > 0:
                print("\r down imgs " + "▇" * imgindex +
                    " " + str(imgindex), end="")
                if "data-type" in img.attrs:
                    imgtype = img.attrs["data-type"]
                else:
                    imgtype = "png"
                ImgName = str(HtmlName) + "_"+str(imgindex)+"."+imgtype 
                imgsavepath = os.path.join(HtmlDir, ImgDir, ImgName) 
                headers = PubVar.headers
                requests.packages.urllib3.disable_warnings()
                r = requests.get(originalURL, headers=headers, proxies=None, verify=False)
                with open(imgsavepath, 'wb') as f:
                    f.write(r.content)
                img.attrs["src"] = os.path.join(ImgDir , ImgName )
            else:
                img.attrs["src"] = ""
        
        linkList = HtmlDataBS4ED.findAll("link")
        for link in linkList:
            if link.attrs["href"].startswith("//"):
                link.attrs["href"] = "https:" + link.attrs["href"]
        jscontent = HtmlDataBS4ED.find(id="js_content")
        jscontent.attrs["style"]=""
        print("\r", end="")
        SaveFile(HtmlFilePath, str(HtmlDataBS4ED))
        sleep(PubVar.SleepTime)


if __name__ == "__main__":
    HtmlDir =  "./"+ PubVar.WXID +"/"
    if not os.path.exists(HtmlDir):
        os.makedirs(HtmlDir)
    ImgDir =  "./images"
    if not os.path.exists(os.path.join(HtmlDir ,ImgDir)):
        os.makedirs(os.path.join(HtmlDir ,ImgDir))


    if PubVar.ListType == 1:
        URLList = PubVar.URLList
    elif PubVar.ListType == 2:
        print("Sorry,PLEASE WAITING FOR NEXT Ver.")
    else:
        print("ERROR")

    Downloader(URLList, HtmlDir)
