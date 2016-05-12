# coding:utf-8
"""
处理接口请求
"""
import ia_configure
import ia_http
import ia_json
import time
import requests
import json
import ia_token
import urllib2, urllib,httplib
from urllib2 import Request, urlopen, URLError, HTTPError
interface_url = ia_configure.interface_dir
host = ia_configure.url_ym
auth = ia_token.addHeader(1,ia_configure.account_live[0],ia_configure.account_live[1])
phttp=ia_http.py_http()
pjson = ia_json.py_json()
def ergodic(value1, value2):
    for list in value1:
        for (k,v) in list.items():
            if k == 'interface':
                tt_interface = v
            elif k == 'model':
                tt_model = v
            elif k == 'case':
                tt_case = v
        print ia_configure.url_ym+tt_interface, auth
        page=phttp.http_read(ia_configure.url_ym+tt_interface,auth,10,value2)
        message=pjson.json_getvalue(pjson.json_load(page),'message')
        # print message
        timestamp = time.time()
        return page, tt_interface, tt_model, tt_case, timestamp

def send_result(parm1, parm2, parm3, parm4, parm5, parm6, parm7, parm8, parm9, parm10, parm11):
    result = {'host':host,'interface':parm1,'result':parm2,'module':parm3,'casename':parm4,'time':parm5,'code':parm6,'data':parm7,'message':parm8,'request_id':parm9,'request_time':parm10,'response_time':parm11}
    up_data = json.dumps(result)
    requests.post(interface_url,up_data)

def run_get(val, s_data):
    for list in val:
        for (k,v) in list.items():
            if k == 'interface':
                tt_interface = v
            elif k == 'model':
                tt_model = v
            elif k == 'case':
                tt_case = v
        page=phttp.http_read(ia_configure.url_ym+tt_interface,auth,10,s_data)
        timestamp = time.time()
        try:
            code=pjson.json_getvalue(pjson.json_load(page),'code')
            data=pjson.json_getvalue(pjson.json_load(page),'data')
            message=pjson.json_getvalue(pjson.json_load(page),'message')
            request_id=pjson.json_getvalue(pjson.json_load(page),'request_id')
            request_time=pjson.json_getvalue(pjson.json_load(page),'request_time')
            response_time=pjson.json_getvalue(pjson.json_load(page),'response_time')
            if code == 200:
                result = 1
                send_result(tt_interface, result, tt_model, tt_case, timestamp, code, data, message, request_id, request_time, response_time)
            else:
                result = 0
                send_result(tt_interface, result, tt_model, tt_case, timestamp, code, data, message, request_id, request_time, response_time)
        except:
            result = 0
            send_result(tt_interface, result, tt_model, tt_case, timestamp, code='500', data='null', message='失败', request_id='BF0C0D0A70D2325720563604029C9303', request_time='1462948464', response_time='1462948464')
