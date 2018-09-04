#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
默认情况下， Flask_WTF 能保护所有表单免受跨站请求伪造（ Cross-Site Request Forgery，CSRF）的攻击。
恶意网站把请求发送到被攻击者已登录的其他网站时就会引发 CSRF 攻击。为了实现CSRF保护， Flask_WTF 需要程序设置一个密钥。
Flask_WTF 使用这个密钥生成加密令牌，再用令牌验证请求中表单数据的真伪。

设置 Flask-WTF
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'或SECRET_KEY ="dfsadfkl;sd;fsljdkf;sdk"

app.config 字典可用来存储框架、扩展和程序本身的配置变量。
SECRET_KEY 配置变量是通用密钥，可在 Flask 和多个第三方扩展中使用。
"""


