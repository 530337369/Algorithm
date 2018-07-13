
# coding: utf-8

# In[30]:


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
    def getVal(self):
        return self.val
    
    def getNext(self):
        return self.next
    
    def setVal(self,newVal):
        self.val = newVal
    
    def setNext(self,newNext):
        self.next = newNext
    

class unoderedLisetNode:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        item = Node(item)
        item.setNext(self.head)
        self.head = item
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count
    
    def serach(self,item):
        current = self.head
        while current != None:
            if current.getVal() == item:
                return True
            else:
                current = current.getNext()
        return False
    
    def remove(self,item):
        current = self.head
        previous = None
        if self.serach(item):
            while current.getVal()!= item:
                previous = current
                current = current.getNext()
            if not previous:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            return 'No such val'
        

