
# coding: utf-8

# In[41]:


# serach binary tree
# 7种遍历
class treeNode:
    def __init__(self,key,data,left=None,right=None,parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        


class binarySerachTree:
    def __init__(self):
        self.root = None
    
    def add(self,key,data):
        if self.root:
            self._add(key,data,self.root)
        else:
            self.root = treeNode(key,data)
    
    def _add(self,key,data,curr_node):
        if key < curr_node.key:
            if curr_node.left:
                self._add(key,data,curr_node.left)
            else:
                curr_node.left = treeNode(key,data,parent = curr_node)
        else:
            if curr_node.right:
                self._add(key,data,curr_node.right)
            else:
                curr_node.right = treeNode(key,data,parent = curr_node)
    def preOrder(self):
        if not self.root:
            return
        stakeNode = []
        stakeNode.append(self.root)
        while stakeNode:
            node = stakeNode.pop()
            print(node.key)
            if node.right:
                stakeNode.append(node.right)
            if node.left:
                stakeNode.append(node.left)
    
    def recur_pre(self,node):
        if node:
            print(node.key)
            self.recur_pre(node.left)
            self.recur_pre(node.right)
    
    def midOrder(self):
        if not self.root:
            return
        stakeNode = []
        node = self.root
        while stakeNode or node:
            while node:
                stakeNode.append(node)
                node = node.left
            node = stakeNode.pop()
            print(node.key)
            node = node.right
        
    
    def recur_mid(self,node):
        if node:
            self.recur_mid(node.left)
            print(node.key)
            self.recur_mid(node.right)
            
    def aftOrder(self):
        if not self.root:
            return
        stakeNode = []
        markNode = None
        node = self.root
        while stakeNode or node:
            while node:
                stakeNode.append(node)
                node = node.left
            node = stakeNode.pop()
            if not node.right or node.right == markNode:
                print(node.key)
                markNode = node
                node = None
            else:
                stakeNode.append(node)
                node = node.right
        
    def recur_aft(self,node):
        if node:
            self.recur_aft(node.left)
            self.recur_aft(node.right)
            print(node.key)

