# WeChat Backup Tool

## 制作前提

20210706公众号集体炸号事件

## 使用方法

1. 需要通过各种方式获取文章URL（链接）列表，详细方法建议网上搜索。
   1. 推荐方式1 微信公众号的素材管理，获取公众号文章
   2. 推荐方式2 抓包
   3. 推荐方式3 搜狗微信搜索
2. 打开`a001mainpro.py` 根据情况修改`PubVar` 部分信息
3. 将第一步取得的URL填写在`PubVar.URLList`，需要按照List语法填写
4. Python3 环境下直接在目录下运行`a001mainpro.py` 
5. 如果被访问控制，可通过切换IP方式（proxy等）进行处理后再次运行。运行时会自动检查是否已经保存，如已经保存则自动跳过
6. 打开`a002rename.py` 会自动根据公众号文章名称修改文件名
7. 打开`a003htmltopdf.py`会自动根据HTML文件转换为PDF文件

## 注意事项

- 部分参考GitHub：LeLe86/vWeChatCrawl

- 潦草生成，面向谷歌编程，建议自行优化

- 可能触发微信反爬虫机制

- 文章列表获取方式请参考其他文章

- 仅建议在类Unix（darwin/Linux/FreeBSD/WSL）下使用
- 文件自带URL为搜狗微信推荐前4篇

## 依赖

- Python3
- bs4 `pip3 / pip install bs4`
- pdfkit `pip3 / pip install pdfkit`
- wkhtmltopdf https://wkhtmltopdf.org

## TODOS

1. 文件读取URL
2. CSV读取URL
3. 自动化获取文章列表
4. 错误后自动恢复运行
5. 等等


