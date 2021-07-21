import requests
import json

i = 0
while i < 3:
    r = requests.get('https://api.uomg.com/api/rand.qinghua?format=text')
    _a = r.text.encode('gbk')
    f1 = open('content/test.txt', 'r+')
    f1.write(_a.decode('gbk'))
    i += 1
else:
    print('本次获取 %d' % i + '条数据，程序结束')

# i=0;
# while  i<10:
#     r = requests.get('https://api.uomg.com/api/rand.qinghua?format=json')
#     _a = r.text.encode('gbk')
#     print('序号：%d'%i+':'+_a.decode('gbk'))
#     i+=1;
# else:
#     print('本次获取 %d'%i+'条数据，程序结束')
