import requests
from lxml import etree

#当当网爬虫
class DangdangSpider:
    def __init__(self):
        self.url_temp = "http://search.dangdang.com/?key={}&act=input"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

    #发送请求,获取响应
    def parse_url(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content.decode('gbk')

    #保存数据
    def save_content_list(self, content_list):
        # print(content_list)
        pass

    #提取数据
    def get_content_list(self,html_str):
        html = etree.HTML(html_str)
        li_list = html.xpath("//div[@id='search_nature_rg']//li")  # 分组
        content_list = list()
        for li in li_list:  # 遍历每个商品
            book = dict()
            book["source"] = 'dangdang'
            book_a = li.xpath("./p[@class='name']/a")
            if len(book_a) > 0:
                book_a = book_a[0] #图书的a标签
                #标题
                book["title"] = book_a.xpath("./text()")
                book["title"] = book["title"][0] if len(book["title"]) > 0 else None
                #购买链接
                book["link"] = book_a.xpath("./@href")
                book["link"] = book["link"][0] if len(book["link"]) > 0 else None
            else:
                continue
            #图片
            book["img"] = li.xpath("./a/img/@data-original")
            if len(book["img"]) > 0:
                book["img"] = book["img"][0]
            else:
                book["img"] = li.xpath("./a/img/@src")
                book["img"] = book["img"][0] if len(book["img"]) > 0 else None
            #价格
            book["price"] = li.xpath(".//span[@class='search_now_price']/text()")
            book["price"] = book["price"][0].replace('¥', '') if len(book["price"]) > 0 else None
            #商家
            book["store"] = li.xpath("./p[@class='search_shangjia']/a/text()")
            book["store"] = book["store"][0] if len(book["store"]) > 0 else '当当自营'

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
    dangdang = DangdangSpider()
    dangdang.run()