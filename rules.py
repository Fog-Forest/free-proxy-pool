#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: 蘑菇君
# @Date  : 2021/01/03
# @Desc  : 网站爬取规则

import re
import time

import requests
from bs4 import BeautifulSoup

# 全局变量
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

proxy_ip = []  # 代理IP列表


# 1. 使用正则获取代理IP函数(接口提取形式):提取接口URL、备注名称
def ip_api(link, text):
    global proxy_ip
    ip_num = 0
    try:
        url = str(link)
        response = requests.get(url, headers=headers, timeout=8)
        temp = re.findall(r'(\d+.\d+.\d+.\d+:\d+)', response.text)
        for ip in temp:
            ip_num += 1  # 自增计算IP数
            proxy_ip.append(ip)
    except Exception as e:
        print(e)
    print(str(text) + "获取到" + str(ip_num) + "个代理IP")


# 2. 使用HTML解析获取代理IP函数【一】(源码IP和端口在一起且在第1个<td>标签内):网页链接、备注名称、爬取页数、爬取速度
def ip_html1(link, text, page, speed):
    global proxy_ip
    ip_num = 0
    try:
        for a in range(1, page):  # 爬取多少页
            url = str(link) + str(a)
            response = requests.get(url, headers=headers, timeout=8)
            # print(response.text)
            soupIP = BeautifulSoup(response.text, 'html5lib')
            trs = soupIP.find_all('tr')
            for tr in trs[1:]:
                ip_num += 1  # 自增计算IP数
                tds = tr.find_all('td')
                # print(tds)
                ip = tds[0].text.strip()
                proxy_ip.append(ip)
            time.sleep(speed)  # 控制访问速度(很重要，如果访问太快被封IP就不能继续爬了)
    except Exception as e:
        print(e)
    print(str(text) + "获取到" + str(ip_num) + "个代理IP")


# 3. 使用HTML解析获取代理IP函数【二】(源码IP和端口不在一起,IP在第1个<td>标签内,端口在第2个<td>标签内):网页链接、备注名称、爬取页数、爬取速度
def ip_html2(link, text, page, speed):
    global proxy_ip
    ip_num = 0
    try:
        for a in range(1, page):  # 爬取多少页

            # 部分URL特殊处理
            if "www.kxdaili.com" in link.split("/"):
                url = str(link) + str(a) + ".html"
            else:
                url = str(link) + str(a)

            response = requests.get(url, headers=headers, timeout=8)
            soupIP = BeautifulSoup(response.text, 'html5lib')
            trs = soupIP.find_all('tr')
            for tr in trs[1:]:
                ip_num += 1  # 自增计算IP数
                tds = tr.find_all('td')
                # print(tds)
                ip = tds[0].text.strip()
                port = tds[1].text.strip()
                proxy_ip.append(ip + ':' + port)
            time.sleep(speed)  # 控制访问速度(很重要，如果访问太快被封IP就不能继续爬了)
    except Exception as e:
        print(e)
    print(str(text) + "获取到" + str(ip_num) + "个代理IP")


# 4. 使用HTML解析获取代理IP函数【三】(源码IP和端口不在一起,IP在第2个<td>标签内,端口在第3个<td>标签内):网页链接、备注名称、爬取页数、爬取速度
def ip_html3(link, text, page, speed):
    global proxy_ip
    ip_num = 0
    try:
        for a in range(1, page):  # 爬取多少页
            url = str(link) + str(a)
            response = requests.get(url, headers=headers, timeout=8)
            # print(response.text)
            soupIP = BeautifulSoup(response.text, 'html5lib')
            trs = soupIP.find_all('tr')
            for tr in trs[1:]:
                ip_num += 1  # 自增计算IP数
                tds = tr.find_all('td')
                # print(tds)
                ip = tds[1].text.strip()
                port = tds[2].text.strip()
                proxy_ip.append(ip + ':' + port)
            time.sleep(speed)  # 控制访问速度(很重要，如果访问太快被封IP就不能继续爬了)
    except Exception as e:
        print(e)
    print(str(text) + "获取到" + str(ip_num) + "个代理IP")


# 5. 使用HTML解析获取代理IP函数【四】(源码IP和端口不在一起,IP在第1个<div class="td">标签内,端口在第2个<div class="tr">标签内):网页链接、备注名称、爬取页数、爬取速度
def ip_html4(link, text, page, speed):
    global proxy_ip
    ip_num = 0
    try:
        for a in range(1, page):  # 爬取多少页
            url = str(link) + str(a)
            response = requests.get(url, headers=headers, timeout=8)
            soupIP = BeautifulSoup(response.text, 'html5lib')
            divs = soupIP.find_all('div', class_="tr")
            for div in divs[1:]:
                ip_num += 1  # 自增计算IP数
                tds = div.find_all('div', class_="td")
                # print(tds)
                ip = tds[0].text.strip()
                port = tds[1].text.strip()
                proxy_ip.append(ip + ':' + port)
            time.sleep(speed)  # 控制访问速度(很重要，如果访问太快被封IP就不能继续爬了)
    except Exception as e:
        print(e)
    print(str(text) + "获取到" + str(ip_num) + "个代理IP")


# 6. 小舒代理函数(发布代理文章这类的网站):网页链接、备注名称、爬取页数、爬取速度
def ip_article1(link, text, page, speed):
    global proxy_ip
    ip_num = 0
    try:
        url = str(link)
        response = requests.get(url, headers=headers, timeout=8)
        page_urls = re.findall(r'(?<=href="/dayProxy/ip/).*?(?=">20)', response.text)
        for a in range(int(page)):  # 爬取前几篇文章内容

            # 部分URL特殊处理
            if "www.zdaye.com" in link.split("/"):
                page_url = "https://www.zdaye.com/dayProxy/ip/" + page_urls[a]
            else:
                page_url = link + "dayProxy/ip/" + page_urls[a]

            # 爬取文章内容
            article = requests.get(page_url, headers=headers, timeout=8)
            temp = re.findall(r'(\d+.\d+.\d+.\d+:\d+)', article.text)
            for ip in temp:
                ip_num += 1  # 自增计算IP数
                proxy_ip.append(ip)
            time.sleep(speed)
    except Exception as e:
        print(e)
    print(str(text) + "获取到" + str(ip_num) + "个代理IP")


# 7. 小幻HTTP代理函数(小幻HTTP代理专用):网页链接、备注名称、爬取速度
def ip_article2(link, text, speed):
    global proxy_ip
    ip_num = 0
    try:
        response = requests.get(link, headers=headers, timeout=20)
        soupIP = BeautifulSoup(response.text, 'html5lib')
        divs = soupIP.find_all('div', class_='bs-callout bs-callout-info')
        for div in divs:
            ip_num += 1  # 自增计算IP数
            hrefs = div.find_all('a')
            url = hrefs[0].attrs['href']

            # 爬取文章内容
            article = requests.get("https://ip.ihuan.me/today" + url, headers=headers, timeout=20)
            temp = re.findall(r'(\d+.\d+.\d+.\d+:\d+)', article.text)
            for ip in temp:
                ip_num += 1  # 自增计算IP数
                proxy_ip.append(ip)
            time.sleep(speed)  # 控制访问速度(很重要，如果访问太快被封IP就不能继续爬了)
    except Exception as e:
        print(e)
    print(str(text) + "获取到" + str(ip_num) + "个代理IP")
