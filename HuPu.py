import requests
from lxml import etree




url = "http://nba.hupu.com/stats/players"

headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Host":"nba.hupu.com",
"Pragma":"no-cache",
"Referer":"https://www.google.com.hk/",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

# 发起请求
res = requests.get(url=url,headers=headers)

# 打印响应的数据
# print(res.text)

# 处理结果
e =etree.HTML(res.text)


# 解析响应数据
nos = e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
scores = e.xpath('//table[@class="players_table"]//tr/td[4]/text()')

# 是否保存
with open("nba.txt","w",encoding="utf-8") as f:
    for no,name,team,score in zip(nos[1:],names,teams,scores[1:]):
        # print(f'排名：{no} 姓名：{name} 球队：{team} 得分：{score}')
        f.write(f'排名：{no} 姓名：{name} 球队：{team} 得分：{score}\n')

"""
print("排名:",nos)
print("球员：",names)
print("球队：", teams)
"""

