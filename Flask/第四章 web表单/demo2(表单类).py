#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
"""
使用 Flask_WTF 时，每个 Web 表单都由一个继承自 Form 的类表示。这个类定义表单中的一组字段，每个字段都用对象表示。
字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入值是否符合要求。
示例是一个简单的 Web 表单，包含一个文本字段和一个提交按钮。

示例： 定义表单类
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
class NameForm(Form):
name = StringField('What is your name?', validators=[Required()])  validators=[Required()])
submit = SubmitField('Submit')

这个表单中的字段都定义为类变量，类变量的值是相应字段类型的对象。在这个示例中，NameForm 表单中有一个名为 name
的文本字段和一个名为 submit 的提交按钮。 StringField类表示属性为 type="text" 的 <input> 元素。 SubmitField
类表示属性为 type="submit" 的<input> 元素。字段构造函数的第一个参数是把表单渲染成 HTML 时使用的标号。

StringField 构造函数中的可选参数 validators 指定一个由验证函数组成的列表，在接受用户提交的数据之前验证数据。
验证函数 Required() 确保提交的字段不为空。Form 基类由 Flask_WTF 扩展定义，所以从 flask_wtf 中导入。字段和验
证函数却可以直接从 WTForms 包中导入。

WTForms支持的HTML标准字段
字段类型            说　　明
StringField         文本字段
TextAreaField       多行文本字段
PasswordField       密码文本字段
HiddenField         隐藏文本字段
DateField           文本字段，值为 datetime.date 格式
DateTimeField       文本字段，值为 datetime.datetime 格式
IntegerField        文本字段，值为整数
DecimalField        文本字段，值为 decimal.Decimal
FloatField          文本字段，值为浮点数
BooleanField        复选框，值为 True 和 False
RadioField          一组单选框
SelectField         下拉列表
SelectMultipleField 下拉列表，可选择多个值
FileField           文件上传字段
SubmitField         表单提交按钮
FormField           把表单作为字段嵌入另一个表单
FieldList            一组指定类型的字段


WTForms验证函数
验证函数            说　　明
Email           验证电子邮件地址
EqualTo         比较两个字段的值；常用于要求输入两次密码进行确认的情况
IPAddress       验证 IPv4 网络地址
Length          验证输入字符串的长度
NumberRange     验证输入的值在数字范围内
Optional        无输入值时跳过其他验证函数
Required        确保字段中有数据
Regexp          使用正则表达式验证输入值
URL             验证 URL
AnyOf           确保输入值在可选值列表中
NoneOf          确保输入值不在可选值列表中
"""
