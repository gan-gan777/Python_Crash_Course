# !/usr/bin/env python3

import re, requests

SAVE_DIR_PATH = '/Users/admin/Documents/pic/20180429'
URL = 'http://www.zhihu.com.question/24279174'
save = lambda url: open(SAVE_DIR_PATH + url[url.rfind('/')+1:], 'wb').write(requests.get(url).content)

if __name__ == '__main__':
	map(save, ['http:' + url for url in re.findall(ur' <imgsrc=[\' "](//pic.+?)[\' "].+?>', requests.get(URL).content)])