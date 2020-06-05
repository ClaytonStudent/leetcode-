Python 面试题目

1.将不定量的参数传递给一个函数

*arg 非键值对的可变数量的参数列表

*kwargs 键值对的可变数量的参数列表

2 装饰器：函数可以作为参数传递， 是修改其他函数的功能的函数

3 数据类型： int, bool, str, list, tuple, dict

int, str, tuple 不可变数据类型

list, dict 可变数据类型

__init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数

__new__:创建对象时候执行的方法，单列模式会用到



try..except..else没有捕获到异常，执行else语句

try..except..finally不管是否捕获到异常，都执行finally语句



日志的五个等级：DEBUG INFO WARNING ERROR CRITICAL



迭代器：顾名思义，迭代器就是用于迭代操作（for 循环）的对象，它像列表一样可以迭代获取其中的每一个元素，任何实现了 `__next__` 方法 （python2 是 next）的对象都可以称为迭代器。

生成器：普通函数用 `return` 返回一个值，用关键字 `yield` 来返回值，这种函数叫生成器函数