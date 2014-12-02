#!/usr/bin/python  
#coding:utf8

import re,urllib
url  = "http://music.baidu.com/top/oldsong"
openurl = urllib.URLopener()
headers = ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36')
openurl.addheaders = [headers]
data = openurl.open(url).read()
data = data.decode('utf8')
music_sid = re.findall(re.compile(r"'sid': '(.*)', 'author'"),data)
music_sname = re.findall(re.compile(r"'author': '(.*)', 'sname'"),data)
music_author = re.findall(re.compile(r"'sname':'(.*)' }"),data)
file = open('downurl.txt','w')
print len(music_sid)
for i in range(len(music_sid)):
#  file.write(sid[i]+name[i]+'\n')
	print str(i) + ':     ' + music_sname[i] + " --" + music_author[i]
	da = openurl.open('http://music.baidu.com/song/%s/download'%str(music_sid[i])).read()
	downurl = re.findall(re.compile(r'downlink = "/data/music/file\?link=(.*)"type'),da)
	file.write(downurl[0]+'\n')
	print '%s music file download ing ..........'%music_sname[i]
	urllib.urlretrieve(downurl[0],music_sname[i] + "-" + music_author[i]+'.mp3')
	print '-'*50
file.close