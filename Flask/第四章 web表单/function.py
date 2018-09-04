#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
第二章中介绍的请求对象包含客户端发出的所有请求信息。其中， request.form 能获取POST 请求中提交的表单数据。
尽管 Flask 的请求对象提供的信息足够用于处理 Web 表单，但有些任务很单调，而且要重复操作。比如，生成表单的 HTML
代码和验证提交的表单数据。
Flask_WTF（ http://pythonhosted.org/Flask-WTF/） 扩展可以把处理 Web 表单的过程变成一种愉悦的体验。 这个扩展对独立的
WTForms（ http://wtforms.simplecodes.com）包进行了包装，方便集成到 Flask 程序中。

Flask_WTF 及其依赖可使用 pip 安装：
pip install flask-wtf
"""