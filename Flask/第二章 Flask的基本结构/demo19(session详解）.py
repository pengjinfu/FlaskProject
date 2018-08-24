#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
实现状态保持主要有两种方式：
    在客户端存储信息使用Cookie
    在服务器端存储信息使用Session
Session
    对于敏感、重要的信息，建议要存储在服务器端，不能存储在浏览器中，如用户名、余额、等级、验证码等信息.
    在服务器端进行状态保持的方案就是Session.
    Session依赖于Cookie.
"""
from flask import Flask, session

app = Flask(__name__)

# 加密字符串：flask会根据这个字符串给里面的数据进行混淆加密（不需要我们关心）
app.secret_key ="1234878dssdjfsadkfsd65"
# app.config['SECRET_KEY']="1234878dssdjfsadkfsd65"
@app.route("/")
def hello():
    return "Hello World"


# 登录成功的时候，在服务器使用session保存用户数据
@app.route('/lgoin')
def lgoin():
    """使用session"""
    session["user_id"]="66"
    session["user_name"]="curry"
    return "lgoin success"

# 当胸访问首页的时候，我们可以通过session字典获取里面的值
@app.route('/index')
def index():
    """用过session获取值"""
    user_id = session.get("user_id","")
    user_name = session.get("user_name","")
    return "index %s--%s"%(user_id,user_name)

# 当你退出登录的时候，通过session.pop(key)删除数据
@app.route("/lgoin_out")
def lgoin_out():
    session.pop("user_id")
    session.pop("user_name")
    return "lgoin out"


if __name__ == '__main__':
    app.run(debug=True)