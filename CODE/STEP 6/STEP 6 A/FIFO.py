from collections import deque

class FIFO:
    
    def __init__(self, size):
        
        self.queue=deque()
        self.size=size
        
    def add(self, element):
        
        self.queue.append(element)
        
        if len(self.queue)>self.size: self.queue.popleft()
            
    def __len__(self):
        return len(self.queue)
    
    def __repr__(self):
        return str(self.queue)
