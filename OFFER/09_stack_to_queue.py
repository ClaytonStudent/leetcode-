class StackToQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,val):
        self.stack1.append(val)
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    

class QueueToStack(object):
    def __init__(self):
        pass