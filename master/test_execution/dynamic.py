# coding:utf-8
"""
动态测试用例
"""
import sys
sys.path.append('../pub_parameters')
import running
import case
pjson = running.pjson

#发动态,检查权限和动态内容
def ticktocks_send(values):
    page = values
    dpage = page[0]
    tt_interface = page[1]
    tt_model = page[2]
    tt_case = page[3]
    timestamp = page[4]
    try:
        data=pjson.json_getvalue(pjson.json_load(dpage),'extra')
        allow_comments = pjson.json_getvalue(data,'allow_comments')
        feed_id = pjson.json_getvalue(data,'feed_id')
        feed_content = pjson.json_getvalue(data,'feed_content').encode('utf-8')
        code = pjson.json_getvalue(pjson.json_load(dpage),'code')
        message = pjson.json_getvalue(pjson.json_load(dpage),'message')
        request_id = pjson.json_getvalue(pjson.json_load(dpage),'request_id')
        request_time = pjson.json_getvalue(pjson.json_load(dpage),'request_time')
        response_time = pjson.json_getvalue(pjson.json_load(dpage),'response_time')
        if allow_comments == case.allow_comments and feed_content == case.ticktocks_send_text:
            result = 1
            running.send_result(tt_interface, result, tt_model, tt_case, timestamp, code, data, message, request_id, request_time, response_time)
            return code, feed_id, allow_comments
        else:
            result = 0
            running.send_result(tt_interface, result, tt_model, tt_case, timestamp, code, data, message, request_id, request_time, response_time)
            return code
    except:
        result = 0
        running.send_result(tt_interface, result, tt_model, tt_case, timestamp, code='500', data='null', message='失败', request_id='BF0C0D0A70D2325720563604029C9303', request_time='1462948464', response_time='1462948464')
        return code
def ticktocks_like(value_liked):
    page = value_liked
    dpage = page[0]
    tt_interface = page[1]
    tt_model = page[2]
    tt_case = page[3]
    timestamp = page[4]
    try:
        data=pjson.json_getvalue(pjson.json_load(dpage),'extra')
        allow_comments = pjson.json_getvalue(data,'allow_comments')
        feed_content = pjson.json_getvalue(data,'feed_content').encode('utf-8')
        code = pjson.json_getvalue(pjson.json_load(dpage),'code')
        message = pjson.json_getvalue(pjson.json_load(dpage),'message')
        request_id = pjson.json_getvalue(pjson.json_load(dpage),'request_id')
        request_time = pjson.json_getvalue(pjson.json_load(dpage),'request_time')
        response_time = pjson.json_getvalue(pjson.json_load(dpage),'response_time')
        if allow_comments == case.allow_comments and feed_content == case.ticktocks_send_text:
            result = 1
            running.send_result(tt_interface, result, tt_model, tt_case, timestamp, code, data, message, request_id, request_time, response_time)
        else:
            result = 0
            running.send_result(tt_interface, result, tt_model, tt_case, timestamp, code, data, message, request_id, request_time, response_time)
    except:
        result = 0
        running.send_result(tt_interface, result, tt_model, tt_case, timestamp, code='500', data='null', message='失败', request_id='BF0C0D0A70D2325720563604029C9303', request_time='1462948464', response_time='1462948464')