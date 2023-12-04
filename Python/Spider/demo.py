import urllib.request


def main():
    baseurl = "http:movie.douban.com/top250?start=0"
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    #3.保存数据
    # saveData(savepath)

    askURL("http:movie.douban.com/top250?start=0")



#爬取网页
def getData(baseurl):
    datalist = []
    #2.逐一解析数据
    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器
    head = {     #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
    }
    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        elif hasattr(e,"reason"):
            print(e.reason)

        # return html





#保存数据
def saveData(savepath):
    print("save...")

if __name__ == "__main__":#当前程序执行时
    #调用函数
    main()