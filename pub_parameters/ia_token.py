#!/usr/bin/env python
#encoding: utf-8

import urllib
import urllib2
import sys
import json
import ia_configure
import encryption
import base64
import os
import ia_http
import ia_json
import hashlib

from urllib2 import Request, urlopen, URLError, HTTPError

def get_token(acc,pas):

    pc=encryption.prpcrypt()
    dev_id=pc.get_devid()


    values={'type':'email','identity':acc,'password':pas,'dev_id':dev_id}
    jdata2=pc.jiami_j2j(values)
    req = urllib2.Request(url=ia_configure.url_ym+'/passport/auth',data=jdata2,headers=addHeader(0))

    token=''

    try:
        response = urllib2.urlopen(req)
        the_page = response.read()
        j2=pc.jiemi_j2j(the_page)

        j3=json.loads(j2)


        token=j3['access_token']
        uid=j3['uid']
        if token!='':
            en_text=pc.encrypt(token)
            ak_text=pc.padAK(en_text)
            b2=base64.encodestring(str(uid)+':'+ak_text).replace('\n','')
            save_auth('Basic '+b2)
            return 'Basic '+b2
        else:
            return ''

    except HTTPError,e:
        print 'get token from server error'+e.read()
        print 'get token from locate file'
        return get_auth()
    except URLError,e:
        print e.reason
        print 'get error'
        return get_auth()


def get_token_forzhuce():

    phttp=ia_http.py_http()
    pc=encryption.prpcrypt()
    pjson=ia_json.py_json()

    values={'type':'email','stage':'token'}
    jdata2=pc.jiami_j2j(values)
    page=phttp.http_read(ia_configure.url_ym+ia_configure.zc_identity,addHeader(0),10,jdata2)
    values=pc.jiemi_j2j(page)

    values=pjson.json_load(values)
    a=pjson.json_getvalue(values,'token')
    return a


def addHeader(b_int,acc='',pas=''):
    header={}
    header['Accept-Language']='zh-cn'
    header['User-Agent']='Mozilla/5.0 (iPhone; iOS 9.3.1; Scale/2.00) iOS/084_0.8.4_6311_046 (Asia/Shanghai)'
    header['Content-Type']='application/json'
    header['Connection']='keep-alive'
    header['Accept']='*/*'
    if b_int!=0:
        header['Authorization']=get_token(acc,pas)
    return header


def save_auth(text):
    f=open('auth.txt','w')
    f.write(text)
    f.close()

def get_auth():
    if os.path.exists('auth.txt'):
        f=open('auth.txt','r')
        auth=f.read()
        f.close()
        return auth


if __name__ == '__main__':
    #get_token('ldq001@qq.com',hashlib.sha1('111111').hexdigest())
    print addHeader(1,'ldq135@qq.com',hashlib.sha1('1234').hexdigest())
    #save_auth(get_token())
