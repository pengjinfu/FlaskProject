#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
请求勾子:
    在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：

        在请求开始时，建立数据库连接；
        在请求开始时，根据需求进行权限校验；
        在请求结束时，指定数据的交互格式；
        为了让每个视图函数避免编写重复功能的代码，Flask提供了通用设施的功能，即请求钩子。

    请求钩子是通过装饰器的形式实现，Flask支持如下四种请求钩子：

        before_first_request
            在处理第一个请求前执行
        before_request
            在每次请求前执行
            如果在某修饰的函数中返回了一个响应，视图函数将不再被调用
        after_request
            如果没有抛出错误，在每次请求后执行
            接受一个参数：视图函数作出的响应
            在此函数中可以对响应值在返回之前做最后一步修改处理
            需要将参数中的响应在此参数中进行返回
        teardown_request：
            在每次请求后执行
            接受一个参数：错误信息，如果有相关错误抛出
"""

from flask import Flask

app = Flask(__name__)


# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request")


# 在每一次请求之前调用，这时候已经有请求了，可能在这个方法里面做请求的校验
# 如果请求的校验不成功，可以直接在此方法中进行响应，直接return之后那么就不会执行视图函数
@app.before_request
def before_request():
    print("before_request")
    # if 请求不符合条件:
    #     return "laowang"


# 在执行完视图函数之后会调用，并且会把视图函数所生成的响应传入,可以在此方法中对响应做最后一步统一的处理
@app.after_request
def after_request(response):
    print("after_request")
    response.headers["Content-Type"] = "application/json"
    return response


# 请每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(e):
    print("teardown_request")


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)


"""
结果：
 * Serving Flask app "demo9(请求--响应循环--请求勾子）" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 429-680-233
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
 第一次请求：
127.0.0.1 - - [1/Aug/2018 19:44:13] "GET / HTTP/1.1" 200 -
before_first_request
before_request
after_request
teardown_request

第二次请求：
before_request
after_request
teardown_request
127.0.0.1 - - [1/Aug/2018 19:44:15] "GET / HTTP/1.1" 200 -
"""