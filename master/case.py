# coding:utf-8

import sys
sys.path.append('../pub_parameters')
import ia_configure
uid = ia_configure.account_live[2]
post_data = ''
#----------------------动态相关----------------------------

#个人主页
info_person = {'interface':'/users/%s'%uid,'model':'个人主页','case':'个人主页加载个人信息'}
info_ticktock = {'interface':'/ticktocks/users/%s/timeline'%uid,'model':'个人主页','case':'个人主页加载个人动态信息'}
tt_case_homepage =[info_person,info_ticktock]

#关注人（附近的、热门）动态
ticktocks_follows = {'interface':'/ticktocks/users/%s?filter=follows&gmt=28800&page=1'%uid,'model':'动态相关','case':'动态关注第一页'}
ticktocks_follows_page2 = {'interface':'/ticktocks/users/%s?filter=follows&gmt=28800&page=2'%uid,'model':'动态相关','case':'动态关注第二页'}
ticktocks_hot = {'interface':'/ticktocks/users/%s?filter=hot&gmt=28800&page=1'%uid,'model':'动态相关','case':'动态热门第一页'}
ticktocks_hot_page2 = {'interface':'/ticktocks/users/%s?filter=hot&gmt=28800&page=2'%uid,'model':'动态相关','case':'动态热门第二页'}
ticktocks_nearby = {'interface':'/ticktocks/users/%s?filter=nearby&gmt=28800&lat=39.89995198567708&lot=116.47044921875&page=1'%uid,'model':'动态相关','case':'动态附近第一页'}
ticktocks_nearby_page2 = {'interface':'/ticktocks/users/%s?filter=nearby&gmt=28800&lat=39.89995198567708&lot=116.47044921875&page=2'%uid,'model':'动态相关','case':'动态附近第一页'}
ticktocks_all = [ticktocks_follows,ticktocks_follows_page2,ticktocks_hot,ticktocks_hot_page2,ticktocks_nearby,ticktocks_nearby_page2]

#热门话题
topic_hot = {'interface':'/ticktocks/topics/hot?filter=list&page=1&size=20','model':'动态相关','case':'热门话题列表'}
topic_hot_detail = {'interface':'/ticktocks/topics?name=GG&filter=hot&page=1&size=20','model':'动态相关','case':'名称为GG的话题详情'}
topic = [topic_hot,topic_hot_detail]

#消息,动态详情
dynamic_news_list = {'interface':'/ticktocks/users/%s/information?filter=comments&isoffset=1&offset=0&size=20'%uid,'model':'动态相关','case':'动态消息列表'}
#198为点击评论人的uid,请自行修改
dynamic_detail = {'interface':'/ticktocks/198/comments?gmt=28800&page=1','model':'动态相关','case':'动态消息->动态详情'}
praise_me = {'interface':'/ticktocks/users/%s/information?filter=liked&isoffset=1&offset=0&size=20'%uid,'model':'动态相关','case':'动态消息->赞过我的'}
dynamic = [dynamic_news_list,dynamic_detail,praise_me]

#发动态
allow_comments = 2
ticktocks_send_text = 'happy one day'
ticktocks_send = {'interface':'/ticktocks/me','model':'动态相关','case':'发送动态(allow_comments=%s text=%s)'%(allow_comments, ticktocks_send_text)}
ticktocks_send_data = {"phone":"iPhone","os":"ios9.3.1","send":"1","allow_comments":allow_comments,"text":ticktocks_send_text,"lot":"116.4704760742188","lat":"39.89992024739583","gmt":"28800"}
ticktocks = [ticktocks_send]




