import requests
import re
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = []
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="book-mulu"]/ul/li')
for li in li_list:
    title=li.xpath('.//a/text()')[0].encode('ISO-8859-1').decode('utf-8')# 中文乱码处理
    title_url = li.xpath('.//a/@href')[0].encode('ISO-8859-1').decode('utf-8')
    dic = {
        "title": re.sub('\s+', ' ',title),# 将有多个空格的地方替换为只有一个空格
        "title_url": 'https://www.shicimingju.com/'+title_url
    }
    data.append(dic)
print(data)
