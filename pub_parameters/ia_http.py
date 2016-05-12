#!/usr/bin/env python
#encoding: utf-8

import urllib
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
import json

class py_http():
    
    def __init__(self):
        pass

    def http_read(self,s_url,s_header,s_timeout,s_data):
        if s_data=='':
            req = urllib2.Request(url=s_url,headers=s_header)
        else:
            params = json.dumps(s_data)
            req = urllib2.Request(s_url,params,s_header)
        try:
            response = urllib2.urlopen(req,timeout=s_timeout)
            the_page = response.read()
            return the_page

        except HTTPError,e:
            return e.read()

        except URLError,e:
            return self.Cjson('URLError '+str(e.reason))
        except:
            return self.Cjson('http_read other error or time out')

    def Cjson(self,text):
        b={}
        b['code']='8888'
        b['message']=text
        b['data']='http_read has some error'
        b['request_time']=0.0
        b['response_time']=0.0
        return json.dumps(b)

if __name__ == '__main__':    
    #save_auth(get_token())
    # cc={"code":200,"message":"","data":[{"description":"","last_operate":1444720592,"height":219,"astro":9,"weixin":"","ethnicity":1,"name":"\u7f8e\u4e3d\u7684\u5929\u5c713192","vbadge":0,"ilike":"","city_settled":"1_999_000000","weibo":"","photos_count":7,"ihate":"","blood_type":"A","is_locked":0,"status":"0","lang":"zh-cn","weight":58,"birthday":599241600,"education":"","role":"1","avatar":"http:\/\/77g4l9.com5.z0.glb.qiniucdn.com\/userfiles\/005\/126\/448\/61130!Head.jpg","qq":"","hometown":"1_156_659003","chinese_zodiac":4,"uid":5126448,"last_login":1444720602,"industry":"","hot":71,"age":26,"online_state":1,"note":"","distance":0,"album":[{"pid":34079453,"url":"http:\/\/77g4l9.com5.z0.glb.qiniucdn.com\/userfiles\/005\/126\/448\/13300!Head.jpg"},{"pid":34489603,"url":"http:\/\/77g4l9.com5.z0.glb.qiniucdn.com\/userfiles\/005\/126\/448\/69248!Head.jpg"},{"pid":34492840,"url":"http:\/\/77g4l9.com5.z0.glb.qiniucdn.com\/userfiles\/005\/126\/448\/91620!Head.jpg"}],"relationship":0,"in_blacklist":0,"red_ribbon":0,"red_ribbon_link":"http:\/\/www.blued.cn\/CRR\/","groups_count":3,"followed_count":35,"followers_count":57,"is_access_groups":1,"is_access_follows":1,"friends_count":5,"black_count":1,"black_allowed_count":50,"avatar_pid":26995277,"verify":[{"verified_time":1442913541,"add_time":1441070840,"has_audited":2}]}],"request_id":"3C02060ADAAF1C56B034EF420211DD1F","request_time":1444720602.7161,"response_time":1444720602.8436}
    # aa=py_json()
    # bb=aa.json_dump(c
    pass