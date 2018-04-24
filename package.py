#__author__='Demon'
#__date__='2018.4.24'

import json
import requests

def getPackage(package):
	try:
		#输入运单号码
		url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text='+package
		#用url1查询运单号对应的快递公司，如中通，返回：zhongtong
		companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
		#在用url2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
		url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + package 
		print('快递号对应的快递公司：',companyName)
		print('时间↓                             地点和跟踪进度↓\n')
		details ="时间↓————地点和跟踪进度↓ "
		for item in json.loads(requests.get(url2).text)['data']:
			details += item['time']+item['context']+'\n'

	except Exception as e:
		details = "运单号码有误"+repr(e)
	finally:
		print(details)

if __name__ =="__main__":
	getPackage(package='11111111')