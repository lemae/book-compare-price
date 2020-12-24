l1 = [
{'source': 'dangdang', 'title': ' Python编程从入门到实践 编程入门类图书 从基本概念到完整项目开发 帮助零基础读者迅速掌握Python编程 pyth ', 'link': 'http://product.dangdang.com/1697176075.html', 'img': 'images/model/guan/url_none.png', 'price': '90.44', 'store': '格林美图书专营店'},
    {'source': 'dangdang', 'title': ' 正版 图灵程序设计丛书 Python编程 从入门到实践 （美）马瑟斯 Python编程教程 编写代码 Web应用程序 人 ', 'link': 'http://product.dangdang.com/1593176031.html', 'img': 'images/model/guan/url_none.png', 'price': '89.70', 'store': '育博彦图书专营店'},{'source': 'dangdang', 'title': ' 【赠源代码】python编程 从入门到实践python基础教程数据分析python学习手册编程入门迅速掌握Python编 ', 'link': 'http://product.dangdang.com/1609473827.html', 'img': 'images/model/guan/url_none.png', 'price': '87.00', 'store': '晖文锦绣图书专营店'}
      ]
l1.sort(key=lambda book: book['price'])
print(l1)
