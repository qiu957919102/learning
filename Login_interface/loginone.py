#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Bruce
# mail: 957919102@qq.com
# QQ : 957919102

for i in range(3):
    name = raw_input("请输入用户名：")
    pwd = raw_input("请输入密码：")
    if name == "Bruce" and pwd == "123456":
        print "登录成功，欢迎！"
        break
    else:
        print "用户信息错误，请重新输入！"
else:
    print "很抱歉，用户已被锁定！"