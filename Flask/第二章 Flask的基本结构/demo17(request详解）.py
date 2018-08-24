#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
request:
request 就是flask中代表当前请求的 request 对象，其中一个请求上下文变量(理解成全局变量，在视图函数中直接使用可以取到当前本次请求)

常用的属性如下：
属性	                   说明	                     类型
data	       记录请求的数据，并转换为字符串	     *
form（重点）	   记录请求中的表单数据	           MultiDict
args(重点）	   记录请求中的查询参数	           MultiDict
cookies	       记录请求中的cookie信息	       Dict
headers	       记录请求中的报文头	               EnvironHeaders
method	       记录请求使用的HTTP方法	           GET/POST
url	           记录请求的URL地址	               string
files（掌握）   记录请求上传的文件    	           *
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


# 提取get请求后面携带的参数  request.args.get("key", "")
# http://127.0.0.1:5000/get?name=laowang&age=18
@app.route('/get')
def demo1():
    """提取get请求携带的参数"""
    # request.methods返回请求方式的字符串是大写的
    if request.method == "GET":
        name = request.args.get("name", "")
        age = request.args.get("age", "")
        return "%s--%s" % (name, age)
    else:
        return "请求方式错误 405"


# 提取post请求后面携带的参数  request.form.get("key", "")
# http:127.0.0.1:5000/post?name=laowang&age=18
@app.route('/post', methods=['POST'])
def demo2():
    """提取get请求携带的参数"""
    # request.methods返回请求方式的字符串是大写的
    if request.method == "POST":
        name = request.form.get("name", "")
        age = request.form.get("age", "")
        return "%s--%s" % (name, age)
    else:
        return "请求方式错误 405"


# 上传一张图片数据给后端，后台提取图片数据，并保存起来（本地）
# http://127.0.0.1：5000/upload
@app.route('/upload', methods=['POST'])
def demo3():
    """上传图片"""
    if request.method == "POST":
        # 1.使用request.files属性，提取图片数据
        img = request.files.get('img')
        # 2.保存图片到本场（并且修改其名字为：1.png)
        img.save("./1.png")
        return "upload success"
    else:
        return "请求方式错误 405"


if __name__ == '__main__':
    app.run(debug=True)
