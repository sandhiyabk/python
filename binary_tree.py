class vertex:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return vertex(key)
    queue=[]
    queue.append(root)
    while queue:
        temp=queue.pop(0)
        if not temp.left:
            temp.left=vertex(key)
            break
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right=vertex(key)
            break
        else:
            queue.append(temp.right)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")
def size(node):
    if node is None:
        return 0
    else:
        si=size(node.left)+size(node.right)+1
        print(si)
root=vertex(1)
root=insert(root,2)
root=insert(root,3)
root=insert(root,4)
size(vertex(4))
print("The inorder is:",inorder(root))
print("The preorder is:",preorder(root))
print("The postorder is:",postorder(root))


    
