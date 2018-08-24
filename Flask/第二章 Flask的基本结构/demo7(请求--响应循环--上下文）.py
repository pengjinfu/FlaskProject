#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
1.程序和请求上下文:相当于一个容器，保存了 Flask 程序运行过程中的一些信息。
    为了避免大量可有可无的参数把视图函数弄得一团糟， Flask 使用上下文临时把某些对象变为全局可访问。
2.在 Flask 中有两种上下文： 程序上下文和请求上下文

3.Flask上下文全局变量
变量名             上下文         说　　明
current_app     程序上下文       当前激活程序的程序实例
g               程序上下文       处理请求时用作临时存储的对象。每次请求都会重设这个变量
request         请求上下文       请求对象，封装了客户端发出的 HTTP 请求中的内容
session         请求上下文       用户会话，用于存储请求之间需要“记住”的值的词典

Flask 在分发请求之前激活（或推送）程序和请求上下文，请求处理完成后再将其删除。程序上下文被推送后， 就可以在线程中使用 current_app 和 g 变量。类似地，请求上下文被推送后，就可以使用 request 和 session 变量。如果使用这些变量时我们没有激活程序上下文或请求上下文， 就会导致错误。

请求上下文：保存了客户端和服务器交互的数据
程序上下文：flask 应用程序运行过程中，保存的一些配置信息，比如程序名、数据库连接、应用信息等

例：
# >>> from hello import app
# >>> from flask import current_app
# >>> current_app.name
# Traceback (most recent call last):
# ...
# RuntimeError: working outside of application context
# >>> app_ctx = app.app_context()
# >>> app_ctx.push()
# >>> current_app.name
# 'hello'
# >>> app_ctx.pop()

没激活程序上下文之前就调用 current_app.name 会导致错误，但推送完上
下文之后就可以调用了。 注意，在程序实例上调用 app.app_context() 可获得一个程序上
下文
"""
# 导入flask库中的Flask中的类
from demo import app
from flask import current_app
# current_app.name
"""
demo是用于验证demo7的：在以下程序之前运行会出现如下结果
结果：
 raise RuntimeError(_app_ctx_err_msg)
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
to interface with the current application object in some way. To solve
this, set up an application context with app.app_context().  See the
documentation for more information.

"""
app_ctx = app.app_context()
app_ctx.push()
current_app.name

"""
没激活程序上下文之前就调用 current_app.name 会导致错误，但推送完上下文之后就可以调用了。 注意，在程序实例上调用 app.app_context() 可获得一个程序上下文。
"""
# 入口函数
if __name__ == '__main__':
    # 启动服务器
    app.run()


"""
如果此行程序from demo import app会报错，是因为路径问题，你把第二章单独打开再运行是不会报错的，这是Python的基础，
就不多说了，由于在Pycharm中用整个flask打开，路径会自动更改。
"""
# 升级程序：
# from flask import Flask, session, request, current_app
#
# app = Flask(__name__)
#
# app.secret_key ="fdasl;dfsadbfsd;123"
# # 在外部使用 请求上下文
# # RuntimeError: Working outside of request context. 超出了请求的上下文的范围
# # print(request)
# # print(session)
#
#  # 在外部使用 应用上下文
# # RuntimeError: Working outside of request context. 超出了请求的上下文的
# # print(current_app)
#
# @app.route("/")
# def hello():
#     # 只有在视图函数中才能去使用上下文，request session
#     # 使用请求上下文
#     print(request.url)
#     print(request.method)
#     session["name"]="harden"
#     print(session["name"])
#
#     # 应用上下文
#     print(current_app.config["DEBUG"])
#     # g对象：存储这次请求过来的临时变量
#     # g.key = value
#     return "Hello World"
#
#
#
# if __name__ == '__main__':
#     app.run(host="0.0.0.0",port=5000,debug=True)