#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/demo1')
def demo1():
    # 重定向到百度官网
    # 参数1：需要重定向的网页地址即可
    return redirect("http://www.baidu.com")


@app.route('/demo2')
def demo2():
    # 重定向自己的界面
    # 参数1：需要重定向的网页地址即可
    # url_for反向解析函数
    # 作用：url_for(函数名称) 根据函数名称获取到这个视图函数对应的url
    return redirect(url_for("demo1"))


if __name__ == '__main__':
    app.run(debug=True)
