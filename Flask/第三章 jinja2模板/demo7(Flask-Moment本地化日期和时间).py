#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
如果 Web 程序的用户来自世界各地，那么处理日期和时间可不是一个简单的任务。
服务器需要统一时间单位， 这和用户所在的地理位置无关，所以一般使用协调世界时（ Coordinated Universal Time， UTC）

要想在服务器上只使用 UTC 时间，一个优雅的解决方案是，把时间单位发送给 Web 浏览器，转换成当地时间， 然后渲染。
 Web 浏览器可以更好地完成这一任务，因为它能获取用户电脑中的时区和区域设置。
有一个使用 JavaScript 开发的优秀客户端开源代码库，名为 moment.js（ http://momentjs.com/），它可以在浏览器中渲染日期和时间。
 Flask_Moment 是一个 Flask 程序扩展，能把moment.js 集成到 Jinja2 模板中。

 Flask_Moment安装：
 pip install Flask_Moment

 始化 Flask-Moment
    from flask_moment import Moment
    moment = Moment(app)
除了 moment.js， Flask_Moment 还依赖 jquery.js。要在 HTML 文档的某个地方引入这两个库，可以直接引入，这样可以选择使用
哪个版本，也可使用扩展提供的辅助函数，从内容分发网络（ Content Delivery Network， CDN）中引入通过测试的版本。 Bootstrap
已经引入了 jquery.js， 因此只需引入 moment.js 即可。

templates/base.html：引入 moment.js 库
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}

Flask-Moment 实现了 moment.js 中的 format()、 fromNow()、 fromTime()、 calendar()、 valueOf()和 unix() 方法。
你可查阅文档（ http://momentjs.com/docs/#/displaying/）学习 moment.js 提供的全部格式化选项。
"""
from flask import Flask
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask import render_template
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/user/<name>")
def user(name):
    return render_template("user5.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)


"""
把404和500的base.html改为base1.html
"""