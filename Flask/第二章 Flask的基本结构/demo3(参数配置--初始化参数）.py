#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1

from flask import Flask

# 创建flask实例对象
# app = Flask(__name__)    平时可以这样写，默认就可以

# 可以对指定参数进行更改，但个人建议最好不要
app = Flask(__name__,
            static_url_path=None,
            static_folder='static',
            static_host=None,
            host_matching=False,
            subdomain_matching=False,
            template_folder='templates',
            instance_path=None,
            instance_relative_config=False,
            root_path=None)

if __name__ == '__main__':
    app.run()

"""
1.Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。在大多数程序中， Python 的 __name__ 
变量就是所需的值。

2.将构造函数的 name 参数传给 Flask 程序，这一点可能会让 Flask 开发新手心生迷惑。 Flask 用这个参数决定程序的
根目录，以便稍后能够找到相对于程序根目录的资源文件位置。

3.参数说明：
    static_url_path = None,  # 静态文件目录的url路径 默认不写是与static_folder同名,远程静态文件时复用

    static_folder = 'static',  # 静态文件目录的路径 默认当前项目中的static目录

    static_host = None,  # 远程静态文件所用的Host地址,默认为空

    # host_matching是否开启host主机位匹配,是要与static_host一起使用,如果配置了static_host, 则必须赋值为True
    # 这里要说明一下,@app.route("/",host="localhost:5000") 就必须要这样写
    # host="localhost:5000" 如果主机头不是 localhost:5000 则无法通过当前的路由
    host_matching = False,  # 如果不是特别需要的话,慎用,否则所有的route 都需要host=""的参数

    subdomain_matching = False,  # 理论上来说是用来限制SERVER_NAME子域名的,但是目前还没有感觉出来区别在哪里

    template_folder = 'templates'  # template模板目录, 默认当前项目中的 templates 目录

    instance_path = None,  # 指向另一个Flask实例的路径

    instance_relative_config = False  # 是否加载另一个实例的配置

    root_path = None  # 主模块所在的目录的绝对路径,默认项目目录
"""
