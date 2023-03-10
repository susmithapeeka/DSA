class BSTnode:
  def __init__(self,value):
    self.value=value
    self.leftchild=None
    self.rightchild=None

def insertion(root,newvalue):
  if root.value is None:
    root.value=newvalue
  elif root.value>=newvalue:
    if root.leftchild is None:
      root.leftchild=BSTnode(newvalue)
    else:
      insertion(root.leftchild,newvalue)
  else:
    if root.rightchild is None:
      root.rightchild=BSTnode(newvalue)
    else:
      insertion(root.rightchild,newvalue)

def inorder(root):
  if root is None:
    return 
  inorder(root.leftchild)
  print(root.value)
  inorder(root.rightchild)

BST=BSTnode(None)
insertion(BST,9)
insertion(BST,8)
insertion(BST,11)
inorder(BST)
