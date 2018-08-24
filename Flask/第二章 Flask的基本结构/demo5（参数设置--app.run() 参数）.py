#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
# 导入flask库中的Flask中的类
from flask import Flask

# 创建flask实例对象
app = Flask(__name__)

# 入口函数
if __name__ == '__main__':
    # 启动服务器
    """
    run(self, host=None, port=None, debug=None,
            load_dotenv=True, **options)
    """
    app.run(host=None, port=None, debug=None,load_dotenv=True)

"""
参数说明：
1.host:默认的主机为你自己的本地电脑：127.0.0.1或localhost。可以更改为你的ip，若ip设置为0.0.0.0所的ip都可以访问你的服务器。
2.port:默认为5000，可以自行设置。
3.debug:默认不开启，设置为True为开启。
4.options:选项参数是将server的参数传送到Werkzeug server去处理。
"""