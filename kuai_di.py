import requests
url = 'https://www.kuaidi100.com/query'
wed =input('请输入查询的物流名称拼音：')
num = input('请输入单号：')

headers = {
    'Host': 'www.kuaidi100.com',
    'Referer': 'https://www.kuaidi100.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

params = {
'type': wed,
'postid': num,
'temp': '0.6062045325692598',
'phone': ''
}
res = requests.get(url,headers=headers,params=params)
jie = res.json()
xin_xi = jie['data']
for i in xin_xi:
    print(i['time'] + i['context'])




# import requests
# #调用requests模块，负责上传和下载数据

# logisticsName = input('你的快递是什么物流呀？')
# courierNum = input('你的快递单号是什么呀？')

# url = 'https://www.kuaidi100.com/query?'
# #使用get需要一个链接

# headers = {
#     'Host': 'www.kuaidi100.com',
#     'Referer': 'https://www.kuaidi100.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
# }

# params = {
#           'type': logisticsName,
#           'postid': courierNum,
#           'temp': '0.9661515218223198',
#           'phone':''
#           }
# #将需要get的内容，以字典的形式记录在params内

# r = requests.get(url,headers=headers,params=params)
# #get需要输入两个参数，一个是刚才的链接，一个是params，返回的是一个Response对象
# result = r.json()

# print ('最新物流状态‘：'+ result['data'][0]['context'])