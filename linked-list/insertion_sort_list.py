""" 
Insertion Sort List
Asked in:  
Microsoft
Google
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3

 """
class Solution:
    def __init__(self):
        self.head = None
    def sortedInsert(self,val):
        node = ListNode(val)
        if(self.head==None):
            self.head = node
        else:
            if(val<=self.head.val):
                node.next = self.head
                self.head = node
                return
            temp = self.head
            prev = self.head
            while(temp!=None and val > temp.val ):
                prev =temp
                temp = temp.next
            node.next= temp
            prev.next = node
        return
    def insertionSortList(self, A):
        if(A==None or A.next ==None):
            return A
        element = A
        while(element!=None):
            self.sortedInsert(element.val)
            element = element.next
        return self.head
            