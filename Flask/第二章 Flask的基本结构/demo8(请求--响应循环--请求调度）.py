#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
请求调度：由于映射关系。即我们请求服务器时是如何访问路径的。
    程序收到客户端发来的请求时，要找到处理该请求的视图函数。为了完成这个任务， Flask会在程序的 URL 映射中查找请求的 URL。 URL 映射是 URL 和视图函数之间的对应关系。

    Flask 使用 app.route 修饰器或者非修饰器形式的 app.add_url_rule() 生成映射。要想查看 Flask 程序中的 URL 映射是什么样子，我们可以在 Python 终端生成的映射。
"""
from flask import Flask

# 创建flask实例对象
app = Flask(__name__)


# 视图函数
@app.route('/')
def hello_world():
    print(app.url_map)
    return 'Hello World!'


# 函数入口
if __name__ == '__main__':
    # 启动服务器
    app.run()


"""
1.当我们用浏览器去访问：127.0.0.1：5000 时
2.控制台显示：
 * Serving Flask app "demo8(请求--响应循环--请求调度）" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
#  这个就请求调度，即路由映射关系
Map([<Rule '/' (OPTIONS, GET, HEAD) -> hello_world>,
 <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])
 
127.0.0.1 - - [1/Aug/2018 19:32:35] "GET / HTTP/1.1" 200 -
"""
"""
URL 映射中的 HEAD、 Options、 GET 是请求方法，由路由进行处理。 Flask 为每个路由都指定了请求方法， 
这样不同的请求方法发送到相同的 URL 上时，会使用不同的视图函数进行处理。 HEAD 和 OPTIONS 方法由 Flask 
自动处理，因此可以这么说，在这个程序中， URL映射中的路由都使用 GET 方法。
"""
