#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
1.Flask 的开发 Web 服务器支持很多启动设置选项，但只能在脚本中作为参数传给 app.run()函数。这种方式并不十分方便，传递设置选项的
理想方式是使用命令行参数。
2.Flask-Script 是一个 Flask 扩展，为 Flask 程序添加了一个命令行解析器。 Flask-Script 自带了一组常用选项，而且还支持自定义命令。
3.安装：pip install flask-script
4.python hello.py runserver --help来查看参数

步骤：
# 1.导入管理类
# 2.创建管理类
# 3.使用管理类开启我们的flask项目
"""
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    manager.run()


'''
python demo16(扩展Flask-Script).py runserver -h 127.0.0.1 -p 8888 -d
python 项目名称   -h ip地址 -p 端口号 -d开启debug模式
'''