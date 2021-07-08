// END PAGE IS endpage，可打开公众平台后台，点击新建图文，添加超链接，输入相应的微信账户之后看一共有多少页
// bizid 可打开任意一篇需要获取的公众号文章，之后打开控制台，输入biz查看
// 复制这个文件的所有内容到公众号后台的开发者控制台，回车
// 如果提示freq control，证明被频率控制，暂时没有解决方案

var endpage = 39;
var bizid = "MzU0MTA3OTU5Ng==";

var urlSearchParams = new URLSearchParams(window.location.search);
var params = Object.fromEntries(urlSearchParams.entries());
var token = params['token'];

const urlpart1 = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin="
const urlpart2 = "&count=5&fakeid="
const urlpart3 = "&type=9&query=&token="
const urlpart4 = "&lang=zh_CN&f=json&ajax=1"



document.body.innerHTML = '';
for (let i = 0; i <= endpage * 5; i=i+5) {
    url = urlpart1 + i.toString() + urlpart2 + bizid + urlpart3 + token + urlpart4;
    console.log(url); 
    // window.open(url);
    var body = document.getElementsByTagName("body");
    var div = document.createElement("div");
    div.innerHTML = '<iframe id="'+ i.toString() + '" name="idFrame" src="'+ url +'" ></iframe>';
    document.body.appendChild(div);
}

