from dangdang_spider import DangdangSpider
from jd_spider import JdSpider

# 图书比价
def compare_price(isbn):
    # 当当网
    dangdang = DangdangSpider()
    result_list = dangdang.run(isbn)

    #京东
    jd = JdSpider()
    result_list += jd.run(isbn)

    # 按价格排序,从低到高
    result_list.sort(key=lambda book: float(book['price']))

    return result_list

if __name__ == '__main__':
    # print(compare_price("9787115428028"))
    pass