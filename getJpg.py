import re
import urllib


# get the source code of a website
def getHtml(url):
    print 'Getting html source code..'
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImageAddrList(html):
    print 'Getting all address of images...'
    rule = r'src="(.+?\.jpg)" pic_ext'
    imReg = re.compile(rule)
    imList = re.findall(imReg,html)
    return imList

def getImage(imList):
	print 'DownLoading'
	name = 1;
	for imgurl in imList:
	     urllib.urlretrieve(imgurl,'%s.jpg' % name)
	     name += 1
	print 'got ',len(imList),' images'

## main
htmlAddr = "http://tieba.baidu.com/p/2510089409"
html = getHtml(htmlAddr)
imList = getImageAddrList(html)
getImage(imList)
