#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
表单字段是可调用的，在模板中调用后会渲染成 HTML。假设视图函数把一个 NameForm 实例通过参数 form 传入模板，
在模板中可以生成一个简单的表单，如下所示：
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name() }}
    {{ form.submit() }}
</form>


要想改进表单的外观，可以把参数传入渲染字段的函数，传入的参数会被转换成字段的 HTML 属性。例如，可以为字段指定
id 或 class 属性，然后定义 CSS 样式：
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name(id='my_tex_field') }}
    {{ form.submit() }}
</form>

即便能指定 HTML 属性，但按照这种方式渲染表单的工作量还是很大，所以在条件允许的情况下最好能使用 Bootstrap 中的表单样式。
 Flask_Bootstrap 提供了一个非常高端的辅助函数，可以使用 Bootstrap 中预先定义好的表单样式渲染整个 Flask_WTF 表单，
 而这些操作只需一次调用即可完成。使用 Flask_Bootstrap，上述表单可使用下面的方式渲染：
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}

import 指令的使用方法和普通 Python 代码一样，允许导入模板中的元素并用在多个模板中。导入的 bootstrap/wtf.html 文件中定义
了一个使用 Bootstrap 渲染 Falsk_WTF 表单对象的辅助函数。 wtf.quick_form() 函数的参数为 Flask_WTF 表单对象，使用
 Bootstrap 的默认样式渲染传入的表单。

使用 Flask-WTF 和 Flask-Bootstrap 渲染表单
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}Flasky{% endblock %}
{% block page_content %}
<div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}
{% endblock %}

模板的内容区现在有两部分。第一部分是页面头部，显示欢迎消息。这里用到了一个模板条件语句。 Jinja2 中的条件语句格式为
{% if condition %}...{% else %}...{% endif %}。
如果条件的计算结果为 True，那么渲染 if 和 else 指令之间的值。如果条件的计算结果为
False，则渲染 else 和 endif 指令之间的值。在这个例子中，如果没有定义模板变量 name，
则会渲染字符串“ Hello, Stranger!”。内容区的第二部分使用 wtf.quick_form() 函数渲染
NameForm 对象。
"""