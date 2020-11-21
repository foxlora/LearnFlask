# -*- coding: utf-8 -*-
'''
学习装饰器
'''
__author__ = 'Foxlora'
__time__ = '2020/11/20 21:37'

#时间装饰器
import time
from functools import wraps


def time_calc(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        start_time = time.time()
        f = func(*args,**kwargs)
        exec_time = time.time() - start_time
        print(exec_time)
        return f
    return wrapper


def sub(a, b):
    return a - b

@time_calc
def add(a,b):
    time.sleep(1)
    return a + b


def sub(a, b):
    return a - b

print(add(1,2))

from inspect import *