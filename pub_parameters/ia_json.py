#!/usr/bin/env python
#encoding: utf-8

import json
import types
class py_json():
    
    def __init__(self):
        self.code=''
        self.message=''
        self.data=''
        self.request_time=0.0
        self.response_time=0.0
        self.speed=0.0
        self.mapvalue={}
    def json_dump(self,maptext):
        return json.dumps(maptext)

    def json_dumpadd(self,key,value):
        self.mapvalue[key]=value
        return self.mapvalue


    def json_load(self,jsontext):
        maptext=json.loads(jsontext)
        self.code=str(maptext.get('code',''))
        self.message=maptext.get('message','')
        self.data=maptext.get('data','')
        self.request_time=maptext.get('request_time',0.0)
        self.response_time=maptext.get('response_time',0.0)
        # self.speed=str(round(self.response_time-self.request_time,4))

        return maptext


    def json_getvalue(self,maptext,key):
        try:
            if type(maptext[key])==types.ListType:
                return maptext[key][0]
            else:
                return maptext[key]
        except Exception,e:
            return 'nokey'
    

# if __name__ == '__main__':    
#     cc={"code":404,"message":"\u672a\u627e\u5230","data":[],"request_id":"BF0C0D0A8BA75656DC22A377027A7B03","request_time":1448519563.8084,"response_time":1448519563.8092}
#     cc=json.dumps(cc)
#     aa=py_json()
#     aa.json_load(cc)
#     print aa.request_time
#     print type(aa.request_time)
#     print type(aa.code)
#     print aa.speed
#     