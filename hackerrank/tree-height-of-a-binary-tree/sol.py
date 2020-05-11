'''
class Node:
      def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return max(
        height(root.left) + 1,
        height(root.right) + 1,
    )
