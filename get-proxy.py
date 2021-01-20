#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: 蘑菇君
# @Date  : 2021/01/03
# @Desc  : 自动获取免费代理IP

import threading

from rules import *

proxy_ok_ip = []  # 验证后的代理IP列表


# 复写Thread类
class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


# 获取普通代理IP函数
def get_ip():
    # 定义一个获取IP的线程池，如果你有其他接口可以往里加
    threads_ip = [MyThread(ip_api, args=(
        "http://www.66ip.cn/mo.php?sxb=&tqsl=7000&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=", "66免费代理")),
                  MyThread(ip_html2, args=("https://www.kuaidaili.com/free/intr/", "快代理", 20, 2)),
                  MyThread(ip_html2, args=("http://www.ip3366.net/free/?stype=2&page=", "云代理", 7, 1)),
                  MyThread(ip_api, args=(
                      "http://www.89ip.cn/tqdl.html?api=1&num=3000&port=&address=&isp=", "89免费代理(未知类型)")),
                  MyThread(ip_html1, args=("http://www.nimadaili.com/putong/", "泥马代理", 100, 1)),
                  MyThread(ip_html1, args=("http://www.xiladaili.com/putong/", "西拉代理", 100, 1)),
                  MyThread(ip_article1, args=("https://www.zdaye.com/dayProxy.html", "站大爷(未知类型)", 14, 4)),
                  MyThread(ip_html2, args=("http://www.kxdaili.com/dailiip/2/", "开心代理", 9, 2))]
    for b in threads_ip:
        b.start()
    for b in threads_ip:
        b.join()


# 获取匿名代理IP函数
def get_anonymous_ip():
    # 定义一个获取IP的线程池，如果你有其他接口可以往里加
    threads_ip = [MyThread(ip_api, args=(
        "http://www.66ip.cn/nmtq.php?getnum=3000&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip",
        "66免费代理")),
                  MyThread(ip_html2, args=("https://www.kuaidaili.com/free/inha/", "快代理", 20, 2)),
                  MyThread(ip_html2, args=("http://www.ip3366.net/free/?stype=1&page=", "云代理", 7, 1)),
                  MyThread(ip_api, args=(
                      "http://www.89ip.cn/tqdl.html?api=1&num=3000&port=&address=&isp=", "89免费代理(未知类型)")),
                  MyThread(ip_html1, args=("http://www.nimadaili.com/gaoni/", "泥马代理", 100, 1)),
                  MyThread(ip_html1, args=("http://www.xiladaili.com/gaoni/", "西拉代理", 100, 1)),
                  MyThread(ip_html2, args=("https://www.7yip.cn/free/?action=china&page=", "齐云代理", 90, 2)),
                  MyThread(ip_html2, args=("https://ip.jiangxianli.com/?page=", "高可用全球免费代理库", 8, 0)),
                  MyThread(ip_article1, args=("http://www.xsdaili.cn/", "小舒代理", 6, 2)),
                  MyThread(ip_article1, args=("https://www.zdaye.com/dayProxy.html", "站大爷(未知类型)", 14, 4)),
                  MyThread(ip_html2, args=("http://www.kxdaili.com/dailiip/1/", "开心代理", 9, 2)),
                  MyThread(ip_html4, args=("http://http.taiyangruanjian.com/free/page", "太阳HTTP", 7, 2)),
                  MyThread(ip_article2, args=("https://ip.ihuan.me/today.html", "小幻HTTP代理", 2))]
    for b in threads_ip:
        b.start()
    for b in threads_ip:
        b.join()


# 验证代理函数
def check_ip(ip, site, word, code):
    global proxy_ok_ip
    try:
        proxy_temp = {"http": ip, "https": ip}
        res = requests.get(site, headers=headers, proxies=proxy_temp, timeout=10)  # 验证超时时间，默认10秒
        if code == "2":
            res.encoding = "gbk"
        else:
            res.encoding = "utf-8"
        if word in res.text:  # 判断关键词是否在网站源码中
            # print(res, ip + "  is OK")
            proxy_ok_ip.append(ip)
        else:
            # print(ip + "  is BOOM")
            pass
    except:
        # print(ip + "  is BOOM")
        pass


# 列表写入json文件函数：filename为写入json文件的路径，data为要写入数据列表
def text_save(filename, data):
    file = open(filename, "w+")
    content = {
        "total": len(data),
        "data": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "ip": data
    }
    file.write(str(content).replace("'", '"'))
    file.close()
    print("代理IP信息保存文件成功，请查看当前运行目录！")


# 列表去重函数
def check_list(lists):
    temp = []
    for i in lists:
        if i not in temp:
            temp.append(i)
    return temp


if __name__ == "__main__":
    input_ip_type = input("请选择你要获取的代理IP类型(1.普通 2.高匿(默认))：")
    input_thread_num = 500  # 验证的线程数（默认500）
    input_wait_time = input("请输入每次重新获取的间隔时间，免费IP不要太快，单位（秒）：")

    while True:
        proxy_ip.clear()  # 代理IP列表
        proxy_ok_ip.clear()  # 验证后的代理IP列表
        if input_ip_type == "1":
            print("\n正在获取[普通]代理IP中请稍等片刻，大概3min... _(:з」∠)_")
            get_ip()
        else:
            print("\n正在获取[高匿]代理IP中请稍等片刻，大概3min... _(:з」∠)_")
            get_anonymous_ip()
        ip_list = check_list(proxy_ip)  # 去重

        # 验证可用性✔
        demo_site = "https://www.baidu.com"
        demo_code = str(1)  # 1.UTF-8(默认) 2.GBK
        demo_word = "百度一下"  # 如 “https://www.baidu.com” 中有关键字符串 “百度一下” ：")

        # 多线程验证开始，GO! GO! GO!
        k = 0
        threads = []  # 定义一个线程池
        thread_count = len(ip_list) // int(input_thread_num) + 1  # 分几段线程
        for i in range(thread_count):
            for j in range(int(input_thread_num)):  # 一段几线程
                try:
                    # 创建新线程,添加到线程池
                    threads.append(MyThread(check_ip, args=(ip_list[k], demo_site, demo_word, demo_code)))
                    k += 1
                except:
                    break
        # 开启所有线程
        for t in threads:
            t.start()
        # 等待所有线程完成
        for t in threads:
            t.join()
        print("共获取到" + str(len(ip_list)) + "个代理IP，可用IP总数为" + str(len(proxy_ok_ip)) + "个")
        text_save("proxy_ip.json", proxy_ok_ip)

        time.sleep(int(input_wait_time))
        print("\n循环获取ing...\n")
