class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        new_node=Node(data)
        self.rear.next=new_node
        self.rear=new_node
    def dequeue(self):
        popped_data=self.front
        self.front=self.front.next
        return popped_data
    def display(self):
        current=self.front
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()
queue.dequeue()
queue.dequeue()
queue.display()



        
        

