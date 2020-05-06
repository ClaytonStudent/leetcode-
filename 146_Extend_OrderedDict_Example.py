# And introduction to OrderedDict
# https://www.journaldev.com/21807/python-ordereddict#python-ordereddict
# 1. If an item is deleted and added again, then it moves to the last.
# 2. popitem(last=True) FIFO删除第一个， popitem(last=False) LIFO删除第最后一个
# 3. move_to_end(last=True) 移动到最后一个， move_to_end(last=False) 移动到第一个
# 4. reversed()
# 5. tow OrderedDict compare is order_sensitive, other compare is not order_sensitive.

from collections import OrderedDict
my_dict = {'kiwi': 4, 'apple': 5, 'cat': 3}
ordered_dict = OrderedDict(my_dict)
ordered_dict['dot'] = 3
ordered_dict['kiwi'] = 10
ordered_dict.pop('kiwi')
ordered_dict.move_to_end('apple')
ordered_dict.move_to_end('dog', False)
item = ordered_dict.popitem(True)
for item in reversed(ordered_dict):
    print(item)

d1 = {'a': 'A', 'b': 'B'}
d2 = {'b': 'B', 'a': 'A'}

od1 = OrderedDict({'a': 'A', 'b': 'B'})
od2 = OrderedDict({'b': 'B', 'a': 'A'})

print(d1 == d2)
print(od1 == od2)
print(d1 == od1)
