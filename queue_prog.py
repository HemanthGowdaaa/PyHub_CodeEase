from collections import deque
class queue:
    def __init__(self):
        self.queue = deque()
    
    def enque(self,item):
        self.queue.append(item)
    
    def deque(self):
        if not len(self.queue) == 0:
            self.queue.popleft()
        return "empty queue"
        
    def front(self):
        if not len(self.queue) == 0:
            return self.queue[0]
        return "empty queue"
    
    def size(self):
        return len(self.queue)
        
q1=queue()
q1.enque(10)
q1.enque(20)
q1.enque(30)
q1.enque(40)
print(q1.queue)
print(f"size of queue is {q1.size()}")
q1.deque()
q1.deque()
print(q1.queue)
print(q1.front())
print(f"size of queue is {q1.size()}")