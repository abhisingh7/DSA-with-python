from collections import deque
	# TC - append() → O(1)
	# TC - popleft() → O(1)

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, val):
        self.queue.append(val)   # O(1)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()  # O(1)
    
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    
    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)      # enqueue → [1]
q.enqueue(2)      # enqueue → [1, 2]
print(q.dequeue())      # dequeue → returns 1, queue: [2]