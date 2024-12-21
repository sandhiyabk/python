class Queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return len(self.queue)==0
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
def palindrome(s):
    queue=Queue()
    for char in s:
        queue.enqueue(char)
    while queue.size()>1:
        if queue.dequeue!=queue.queue[-1]:
            return False
        queue.queue.pop()
    return True
s="sir"
if palindrome(s):
    print("The string is palindrome")
else:
    print("The string is not a palindrome")
    
