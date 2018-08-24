#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
实现状态保持主要有两种方式：
    在客户端存储信息使用Cookie
    在服务器端存储信息使用Session

Cookie：指某些网站为了辨别用户身份、进行会话跟踪而储存在用户本地的数据（通常经过加密）。
    复数形式Cookies。
    Cookie最早是网景公司的前雇员Lou Montulli在1993年3月的发明。
    Cookie是由服务器端生成，发送给客户端浏览器，浏览器会将Cookie的key/value保存，下次请求同一网站时就发送该Cookie给服务器（前提是浏览器设置为启用cookie）。
    Cookie的key/value可以由服务器端自己定义。

应用：
    最典型的应用是判定注册用户是否已经登录网站，用户可能会得到提示，是否在下一次进入此网站时保留用户信息以便简化登录手续，这些都是Cookie的功用。
    网站的广告推送，经常遇到访问某个网站时，会弹出小窗口，展示我们曾经在购物网站上看过的商品信息。
    购物车，用户可能会在一段时间内在同一家网站的不同页面中选择不同的商品，这些信息都会写入Cookie，以便在最后付款时提取信息。

提示：
    Cookie是存储在浏览器中的一段纯文本信息，建议不要存储敏感信息如密码，因为电脑上的浏览器可能被其它人使用
    Cookie基于域名安全，不同域名的Cookie是不能互相访问的
"""
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


# 当你登录成功，借助response对象设置cookie
@app.route('/lgoin')
def lgoin():
    # 将返回的字符串信息，使用make_response函数包装成响应对象
    response = make_response("lgoin success")
    # 通过response对象中的set_cookie方法设置cookie
    # 参数1：key  参数2：value  参数3：过期时长 格式：maxage=xx秒
    response.set_cookie("user_id", "1", max_age=3600)
    response.set_cookie("user_name", "laowang", max_age=3600)

    # 最终将cookie带回给浏览保存
    return response


# 再次进入首页的时候，能够根据根据request请求对象提取cookie
@app.route('/index')
def index():
    """通过request.cookies属性提取cookie值"""
    user_id = request.cookies.get("user_id", "")
    user_name = request.cookies.get("user_name", "")
    return "index %s %s" % (user_id, user_name)


# 退出登录，见风删除cookie
@app.route('/lgoin_out')
def lgoin_out():
    """通过response对象删除cookie"""
    # 通过代码的方式删除cookie只是将内容清除，立马过期
    # 1.构建响应对象
    response = make_response("lgoin_out success")
    # 2.删除cookie
    response.delete_cookie("user_id")
    response.delete_cookie("user_name")

    return response


if __name__ == '__main__':
    app.run(debug=True)
