#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
1.控制结构:
Jinja2 提供了多种控制结构，可用来改变模板的渲染流程。本节使用简单的例子介绍其中最有用的控制结构。
下面这个例子展示了如何在模板中使用条件控制语句：
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}
另一种常见需求是在模板中渲染一组元素。下例展示了如何使用 for 循环实现这一需求：
<ul>
{% for comment in comments %}
<li>{{ comment }}</li>
{% endfor %}
</ul>

2.Jinja2 还支持宏。宏类似于 Python 代码中的函数。例如：
{% macro render_comment(comment) %}
<li>{{ comment }}</li>
{% endmacro %}
<ul>
{% for comment in comments %}
{{ render_comment(comment) }}
{% endfor %}
</ul>

为了重复使用宏，我们可以将其保存在单独的文件中，然后在需要使用的模板中导入：
{% import 'macros.html' as macros %}
<ul>
{% for comment in comments %}
{{ macros.render_comment(comment) }}
{% endfor %}
</ul>
`
3.需要在多处重复使用的模板代码片段可以写入单独的文件，再包含在所有模板中，以避免重复：
{% include 'common.html' %}
4.另一种重复使用代码的强大方式是模板继承，它类似于 Python 代码中的类继承。首先，创建一个名为 base.html 的基模板：
模板 ｜ 23
<html>
<head>
{% block head %}
<title>{% block title %}{% endblock %} - My Application</title>
{% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
block 标签定义的元素可在衍生模板中修改。在本例中，我们定义了名为 head 、 title 和body 的块。
注意， title 包含在 head 中。下面这个示例是基模板的衍生模板：
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
{{ super() }}
<style>
</style>
{% endblock %}
{% block body %}
<h1>Hello, World!</h1>
{% endblock %}

extends 指令声明这个模板衍生自 base.html。在 extends 指令之后，基模板中的 3 个块被重新定义，模板引擎
会将其插入适当的位置。注意新定义的 head 块，在基模板中其内容不是空的，所以使用 super() 获取原来的内容。
"""