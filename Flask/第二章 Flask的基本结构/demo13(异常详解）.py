#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
HTTP 异常主动抛出:
abort 方法
    抛出一个给定状态代码的 HTTPException 或者 指定响应，例如想要用一个页面未找到异常来终止请求，你可以调用 abort(404)。
参数：
    code – HTTP的错误状态码

捕获错误:
errorhandler 装饰器
    注册一个错误处理程序，当程序抛出指定错误状态码的时候，就会调用该装饰器所装饰的方法
参数：
    code_or_exception – HTTP的错误状态码或指定异常
"""
from flask import Flask, abort, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    # 主动产生一个404的错误
    # 参数1：必须是http的错误状态码
    # abort(404)
    a = 1 / 0
    return 'Hello World!'

# 输入：http://127.0.0.1:5000/dfsadfks   由于这个页面不存在，所以会报错404
@app.errorhandler(404)
def error1(error):
    print(error)
    # 捕获404异常 然后重定向到小米404错误页面
    return redirect("http://hd.mi.com/webfile/zt/hd/2014042802/cn.html")


@app.errorhandler(ZeroDivisionError)
def error2(error):
    print(error)
    # 捕获404异常 然后重定向到小米404错误页面
    return "不能除0"


if __name__ == '__main__':
    app.run(debug=True)
