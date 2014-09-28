__author__ = 'John_PC'

import webbrowser

url = ['http://www.zhihu.com', 'http://www.douban.com', 'http://github.com',
       'http://segmentfault.com', 'http://www.theverge.com/', 'http://www.quora.com']
for u in url:
    webbrowser.open_new(u)
