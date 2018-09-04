#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
视图函数 index() 不仅要渲染表单，还要接收表单中的数据。

路由方法
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

app.route 修饰器中添加的 methods 参数告诉 Flask 在 URL 映射中把这个视图函数注册为GET 和 POST 请求的处理程序。
如果没指定 methods 参数，就只把视图函数注册为 GET 请求的处理程序。

把 POST 加入方法列表很有必要，因为将提交表单作为 POST 请求进行处理更加便利。表单也可作为 GET 请求提交，不过 GET
请求没有主体，提交的数据以查询字符串的形式附加到URL 中， 可在浏览器的地址栏中看到。基于这个以及其他多个原因，提交表单
大都作为POST 请求进行处理。

局部变量 name 用来存放表单中输入的有效名字，如果没有输入，其值为 None。如上述代码所示，在视图函数中创建一个 NameForm
 类实例用于表示表单。提交表单后，如果数据能被所有验证函数接受， 那么 validate_on_submit() 方法的返回值为 True，否则返回
 False。这个函数的返回值决定是重新渲染表单还是处理表单提交的数据。

用户第一次访问程序时， 服务器会收到一个没有表单数据的 GET 请求，所以 validate_on_submit() 将返回 False。 if 语句的内容将
被跳过，通过渲染模板处理请求，并传入表单对象和值为 None 的 name 变量作为参数。用户会看到浏览器中显示了一个表单。

用户提交表单后， 服务器收到一个包含数据的 POST 请求。 validate_on_submit() 会调用name 字段上附属的 Required() 验证函数。
如果名字不为空，就能通过验证， validate_on_submit() 返回 True。现在，用户输入的名字可通过字段的 data 属性获取。在 if 语句
中，把名字赋值给局部变量 name，然后再把 data 属性设为空字符串，从而清空表单字段。最后一行调用 render_template() 函数渲染
模板，但这一次参数 name 的值为表单中输入的名字，因此会显示一个针对该用户的欢迎消息。
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)
