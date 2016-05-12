#!/usr/bin/env python
#encoding: utf-8

import hashlib
import os

#使用测试环境还是线上环境 0:测试环境  1:线上环境
is_online=0

if is_online==0:
	#账号列表--主态账号
	account_live=['j@qq.com',hashlib.sha1('1234').hexdigest(),138]
	#域名和网址配置
	url_ym='http://106.75.141.41'

elif is_online==1:
	#账号列表--主态账号
	account_live=['2422694497@qq.com',hashlib.sha1('1234').hexdigest(),5121265]
	#域名和网址配置
	url_ym='https://argo.blued.cn'

#-----注册和登录相关-----
zc_identity='/passport/identity'
zc_name='/passport/name'
zc_binding='/passport/binding'

#日志接口配置
interface_dir='http://106.75.141.41/qatest/autoser'


#接收警报的邮箱
# e_mail=['qa_danlan@126.com','lvduoqiang@danlan.org']