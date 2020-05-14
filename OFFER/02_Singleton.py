# introduce: https://jackpopc.github.io/2019/10/19/singleton/
# Code: https://github.com/JushuangQiao/Python-Offer/tree/master/second/second#%E9%9D%A2%E8%AF%95%E9%A2%982-%E4%BD%BF%E7%94%A8Python%E5%AE%9E%E7%8E%B0%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F
from functools import wraps


def single_ton(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return single


@single_ton
class SingleTon(object):
    val = 123

    def __init__(self, a):
        self.a = a

if __name__ == '__main__':
    s = SingleTon(1)
    t = SingleTon(2)
    print(s is t)
    print(s.a, t.a)
    print(s.val, t.val)