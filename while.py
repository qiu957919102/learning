#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Bruce
# mail: 957919102@qq.com
# QQ : 957919102
print_num = input('Which loop do you want it to be printed out:')
count = 0
while count < 10000:
    if count == print_num:
        print 'There you got the number:', count
        choice = raw_input('Do you want to continr the loop?(y/n)')
        if choice == 'n':
            break
        else:
            while print_num <= count:
                print_num = input('Which loop do you want it to be printed out:')
                if print_num > count:
                    count + 1
                else:
                    print u"已经过了，傻X"

    else:
        print 'loop:', count
    count +=1
else:
    print 'loop:', count