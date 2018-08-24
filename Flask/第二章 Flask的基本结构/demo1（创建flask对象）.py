#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
所有 Flask 程序都必须创建一个程序实例。 Web 服务器使用一种名为 Web 服务器网关接口（ Web Server Gateway Interface， WSGI）的协议，把接收自客户端的所有请求都转交给这个对象处理。
"""
# 导入flask库中的Flask中的类
from flask import Flask

# 创建flask实例对象
app = Flask(__name__)

# 入口函数
if __name__ == '__main__':
    # 启动服务器
    app.run()

"""
1.Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。在大多数程序中， Python 的 __name__ 变量就是所需的值。

2.将构造函数的 name 参数传给 Flask 程序，这一点可能会让 Flask 开发新手心生迷惑。 Flask 用这个参数决定程序的根目录，以便稍后能够找到相对于程序根目录的资源文件位置。

3.队了__name__还有其它参数，将在demo3中介绍。
"""
