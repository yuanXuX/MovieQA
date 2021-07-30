# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:30:17 2020

@author: xuyuan
"""


import time
import xlwt
from lxml import etree
import requests
import json


def processing_data(content_list):
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    # 写入excel
    for i, content in enumerate(content_list):
        for x, info in enumerate(content):
            worksheet.write(i, x, label=info)  # 将数据存入excel
    # 保存
    workbook.save('电影信息.xls')


def save_info(content):
    info = content.xpath("//div[@id='info']")[0]
    try:
        name = str(content.xpath('//*[@id="content"]/h1/span[1]/text()')[0]).replace("'", " ")
    except:
        name = "无"
    try:
        daoyan =  str(info.xpath("./span[1]/span[2]/a/text()")[0] if info.xpath("./span[1]/span[2]/a/text()") else None ).replace("'", " ")
    except:
        daoyan = "无"
    try:
        bianju =  str(info.xpath("./span[2]/span[2]/a/text()")[0] if info.xpath("./span[2]/span[2]/a/text()") else None).replace("'", " ")
    except:
        bianju = "无"
    try:
        zhuyan = '/'.join(info.xpath("./span[3]/span[2]/a/text()")).replace("'", " ")
    except:
        zhuyan = "无"
    try:
        leixing = '/'.join(info.xpath("./span[@property='v:genre']/text()")).replace("'", " ")
    except:
        leixing = "无"
    try:
        shangyingshijian= '/'.join(info.xpath(".//span[@property='v:initialReleaseDate']/text()")).replace("'", " ")
    except:
        shangyingshijian = "无"
    try:
        shichang = str(info.xpath(".//span[@property='v:runtime']/text()")[0]).replace("'", " ")
    except:
        shichang = "无"
    try:
        pingfen = str(content.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]).replace("'", " ")
    except:
        pingfen = "无"
    try:
        jianjie =  str(content.xpath('// *[ @ id = "link-report"] / span[1]/text()')[0]).replace("'", " ")
    except:
        jianjie = "无"
    # tupian = str(content.xpath('//*[@id="mainpic"]/a/img/@src')[0]).replace("https://", "")
    try:
        pingjiarenshu = content.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')[0]
    except:
        pingjiarenshu = "无"
    print("电影名称：", name)
    print("导演：", daoyan)
    print("编剧：", bianju)
    print("主演：", zhuyan)
    print("评分：", pingfen)
    print("评价人数：", pingjiarenshu)
    print("类型：", leixing)
    print("上映时间：", shangyingshijian)
    print("时长：", shichang)
    print("简介：", jianjie)
    # print("图片url：", tupian)
    one_info = [name, daoyan, bianju, zhuyan, pingfen, pingjiarenshu,leixing, shangyingshijian, shichang, jianjie]
    all_list.append(one_info)


def main():
    try:
        for x in range(0,60):
            url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%83%82%E7%89%87&start='+ str(x*20)

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
            }

            content = requests.get(url, headers=headers)
            content_json = json.loads(content.text)["data"]
            for one_info in content_json:
                one_id = one_info["id"]
                print(one_id)
                url2 = "https://movie.douban.com/subject/%s/"%one_id
                # content_html = requests.get(url, headers=headers)
                html = requests.get(url2, headers=headers)
                if html.status_code == 200:
                    content = html.content.decode("utf-8")
                    content = etree.HTML(content)
                    save_info(content)
                time.sleep(1)
    except:
        processing_data(all_list)


if __name__ == '__main__':
    all_list = []
    main()
    processing_data(all_list)
