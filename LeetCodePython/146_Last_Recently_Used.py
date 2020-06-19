# Question
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
# ----------------------------------------------------------------
# Solution
# Vedio: https://www.youtube.com/watch?v=7v_mUfpg46E&feature=youtu.be
# Double Linked List + hash table(dictionary)
from collections import OrderedDict


class Node:
    def __index__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.D = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        p = node.prev
        p.next = node.next
        node.next.prev = p

    def get(self,key):
        if key not in self.D:
            return -1
        self._remove(self.D[key])
        self._add(self.D[key])
        return self.D[key]

    def put(self, key, value):
        if key in self.D:
            self._remove(self.D[key])
            del self.D[key]
        elif len(self.D) == self.capacity:
            n = self.head.next
            self._remove(n)
            del self.D[n.key]

            n = Node(key,value)
            self.D[key] = value
            self._add(n)


class LRUCache_ordered_dict:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)  # if last = true: move to end, false: move to front
        return val

    def put(self, key, val):
        if key in self.cache:
            del self.cache[key]  # 把之前的记录删掉
        self.cache[key] = val  # 添加新的纪律到最后
        if len(self.cache) > self.size:   # 如果超过capacity
            self.cache.popitem(last=False)  # 删掉头一个   if last = false: FIFO; true: LIFO


