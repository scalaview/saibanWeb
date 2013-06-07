#!/usr/bin/python
# -*- coding: UTF-8 -*-
import lxml
import urllib2
from lxml import etree
from StringIO import StringIO
import lxml.html as html
import time, datetime

div = 7
URL_PREFIX = 'http://bbs.dospy.com/'
path = 'http://bbs.dospy.com/forum-141-%d.html'
imgs = ['http://img.dospy.org/images/bluestyle/hot_red_folder.gif','http://img.dospy.org/images/bluestyle/red_folder.gif']
def saiban():
	content =[]
	for x in xrange(1,5):
		res = urllib2.urlopen(path % x).read()
		# print chardet.detect(res)
		doc = html.document_fromstring(res)
		for idx, el in enumerate(doc.xpath('/html/body/center/form/div/div/table')):
			f_folder_img = el.find_class('f_folder')[0].xpath('img')[0]
			gif = f_folder_img.attrib.get('src')
			# if f_folder_img.attrib.get('src')
			if gif in imgs:
				for f_title, f_time in zip(el.find_class('f_title'), el.find_class('smalltxt lighttxt')):
					td = etree.tostring(f_title, encoding='UTF-8')
					td_changed = td[td.index('</div>')+div:]
					tp = td_changed[:td_changed.index('<a')]

					tag_a = f_title.xpath('a')[0]
					url, desc =URL_PREFIX + tag_a.attrib.get('href'), tag_a.text.encode('UTF-8')

					if f_time.text is None:
						date_str = f_time.xpath('font')[0].text
						# print date_str[0].text
					else:
						date_str = f_time.text
					# print date_str
					date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(date_str, '%Y-%m-%d')))
					# print td+"%$"
					# print tp
					content.append([date, tp, url, desc])

	content.sort()
	content.reverse()
	return content


def sortedDictValues1(adict):
	items = adict.items()
	items.sort()
	return [value for key, value in items]

def main():
	return saiban()

if __name__ == '__main__':
	with open('info.txt', 'wb') as f:
		for x in  main():
			f.write("%s, %s, %s, %s\n" % (x[0], x[1], x[2], x[3]))
	# main()
		