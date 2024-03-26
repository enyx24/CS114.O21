import heapq, io, os, bisect
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline



#https://www.geeksforgeeks.org/tree-sort/
class Node: 
  
  def __init__(self,item = 0): 
    self.key = item 
    self.left,self.right = None,None

# Root of BST 
root = Node() 
root = None

# This method mainly 
# calls insertRec() 
def insert(key): 
    global root 
    root = insertRec(root, key) 
  
# A recursive function to  
# insert a new key in BST 
def insertRec(root, key): 
  
  # If the tree is empty, 
  # return a new node 
  
    if (root == None): 
        root = Node(key) 
        return root 
  
  # Otherwise, recur 
  # down the tree  
    if (key < root.key): 
        root.left = insertRec(root.left, key) 
    elif (key > root.key): 
        root.right = insertRec(root.right, key) 
  
  # return the root 
    return root 
    
# A function to do  
# inorder traversal of BST 
def inorderRec(root, x, ord): 
    if (root != None):
        t = inorderRec(root.left, x, ord)
        if (t != None):
            return t
        ord += 1
        if (root.key == x):
            return ord
        t = inorderRec(root.right, x, ord)
        if (t != None):
            return t
    return None

def iR(root): 
  if (root != None): 
    iR(root.left) 
    print(root.key ,end = " ") 
    iR(root.right) 



cmd = list(int(num) for num in input().decode().split())
cnt = 0
while cmd[0] != 0:
    if (cmd[0] == 1):
        insert(cmd[1])
        #print('i', root.key)
        cnt += 1
    else:
        #iR(root)
        #print()
        t = inorderRec(root, cmd[1], 0)
        if (t == None):
            print(0)
        else:
            print(t) 
    cmd = [int(num) for num in input().decode().split()]

