#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.1
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    # 1.定义字典
    dict = {
        "name": "james",
        "age": 33,
        "info": {
            "team": "laker"
        }
    }
    # 2.将python字典对象转换成json字符串
    json_str = json.dumps(dict)
    # 3.将json字符串转成python字典对象
    my_dict = json.loads(json_str)

    # 4.使用flask自带的jsonify这个模块将字典转换成json字符串
    # 4.1.能够将python字典对象转换成json字符串
    # 4.2.能够帮助我们指明返回数据的类型： contentType: application/json
    # 4.3.将数据包装成response响应对象
    json_str1 = jsonify(dict)
    return json_str1


if __name__ == '__main__':
    app.run(debug=True)