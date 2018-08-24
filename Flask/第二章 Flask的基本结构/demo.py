#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
from flask import Flask

# 创建flask实例对象
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask"

# 入口函数
if __name__ == '__main__':
    # 启动服务器
    app.run()