#!/usr/bin/python
#-*- coding:utf-8 -*-

import spider, sys
from bs4 import BeautifulSoup
from os import path, system, mkdir

__doc__ = '''
Usage: ./youku.py [url]... [path]
	url: The video list in youku
	path: The path to store video
'''

def spiderYouku(url, store_path):
	h = spider.SpiderHTML()
	html_obj = h.getUrlwithoutHead(url)
	c = html_obj.find_all(class_='v-link')
	a = []
	for item in c:
		a.append(BeautifulSoup(str(item), 'html5lib').a['href'])
	if store_path != '':
		if path.exists(store_path) == False:
			mkdir(store_path)
		for link in a:
			system('you-get -o ' + store_path + ' ' + link)
	else:
		for link in a:
			system('you-get ' + link)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(__doc__)
	else:
		if len(sys.argv) < 3:
			spiderYouku(sys.argv[1])
		else:	
			spiderYouku(sys.argv[1], sys.argv[2])