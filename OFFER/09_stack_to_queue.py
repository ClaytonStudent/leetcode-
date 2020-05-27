# 两个栈实现队列：第一个当作push，第二个当作pop，在pop的时候，如果有则直接出pop，没有则把第一个的全倒进去在pop，如果都为空，返回-1
class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack1.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if self.stack2:    
            return self.stack2.pop()
        else:
            return -1