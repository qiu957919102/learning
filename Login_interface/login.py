#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Bruce
# mail: 957919102@qq.com
# QQ : 957919102

import getpass
logintimes = 0
while logintimes < 3:
    name = raw_input("Please input your username:")
    pwd = getpass.getpass("Please input your password:")
    if name == 'Bruce' and pwd == '123456':
        print "welcome,login succeed!"
        break
    else:
        print "Error,login again:"
        logintimes += 1
else:
    print "sorry,account has been locked!"

