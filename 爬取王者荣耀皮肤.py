import requests
from lxml import etree
import os
from time import sleep

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list_resp = requests.get(url=hero_list_url,headers=headers)

# print(hero_list_resp.json())
for h in hero_list_resp.json():
    # print(h)
    ename = h.get('ename')
    cname = h.get('cname')

    if not os.path.exists(cname):
        os.makedirs(cname)

    # 访问英雄主页
    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{ename}.shtml'

    hero_info_rscp =requests.get(url=hero_info_url,headers=headers)
    hero_info_rscp.encoding='gbk'  #gbk格式

    e = etree.HTML(hero_info_rscp.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    names = [name[0:name.index ('&')] for name in names.split('|')]
    # print(names.split('|'))

    for i,n in enumerate(names):
        url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg'
        # 发生请求并接受
        res = requests.get(url=url,headers=headers)
        # print(res.status_code)

        with open(f"{cname}/{n}.jpg","wb") as f:
            f.write(res.content)
        print(f'已下载：{n}的皮肤')
        sleep(1)
        #数据解析
