#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
这部分虽然在第二章讲过，但在这里再进一步说明：

最新版的 demo4.py 存在一个可用性问题。用户输入名字后提交表单，然后点击浏览器的刷新按钮，会看到一个莫名其妙的警告，
要求在再次提交表单之前进行确认。之所以出现这种情况，是因为刷新页面时浏览器会重新发送之前已经发送过的最后一个请求。
如果这个请求是一个包含表单数据的 POST 请求，刷新页面后会再次提交表单。大多数情况下，这并不是理想的处理方式。
很多用户都不理解浏览器发出的这个警告。 基于这个原因，最好别让 Web 程序把 POST 请求作为浏览器发送的最后一个请求.

很多用户都不理解浏览器发出的这个警告。 基于这个原因，最好别让 Web 程序把 POST 请求作为浏览器发送的最后一个请求。
这种需求的实现方式是， 使用重定向作为 POST 请求的响应，而不是使用常规响应。重定向是一种特殊的响应， 响应内容是 URL，
而不是包含 HTML 代码的字符串。浏览器收到这种响应时， 会向重定向的 URL 发起 GET 请求，显示页面的内容。这个页面的加载可能
要多花几微秒， 因为要先把第二个请求发给服务器。除此之外，用户不会察觉到有什么不同。现在，最后一个请求是 GET 请求，
所以刷新命令能像预期的那样正常使用了。这个技巧称为 Post/ 重定向 /Get 模式。但这种方法会带来另一个问题。 程序处理 POST
 请求时，使用 form.name.data 获取用户输入的名字，可是一旦这个请求结束，数据也就丢失了。因为这个 POST 请求使用重定向处
理，所以程序需要保存输入的名字， 这样重定向后的请求才能获得并使用这个名字，从而构建真正的响应。

程序可以把数据存储在用户会话中，在请求之间“ 记住”数据。用户会话是一种私有存储，存在于每个连接到服务器的客户端中。
 我们在第二章介绍过用户会话，它是请求上下文中的变量，名为 session，像标准的 Python 字典一样操作。

 默认情况下，用户会话保存在客户端 cookie 中，使用设置的 SECRET_KEY 进行加密签名。 如果篡改了 cookie 中的内容，签名就会
 失效，会话也会随之失效。

 重定向和用户会话
from flask import Flask, render_template, session, redirect, url_for
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

在程序的前一个版本中，局部变量 name 被用于存储用户在表单中输入的名字。这个变量现在保存在用户会话中，
即 session['name']，所以在两次请求之间也能记住输入的值。
现在，包含合法表单数据的请求最后会调用 redirect() 函数。 redirect() 是个辅助函数，用来生成 HTTP 重定向响应。
redirect() 函数的参数是重定向的 URL，这里使用的重定向URL 是程序的根地址， 因此重定向响应本可以写得更简单一些，
写成 redirect('/')，但却会使用 Flask 提供的 URL 生成函数 url_for()。推荐使用 url_for() 生成 URL，因为这个函
数使用 URL 映射生成 URL，从而保证 URL 和定义的路由兼容，而且修改路由名字后依然可用。

url_for() 函数的第一个且唯一必须指定的参数是端点名，即路由的内部名字。 默认情况下，路由的端点是相应视图函数的名字。
在这个示例中，处理根地址的视图函数是index()，因此传给 url_for() 函数的名字是 index。

最后一处改动位于 render_function() 函数中，使用 session.get('name') 直接从会话中读取 name 参数的值。和普通的字典一样，
这里使用 get() 获取字典中键对应的值以避免未找到键的异常情况，因为对于不存在的键， get() 会返回默认值 None。
"""
from flask import Flask, render_template, session, redirect, url_for
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
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

if __name__ == '__main__':
    app.run(debug=True)