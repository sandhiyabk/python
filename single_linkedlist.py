class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinked:
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head is None
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def delete(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
linked=singlelinked()
linked.insert(10)
linked.insert(20)
linked.insert(30)
linked.display()
linked.delete(10)
linked.display()

