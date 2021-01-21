# FreeProxyPool 免费代理IP池
多线程爬取多个免费代理IP网站，获取并验证可用代理IP，构建免费代理池，内含多种爬取规则，支持定时爬取，对接 10+ 免费代理源，返回JSON格式，方便对接其他程序

```
 _____   _____    _____   _____   _____   _____    _____  __    __ __    __  _____   _____   _____   _      
|  ___| |  _  \  | ____| | ____| |  _  \ |  _  \  /  _  \ \ \  / / \ \  / / |  _  \ /  _  \ /  _  \ | |     
| |__   | |_| |  | |__   | |__   | |_| | | |_| |  | | | |  \ \/ /   \ \/ /  | |_| | | | | | | | | | | |     
|  __|  |  _  /  |  __|  |  __|  |  ___/ |  _  /  | | | |   }  {     \  /   |  ___/ | | | | | | | | | |     
| |     | | \ \  | |___  | |___  | |     | | \ \  | |_| |  / /\ \    / /    | |     | |_| | | |_| | | |___  
|_|     |_|  \_\ |_____| |_____| |_|     |_|  \_\ \_____/ /_/  \_\  /_/     |_|     \_____/ \_____/ |_____| 
```


### 已支持的免费代理源
如果有新的质量不错的免费代理网站，欢迎反馈或者根据规则尝试自行适配！

| 代理名称 | 状态 | 地址 |
| ------- | ---- | ---- |
| 66免费代理 | √ | <http://www.66ip.cn> |
| 快代理 | √ | <https://www.kuaidaili.com> |
| 云代理 | √ | <http://www.ip3366.net> |
| 89免费代理 | √ | <http://www.89ip.cn> |
| 泥马代理 | √ | <http://www.nimadaili.com> |
| 西拉代理 | √ | <http://www.xiladaili.com> |
| 站大爷 | √ | <https://www.zdaye.com> |
| 开心代理 | √ | <http://www.kxdaili.com> |
| 高可用全球免费代理库 | √ | <https://ip.jiangxianli.com> |
| 小舒代理 | √ | <http://www.xsdaili.cn> |
| 太阳HTTP | √ | <http://http.taiyangruanjian.com> |
| 小幻HTTP代理 | √ | <https://ip.ihuan.me> |
| 齐云代理 | √ | <https://www.7yip.cn> |


### 使用说明
1. 安装需要的支持库 `pip install -r requirements.txt`

2. 运行 `get-proxy.py`，根据提示输入即可


### 运行结果

![jieguo](https://raw.githubusercontent.com/Fog-Forest/free-proxy-pool/main/demo.png)


### 注意事项
本项目仅仅是一个简单的脚本，请勿用作非法用途，通常免费代理质量都较差，不建议用于爬虫，本项目依然不够完善，后续随缘更新，如果发现 bug 或有新的功能添加，欢迎在 [Issues](https://github.com/Fog-Forest/free-proxy-pool/issues) 中反馈，同时也可以到我的 [博客](https://m1314.cn/) 中留言。
