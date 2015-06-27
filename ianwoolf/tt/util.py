#!/bin/python
import httplib, sys

def ReadGpData(Num):
	gp_no = Num
	error_status = ["499","403","500"]
	conn = httplib.HTTPConnection("hq.sinajs.cn", 80, False)
	conn.request('get', '/list='+gp_no, headers = {"Host": "hq.sinajs.cn",
                                    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                                    "Accept": "text/plain"})
	res = conn.getresponse()
	if res.status not in error_status:
        	result = res.read().decode('gb2312').encode('utf8').strip("\n")
	else:
        	print "error"
	        print 'reason:', res.reason
        	print 'msg:', res.msg
        	print 'headers:', res.getheaders()
	conn.close()
        result = result.split("=")[1].strip(";").strip('"')
        return result
