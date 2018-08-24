#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1

# 通过rnder_template方法去加载模板
# 参数1：模板文件 参数2：需要传入的参数 key = valiue
from flask import Flask, render_template

app = Flask(__name__)

# Flask 在程序文件夹中的 templates 子文件夹中寻找模板
# 模板保存在 templates 文件夹中，并分别命名为 index.html 和 user.html。
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

"""
1.Flask 提供的 render_template 函数把 Jinja2 模板引擎集成到了程序中。 render_template 函数的第一个参数是
模板的文件名。 随后的参数都是键值对，表示模板中变量对应的真实值。在这段代码中，第二个模板收到一个名为 name 的变量。

2.前例中的 name=name 是关键字参数，这类关键字参数很常见，但如果你不熟悉它们的话，可能会觉得迷惑且难以理解。 
左边的“ name”表示参数名，就是模板中使用的占位符；右边的“ name”是当前作用域中的变量，表示同名参数的值。
"""
