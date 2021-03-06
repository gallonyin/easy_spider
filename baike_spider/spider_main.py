__author__ = 'Gallon'
# coding:utf-8

from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 20:
                    break
                count += 1
            except:
                print("craw failed!")

        self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/Python"
    # root_url = "https://baike.baidu.com/item/%E5%8D%A1%E5%86%85%E5%9F%BA%C2%B7%E6%A2%85%E9%9A%86%E5%A4%A7%E5%AD%A6/514335?fromtitle=%E5%8D%A1%E8%80%90%E5%9F%BA%E6%A2%85%E9%9A%86%E5%A4%A7%E5%AD%A6&fromid=5383421"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)