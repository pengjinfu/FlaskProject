#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
"""
一、基本概念
1.Flask 是一个小型框架，或者说是微型框架。
2.Flask 自开发伊始就被设计为可扩展的框架，它具有一个包含基本服务的强健核心， 其他功能则可通过扩展实现。
3.Flask 有两个主要依赖：路由、调试和 Web 服务器网关接口（ Web Server Gateway Interface，WSGI）子系统由 Werkzeug（ http://werkzeug.pocoo.org/）提供；模板系统由 Jinja2（ http://jinja.pocoo.org/）提供。 Werkzeug 和 Jinjia2 都是由 Flask 的核心开发者开发而成。
4.Flask 并不支持很多原生功能，要使用具体的某些功能就必须使用扩展。


二、安装
windows下：
pip install flask
Ubuntu下：
sudo pip install flask
指定装哪个版本：sudo pip install flask==0.10.1

若在同一个包下：使用不同版本开发，会造成版本问题。
解决办法：安装虚拟环境
sudo pip install virtualenv
sudo pip install virtualenvwrapper

# 1、创建目录用来存放虚拟环境
mkdir $HOME/.virtualenvs

# 2、打开~/.bashrc文件，并添加如下：
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

# 3、运行
source ~/.bashrc

提示：如果不指定python版本，默认安装的是python2的虚拟环境
在python2中，创建虚拟环境

mkvirtualenv 虚拟环境名称
例 ：
mkvirtualenv py_flask
在python3中，创建虚拟环境

mkvirtualenv -p python3 虚拟环境名称
例 ：
mkvirtualenv -p python3 py3_flask

提示 :
创建虚拟环境需要联网
创建成功后, 会自动工作在这个虚拟环境上
工作在虚拟环境上, 提示符最前面会出现 “虚拟环境名称”


如何使用虚拟环境?
查看虚拟环境的命令 :
workon 两次tab键


使用虚拟环境的命令 :
workon 虚拟环境名称

例 ：使用python2的虚拟环境
workon py_flask

例 ：使用python3的虚拟环境
workon py3_flask


退出虚拟环境的命令 :
deactivate


删除虚拟环境的命令 :
rmvirtualenv 虚拟环境名称

例 ：删除虚拟环境py3_flask

先退出：deactivate
再删除：rmvirtualenv py3_flask

如何在虚拟环境中安装工具包?
提示 : 工具包安装的位置 :
python2版本下：
~/.virtualenvs/py_flask/lib/python2.7/site-packages/
python3版本下：
~/.virtualenvs/py3_flask/lib/python3.5/site-packages
python3版本下安装flask-0.10.1的包 :

pip install 包名称
例 : 安装flask-0.10.1的包
pip install flask==0.10.1

查看虚拟环境中安装的包 :
pip freeze

注：选择了哪个版本环境后，就可以在这个环境下创建对应版本的python文件。

三、Flask常用扩展包
Flask常用扩展包：
    Flask-SQLalchemy：操作数据库；
    Flask-script：插入脚本；
    Flask-migrate：管理迁移数据库；
    Flask-Session：Session存储方式指定；
    Flask-WTF：表单；
    Flask-Mail：邮件；
    Flask-Bable：提供国际化和本地化支持，翻译；
    Flask-Login：认证用户状态；
    Flask-OpenID：认证；
    Flask-RESTful：开发REST API的工具；
    Flask-Bootstrap：集成前端Twitter Bootstrap框架；
    Flask-Moment：本地化日期和时间；
    Flask-Admin：简单而可扩展的管理接口的框架

"""

# 导入flask包
import flask  # 没有报错，说明是成功的，在这里，由于我指定是在哪个环境，故我安装的是哪个版本，就是在哪个flask环境下。