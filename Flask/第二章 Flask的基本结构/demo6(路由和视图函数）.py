#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
1.什么是路由？
    客户端（例如 Web 浏览器）把请求发送给 Web 服务器， Web 服务器再把请求发送给 Flask 程序实例。程序实例需要知道对每个URL请求运行哪些代码，所以保存了一个 URL 到Python 函数的映射关系。处理 URL 和函数之间关系的程序称为路由。

    在 Flask 程序中定义路由的最简便方式，是使用程序实例提供的 app.route 修饰器，把修饰的函数注册为路由。下面的例子说明了如何使用这个修饰器声明路由：

    @app.route('/')
    def index():
    return '<h1>Hello World!</h1>'

    修饰器是 Python 语言的标准特性，可以使用不同的方式修改函数的行为。惯常用法是使用修饰器把函数注册为事件的处理程序。

    前例把 index() 函数注册为程序根地址的处理程序。如果部署程序的服务器域名为www.example.com，在浏览器中访问http://www.example.com后，会触发服务器执行 index() 函数。这个函数的返回值称为响应，是客户端接收到的内容。如果客户端是 Web 浏览器，响应就是显示给用户查看的文档。

@app.route('/')   静态的根路由
@app.route('/user/<name>')   动态的路由，尖括号中的内容就是动态部分。
路由中的动态部分默认使用字符串，不过也可使用类型定义。例如，路由 /user/<int:id>只会匹配动态片段 id 为整数的 URL。 Flask 支持在路由中使用 int、 float 和 path 类型。path 类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。


2.视图
    像 index() 这样的函数称为视图函数（ view function）。视图函数返回的响应可以是包含HTML 的简单字符串，也可以是复杂的表单。

    在 Python 代码中嵌入响应字符串会导致代码难以维护，此处这么做只是为了介绍响应的概念。后续将会讲解生成响应的正确方法。
"""
# 导入flask库中的Flask中的类
from flask import Flask

# 创建flask实例对象
app = Flask(__name__)


# 静态路由：用装饰器函数
@app.route('/')
# 视图函数：index函数
def index1():
    return "我是静态路由"


# 动态路由：用装饰器函数
@app.route('/user/<name>')
# 视图函数：index函数
def index(name):
    return "我是动态路由%s" % name


# 路由传递参数：int型
@app.route('/user/<int:user_id>')
def user_info(user_id):
    return 'hello %d' % user_id


# 入口函数
if __name__ == '__main__':
    # 启动服务器
    app.run()

"""
注：
1.静态路由：127.0.0.1：5000 就可以访问
2.动态由于：127.0.0.1：5000/user/name  在动态路由中，函数要记得传参，且返回值中记得格式化字符
3.路由中的参数还可以设置其类型：int、 float 和 path 类型
"""
