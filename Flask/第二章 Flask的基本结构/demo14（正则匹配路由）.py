#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
在 web 开发中，可能会出现限制用户访问规则的场景，那么这个时候就需要用到正则匹配，根据自己的规则去限定请求参数再进行访问

具体实现步骤为：
    导入转换器基类：在 Flask 中，所有的路由的匹配规则都是使用转换器对象进行记录
    自定义转换器：自定义类继承于转换器基类
    添加转换器到默认的转换器字典中



系统自带转换器
DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}
"""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 1. 自定义转换器，继承BaseConverter
class RegexConverter(BaseConverter):
    # 重写父类的regx属性，将自定义的正则表达式赋值给他
    # 123456
    # regex = "[0-9]{6}"
    def __init__(self, url_map, re):
        # 父类的初始化工作
        super(RegexConverter, self).__init__(url_map)
        # 将外界传入的正则表达式，赋值给regex属性
        self.regex = re


# 2.将自定义好的类，注册到url_map.converters这个字典中
app.url_map.converters["re"] = RegexConverter


@app.route('/')
def hello_world():
    return 'Hello World!'


# 3.使用<re:user_id>
# 127.0.0.1:5000/user/123456 -> "[0-9]{6}" -->demo1
# 127.0.0.1:5000/user/1234 -> "[0-9]{4}" -->demo1
@app.route('/user/<re("[0-9]{6}"):user_id>')
def demo1(user_id):
    return "demo1 %s" % user_id


if __name__ == '__main__':
    app.run(debug=True)
