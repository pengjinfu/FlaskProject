#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.2
"""
创建模板的流程：
1.创建flask文件
2.创建一个templates文件夹，并标记为jinja2模式，里面存放的都是模板文件,并创建一个demo2.html文件
3.通过模板对内容进行渲染
"""
from flask import Flask,render_template

app = Flask(__name__)

# 创建视图函数，将该模板内容进行渲染返回
@app.route("/")
def index():
    name = "我是一个变量"
    return render_template("demo2.html",name=name)


if __name__ == '__main__':
    app.run(debug=True)

