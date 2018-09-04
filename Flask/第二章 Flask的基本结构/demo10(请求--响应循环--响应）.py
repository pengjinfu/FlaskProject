#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
    Flask 调用视图函数后，会将其返回值作为响应的内容。大多数情况下，响应就是一个简单的字符串，作为 HTML 页面回送客户端。
    但 HTTP 协议需要的不仅是作为请求响应的字符串。 HTTP 响应中一个很重要的部分是状态码， Flask 默认设为 200，这个代码表
明请求已经被成功处理。
    如果视图函数返回的响应需要使用不同的状态码， 那么可以把数字代码作为第二个返回值，添加到响应文本之后。例如，下述视图函
数返回一个 666 状态码.


"""

from flask import Flask
# 设置cookie
from flask import make_response
# 响应由 abort 函数生成，用于处理错误
from flask import abort
# url重定向
from flask import redirect

# 创建flask实例对象
app = Flask(__name__)


# 视图函数
@app.route('/')
def hello_world():
    return 'Hello World!', 666  # 自定义响应函数


# 结果：127.0.0.1 - - [1/Aug/2018 20:33:12] "GET / HTTP/1.1" 666 -

@app.route("/aa")
def hello():
    return "Hello World", "666  i am status"  # 状态码后面的相关信息不能是中文，不能会中文乱码


# 设置cookie名字与内容
@app.route('/index')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


# 设置重定向到新的界面
@app.route('/error')
def index2():
    return redirect('http://www.example.com')


# 设置一个一异常
@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了'


# 函数入口
if __name__ == '__main__':
    # 启动服务器
    app.run()

"""
0.自定义状态码。
1.设置cookie。视图函数返回的响应还可接受第三个参数，这是一个由首部（ header）组成的字典，可以添加到 HTTP 响应中。
如果不想返回由 1 个、 2 个或 3 个值组成的元组， Flask 视图函数还可以返回 Response 对象。 make_response() 函数
可接受 1 个、 2 个或 3 个参数（和视图函数的返回值一样），并返回一个 Response 对象。有时我们需要在视图函数中进行这
种转换，然后在响应对象上调用各种方法，进一步设置响应。
2.设置重定向新的界面。
3.异常处理
"""
