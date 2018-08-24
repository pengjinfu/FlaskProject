#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
在 Flask 中，定义一个路由，默认的请求方式为：
    GET
    OPTIONS(自带)
    HEAD(自带)

前面也提到了请求方式，浏览器只能看到get请求，如果用模拟post请求，就需要使用 PostMan 软件对请求进行测试。
"""
from flask import Flask


app = Flask(__name__)


# 127.0.0.1:5000/demo1 --> demo1视图函数
@app.route("/demo1")
def demo1():
    return "demo1"


# 127.0.0.1:5000/user/1 --> demo2视图函数
# <变量>转换器的方式提取参数：默认是str类型
@app.route("/user/<user_id>")
def demo2(user_id):
    return "demo2  %s" % user_id


# 127.0.0.1:5000/user_int/1 --> demo3视图函数
# <int: 变量>转换器的方式提取参数：就是int类型
@app.route("/user_int/<int:user_id>")
def demo3(user_id):
    return "demo3  %d" % user_id


# 修改访问方式：记得要用PostMan 软件对请求进行测试
# 通过methods列表属性修改视图函数的请求方式
@app.route("/demo4", methods=["POST"])
def demo4():
    return "demo4"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)


