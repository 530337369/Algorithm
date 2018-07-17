
# coding: utf-8

# In[56]:


#Stake
class Stake(object):
    def __init__(self,S = []):
        self.S = S
        self.top = len(S)-1
    def stake_empty(self):
        return self.top <0

    def push(self,x):
        self.top += 1
        self.S.append(x)

    def pop(self):
        if self.stake_empty():
            return 'Eror Underflow'
        else:
            self.top -= 1
        return self.S.pop()
#Queue
class Queue(object):
    def __init__(self,Q ,head,tail):
        self.Q = Q
        self.head  = head
        self.tail = tail
    def enqueue(self,x):
        if self.head == self.tail +1 or (self.head ==0 and self.tail == len(self.Q)-1):
            return 'overflow'
        Q[self.tail] = x
        if self.tail == len(self.Q)-1:
            self.tail = 0
        else:
            self.tail += 1
    def dequeue(self):
        if self.tail == self.head:
            return 'underflow'
        x = Q[self.head]
        if self.head  == len(Q)-1:
            self.head = 0
        else:
            self.head += 1
        return x

