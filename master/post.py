#coding=utf-8
import requests
import json, urllib2, httplib
# data = {'platform':'ios','down_url':'www.baidu.com','pwd':123123}
# data = json.dumps({"platform": "ios", "version": '4.8.0', "result":0, 'module':'登录','casename':'执行登录测试,点击事件','time':'321312342.43242','exception':'登录报错','screenshot':['www.baidu.com','www.google.com','www.baidu.com','www.baidu.com']})
# data = json.dumps({"host": "api.blued.com", "interface": '/qatest/autoser', "result":0, 'module':'登录','casename':'执行登录测试,点击事件','time':'321312342.43242','code':10232,'data':'dsadas','message':'123132','request_id':'12312','request_time':'1231243','response_time':'34234234'})
# data = json.dumps({"_": "rH3oQp00CzExMTExMTExMTExMTExMTF+BU7/Xdnl2KzWdWXWSRowSRuL3kfAT4t8JZiTU9NC3eSgrC0wKuki7h4F"})
# data = json.dumps({"page":1,"type":"hot"})
def firpw(url):
    # req = requests.xpost(url,data)
    # req = requests.get(url)
    # requests.post(url,data)
    # requests.post(url,data)
    # requests.post(url,data)
    # a = urllib2.urlopen(url,data).read()
    # json = req.json()
    # req = urllib2.Request(url)
    # print req
    # res_data = urllib2.urlopen(req)
    # res = res_data.read()
    # print res


    conn = httplib.HTTPConnection("106.75.141.41")
    conn.request(method="GET",url=url)
    response = conn.getresponse()
    res= response.read()
    print res
    # print req
    # json = eval(json)
    # json = json.loads(json)
    # print a
    # print type(json)
    # print json

if __name__ == '__main__':
    # url = "http://172.16.20.119:8000/qatest/autocli"
    # url = "http://106.75.141.41/qatest/autocli"
    # url = "http://172.16.20.119:8000/qatest/autoser"
    url = "http://106.75.141.41/ticktocks/users/70?filter=nearby&lot=116.279992&distance=500&size=10&page=1&lat=40.065751&gmt="
    firpw(url)
