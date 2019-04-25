
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

# 堆排序

# O(lgn)
def Max_Heapify(A,i,heap_size):
    l = 2*i+1
    r = 2*i+2
    largest = i
    if l<= heap_size and A[i] < A[l]:
        largest = l
    if r<= heap_size and A[largest] < A[r]:
        largest = r
    if i != largest:
        A[i],A[largest] = A[largest],A[i]
        Max_Heapify(A,largest,heap_size)
# O(n)        
def Build_Max_Heap(A):
    x = int(len(A)/2)-1
    for i in range(x,-1,-1):
        Max_Heapify(A,i,len(A)-1)
        
def Heap_Sort(A):
    if not A:
        return
    Build_Max_Heap(A)
    heap_size = len(A)-1
    while heap_size>0:
        A[0],A[heap_size] = A[heap_size],A[0]
        heap_size -=1
        Max_Heapify(A,0,heap_size)
    return A
	
	
	
#归并排序	
def Merge(A,p,q,r):
    l = A[p:q+1].copy()
    ri = A[q+1:r+1].copy()
    l.append(float('inf'))
    ri.append(float('inf'))
    i = 0
    j = 0
    for n in range(p,r+1,1):
        if l[i]<=ri[j]:
            A[n] = l[i]
            i += 1
        else:
            A[n] = ri[j]
            j += 1

			
			
def MergeSort(A,p,r):
    if p<r:
        q = int((r+p)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)


#二分查找 O(logn)
def BinarySerach(data,k):
    start = 0
    end = len(data)-1
    while start<=end:
        mid = (start+end)>>1
        if k<data[mid]:
            end = mid-1
        elif k>data[mid]:
            start = mid+1
        else:
            return mid
    return -1
	
#冒泡排序
def Bubble_sort(list):
	for i in range(len(list)-1,1,-1):
		for j in range(i):
			if list[j]>list[j+1]:
				list[j],list[j+1] = list[j+1],list[j]
	return list