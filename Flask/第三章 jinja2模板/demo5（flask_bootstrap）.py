#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
使用Flask-Bootstrap集成Twitter Bootstrap

    1.Bootstrap（http://getbootstrap.com/）是 Twitter 开发的一个开源框架，它提供的用户界面组件可用于创建整洁
且具有吸引力的网页，而且这些网页还能兼容所有现代 Web 浏览器。

    2.Bootstrap 是客户端框架，因此不会直接涉及服务器。服务器需要做的只是提供引用了Bootstrap 层 叠 样 式 表（CSS）
和 JavaScript 文 件 的 HTML 响 应， 并 在 HTML、CSS 和JavaScript 代码中实例化所需组件。这些操作最理想的执行场所就是模板。

   3. 要想在程序中集成 Bootstrap，显然要对模板做所有必要的改动。不过，更简单的方法是使用一个名为 Flask-Bootstrap 的 Flask
扩展，简化集成的过程。Flask-Bootstrap 使用 pip

    4.安装：
    pip install flask-bootstrap

    5.初始化 Flask-Bootstrap
    from flask_bootstrap import Bootstrap
    # ...
    bootstrap = Bootstrap(app)

    初始化 Flask-Bootstrap 之后，就可以在程序中使用一个包含所有 Bootstrap 文件的基模板。这个模板利用 Jinja2
的模板继承机制，让程序扩展一个具有基本页面结构的基模板，其中就有用来引入 Bootstrap 的元素。示例 3-5 是把 user.html
改写为衍生模板后的新版本。

示例 3-5　templates/user.html：使用 Flask-Bootstrap 的模板
{% extends "bootstrap/base.html" %}

{% block title %}Flasky{% endblock %}

{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
                data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}

{% block content %}
<div class="container">
    <div class="page-header">
        <h1>Hello, {{ name }}!</h1>
    </div>
</div>
{% endblock %}

    Jinja2 中的 extends 指令从 Flask_Bootstrap 中导入 bootstrap/base.html，从而实现模板继承。Flask_Bootstrap 中
的基模板提供了一个网页框架，引入了 Bootstrap 中的所有 CSS 和模板JavaScript 文件。
    基模板中定义了可在衍生模板中重定义的块。 block 和 endblock 指令定义的块中的内容可添加到基模板中。上面这个 user.html
模板定义了 3 个块，分别名为 title 、 navbar 和 content 。这些块都是基模板提供的，可在衍生模板中重新定义。 title 块的作用
很明显，其中的内容会出现在渲染后的 HTML 文档头部，放在 <title> 标签中。 navbar 和 content 这两个块分别表示页面中的导航条和主体内容。

    在这个模板中， navbar 块使用 Bootstrap 组件定义了一个简单的导航条。 content 块中有个<div> 容器，其中包含一个页面头部。
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("index5.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user5.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)
