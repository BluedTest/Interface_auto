# coding:utf-8
"""
接口自动化测试主文件(测试框架PyUnit)
"""
__author__ = 'jiaoshupeng'
import sys
import unittest
import case
import json
sys.path.append('test_execution')
import dynamic
sys.path.append('../pub_parameters')
import running

pjson = running.pjson

class ticktocks_test(unittest.TestCase):
    def setUp(self):
        print 'test start'
    def tearDown(self):
        print 'test end'
        pass
    # # 个人主页
    def test_ticktockusers(self):
        running.run_get(case.tt_case_homepage, case.post_data)
    # # 关注人（附近的、热门）动态
    def test_ticktockdynamic(self):
        running.run_get(case.ticktocks_all, case.post_data)
    # # 热门话题
    def test_topic(self):
        running.run_get(case.topic, case.post_data)
    # # 消息,动态详情
    def test_dynamic_details(self):
        running.run_get(case.dynamic, case.post_data)
    # # 发送动态
    def test_ticktocks_send(self):
        page = running.ergodic(case.ticktocks, case.ticktocks_send_data)
        #发送动态
        re = dynamic.ticktocks_send(page)
        if type(re) != int:
            ticktocks_like = {'interface':'/ticktocks/%s/liked/%s'%(str(re[1]),str(case.uid)),'model':'动态点赞','case':'创建动态点赞'}
            ticktocks_coments = {'interface':'/ticktocks/%s/comments'%(str(re[1])),'model':'动态评论','case':'创建动态->动态评论'}
            ticktocks_like_delete = {'interface':'/ticktocks/%s/liked/%s?http_method_override=DELETE'%(str(re[1]),str(case.uid)),'model':'动态点赞','case':'创建动态->动态取消点赞'}
            print ticktocks_like
            list_ticktocks_like = [ticktocks_like]
            list_ticktocks_coments = [ticktocks_coments]
            list_ticktocks_like_delete = [ticktocks_like_delete]
            #给新创建的动态点赞
            page_like = running.ergodic(list_ticktocks_like,case.post_data)
            print page_like
            dynamic.ticktocks_like(page_like)




if __name__ == '__main__':
    # unittest.main()
    # # 装载测试用例
    test_cases = unittest.TestLoader().loadTestsFromTestCase(ticktocks_test)
    # # 使用测试套件并打包测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_cases)
    # # 运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    # #生成测试报告
    print "testsRun:%s" % test_result.testsRun
    print("failures:%s" % len(test_result.failures))
    print("errors:%s" % len(test_result.errors))
    print("skipped:%s" % len(test_result.skipped))