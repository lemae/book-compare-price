import requests
import urllib3
from lxml import etree
import re
import json

#淘宝爬虫
class TaobaoSpider:
    def __init__(self):
        self.url_temp = "https://s.taobao.com/search?q={}"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Cookie": "mt=ci%3D-1_1; enc=DcvrGzibBErTzV2bxqRIBz%2FJeCEkKL8Za%2BrvsKgbDFGh2P%2F1U4mHGMFH9WJecj0H7SMhybcg11%2B%2FW7Jjb%2FmtgA%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; cna=2orGF3J6gRkCAQ53udAX8IZH; miid=600577371734573616; tracknick=%5Cu6C89%5Cu6108%5Cu6D1B%5Cu71D5; _cc_=UIHiLt3xSw%3D%3D; sgcookie=E100W4w%2F1nisYZAGtiIsOz8TjA90uT0uZJDO7VECcumlP1qb%2BFIz39hANQk88Sf9Y%2B8Fmp%2BtBavdBtg%2F%2FFiN0bD4fQ%3D%3D; t=56f1a2ee02d5ab23b63ac174d6984299; birthday_displayed=1; mt=ci%3D-1_1; _uab_collina=160870413220138739862789; v=0; _tb_token_=e3e3595eee3e7; _m_h5_tk=fee2867a002f67a647753c64428d00a3_1609066167693; _m_h5_tk_enc=8e97996ae6aabc02d6118614b3f2a917; xlly_s=1; JSESSIONID=A80F5E31D64FAA2E6F9DD244212A410F; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; tfstk=c2ORBOqa9mmo09bv7LH0dGpLoM3cZFaRxzsL9VrD4l7_siPdiHRM6d6iFwrRMqC..; isg=BAMDd1PkWIKHWhTScOlQuow5kseteJe6DzzIdDXgVmLZ9CMWvUmaCmJmaoS61O-y; l=eBTqmYNrObZJvAgEBOfZnurza77TsIRAguPzaNbMiOCPOS1p5-aOWZ-OYhY9CnGVh6v6R3Scn0QBBeYBqIv4n5U62j-la6Dmn"
        }

    #发送请求,获取响应
    def parse_url(self,url):
        urllib3.disable_warnings()
        response = requests.get(url,headers=self.headers,verify=False)
        return response.content.decode()

    #保存数据
    def save_content_list(self, content_list):
        pass
        # print(content_list)

    #提取数据, 如果获取失败, 则返回None
    def get_content_list(self,html_str):
        match_obj = re.search(r'g_page_config = ({[\s|\S]*?});$',html_str,re.M)
        if match_obj is None:   #获取失败
            return None
        res = json.loads(match_obj.group(1))    #结果字典

        item_list = res['mods']['itemlist']['data']['auctions'] #商品列表
        content_list = list()
        for item in item_list:  # 遍历每个商品
            book = dict()
            book["source"] = '淘宝'
            if 'i2iTags' not in item: continue
            #标题
            book["title"] = item['raw_title']
            #购买链接
            book["link"] = "https://item.taobao.com/item.htm?id={}".format(item['nid'])
            #图片
            book["img"] = 'https:'+item['pic_url']
            #价格
            book["price"] = item['view_price']
            #商家
            book["store"] = item['nick']

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
    taobao = TaobaoSpider()
    taobao.run()