
# coding: utf-8

# In[ ]:


#快排
def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j]<=x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1
        
def QuickSort(A,p,r):
        if p<r:
            q = Partition(A,p,r)
            QuickSort(A,p,q-1)
            QuickSort(A,q+1,r)
            
#计数排序
def countsort(A,k):
    c = [0]*(k+1)
    b = [None]*len(A)
    for i in range(len(A)):
        c[A[i]] += 1
    for i in range(1,k+1):
        c[i] = c[i]+c[i-1]
    for i in range(len(A)-1,-1,-1):
        b[c[A[i]]-1] = A[i]
        c[A[i]] -= 1
    return b

