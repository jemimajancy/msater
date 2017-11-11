#!/usr/bin/python

import sys

def bar(pro, a, b):
        print a
        print b
        print "I am in pro"
        print pro
        return 99

def foo(num):
        print num
        pro = 1
        for i in range(num):
                pro = pro * (i + 1)
                print pro
        c = bar(pro, "hi", 20)
        print c

if __name__=="__main__":
	 num=raw_input("enter the no:")
	 num=int(num)
	 foo(num)

	





