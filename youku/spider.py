#!/usr/bin/python
#-*- coding:utf-8 -*-

import os,codecs,urllib2
from bs4 import BeautifulSoup

class SpiderHTML(object):
	#打开页面
	def getUrl(self, url, coding = 'utf-8'):
		header = { 'User-Agent' : 'Mozilla/5.0' }
		req = urllib2.Request(url, None, header)
		html = urllib2.urlopen(req).read()
		return BeautifulSoup(html.decode(coding), "html5lib")

	def getUrlwithoutHead(self, url, coding = 'utf-8'):
		req = urllib2.Request(url)
		html = urllib2.urlopen(req).read()
		return BeautifulSoup(html.decode(coding), "html5lib")

	#保存文本内容到本地
	def saveText(self,filename,content,mode='w'):
		self._checkPath(filename)
		with codecs.open(filename, encoding='utf-8', mode=mode) as f:
			f.write(content)
		
	#保存图片
	def saveImg(self, imgUrl, imgName):
		if os.path.exists(imgName):
			pass
		else:
			header = { 'User-Agent' : 'Mozilla/5.0' }
			req = urllib2.Request(imgUrl, None, header)
			data = urllib2.urlopen(req).read()
			self._checkPath(imgName)
			f = open(imgName,'wb')
			f.write(data)
			f.close()

	#创建目录
	def _checkPath(self, path):
		dirname = os.path.dirname(path.strip())
		if not os.path.exists(dirname):
			os.makedirs(dirname)
