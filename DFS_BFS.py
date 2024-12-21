class vertex:
    def __init__(self,value):
        self.value=value
        self.next=[]
def adjacent(v1,v2):
    v1.next.append(v2)
    v2.next.append(v1)
A=vertex("a")
B=vertex("b")
C=vertex("c")
D=vertex("d")
adjacent(A,B)
adjacent(A,C)
adjacent(B,D)
def dfs(v):
    stack=[v]
    visited=set()
    while stack:
        c=stack.pop()
        if c not in visited:
            visited.add(c)
            print(c.value)
            stack.extend(c.next)
print("DFS")
dfs(A)
from collections import deque
def bfs(v):
    queue=deque([v])
    visited=set()
    while queue:
        c=queue.popleft()
        if c not in visited:
            visited.add(c)
            print(c.value)
            queue.extend(c.next)
print("BFS")
dfs(A)
