import requests
from lxml import etree
import urllib3

#京东爬虫
class JdSpider:
    def __init__(self):
        self.url_temp = "https://search.jd.com/Search?keyword={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

    #发送请求,获取响应
    def parse_url(self,url):
        urllib3.disable_warnings()
        response = requests.get(url,headers=self.headers,verify=False)
        return response.content.decode()

    #保存数据
    def save_content_list(self, content_list):
        pass

    #提取数据
    def get_content_list(self,html_str):
        # print(html_str)
        html = etree.HTML(html_str)
        li_list = html.xpath("//div[@id='J_goodsList']//li")  # 分组
        content_list = list()
        for li in li_list:  # 遍历每个商品
            book = dict()
            book["source"] = '京东'
            #标题
            book["title"] = li.xpath(".//div[contains(@class,'p-name')]/a/em/text()")
            book["title"] = book["title"][0] if len(book["title"]) > 0 else None
            #购买链接
            book["link"] = li.xpath(".//div[@class='p-name']/a/@href")
            book["link"] = 'https:'+book["link"][0] if len(book["link"]) > 0 else None
            #图片
            book["img"] = li.xpath(".//div[@class='p-img']/a/img/@data-lazy-img")
            book["img"] = 'https:'+book["img"][0] if len(book["img"]) > 0 else None
            #价格
            book["price"] = li.xpath(".//div[@class='p-price']/strong/i/text()")
            book["price"] = book["price"][0] if len(book["price"]) > 0 else None
            #商家
            book["store"] = li.xpath(".//a[@class='curr-shop hd-shopname']/@title")
            book["store"] = book["store"][0] if len(book["store"]) > 0 else None

            content_list.append(book)
        return content_list

    def run(self,isbn="9787115428028"):
        #1.准备url
        url = self.url_temp.format(isbn)
        #2.发送请求,获取响应
        html_str = self.parse_url(url)
        #3.提取数据
        content_list = self.get_content_list(html_str)
        #4.保存数据
        self.save_content_list(content_list)

        return content_list

if __name__ == '__main__':
    jd = JdSpider()
    jd.run()