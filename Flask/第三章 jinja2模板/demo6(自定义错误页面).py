#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
像常规路由一样， Flask 允许程序使用基于模板的自定义错误页面。
最常见的错误代码有两个： 404， 客户端请求未知页面或路由时显示； 500，有未处理的异常时显示。

@app.errorhandler(404)
def page_not_found(e):
return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
return render_template('500.html'), 500

templates/base.html 的内容，这是一个继承自 bootstrap/base.html 的新模板，其中定义了导航条。这个模板本身也可作为其
他模板的基模板，例如 templates/user.html、 templates/404.html 和 templates/500.html。
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@app.route('/')
def index():
    return render_template('index.html')
