class vertex:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
def insert(root,key):
    if root is None:
        return vertex(key)
    else:
        if key<root.val:
            root.left=insert(root.left,key)
        else:
            root.right=insert(root.right,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
root=vertex(1)
root=insert(root,2)
root=insert(root,3)
root=insert(root,4)
inorder(root)
    
