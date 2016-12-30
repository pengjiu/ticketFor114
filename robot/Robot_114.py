'''
Created on 2016年12月26日

@author: pengjiu
'''
import cookielib
import mechanize
 
class Robot_114:
    def __init__(self):
        cookiejar = cookielib.LWPCookieJar()
        br = mechanize.Browser()
        br.set_cookiejar(cookiejar)
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36')]
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        self.br=br;
    def Login(self):