# decorators
# introduce: https://jackpopc.github.io/2019/08/10/1-decorators/
# 什么是Python装饰器？
# 顾名思义，从字面意思就可以理解，它是用来"装饰"Python的工具，使得代码更具有Python简洁的风格。
# 换句话说，它是一种函数的函数，因为装饰器传入的参数就是一个函数，然后通过实现各种功能来对这个函数的功能进行增强。
from time import time, sleep

def run_time(func):
    def wrapper():
        start = time()
        func()                  # 函数在这里运行
        end = time()
        cost_time = end - start
        print("func three run time {}".format(cost_time))
    return wrapper

@run_time
def fun_one():
    sleep(1)
    
@run_time
def fun_two():
    sleep(2)
    
@run_time
def fun_three():
    sleep(3)

fun_one()
fun_two()
fun_three()