""" 
Reverse Link List II
Asked in:  
Facebook
Microsoft
Amazon
Reverse a linked list from position m to n. Do it in-place and 
in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing 
the whole linked list which is obviously an easier version of 
this question. 
 """




class Solution:
    def reverse(self,A):
        if(A==None or A.next==None):
            return A
        prev = None
        curr = A
        while(curr!=None):
            next_ = curr.next
            curr.next = prev
            prev= curr
            curr = next_
        return prev
    def length(self,A):
        i = 0
        while A!=None:
            A=A.next
            i+=1
        return i
    def reverseBetween(self, A, B, C):
        if A==None or A.next ==None  or B==C:
            return A
        l = self.length(A)
        if B==1 and C ==l:
            return self.reverse(A)
        start_prev = A
        if(B==1):
            start_rev = A
        else:
            temp = A
            for i in range(B-2):
                temp = temp.next
            start_prev=temp
            start_rev = temp.next
        
        if(C ==l):
            start_prev.next = self.reverse(start_rev)
            return A
        temp = A
        for i in range(C-1):
            temp = temp.next
        end_prev = temp
        end_next= temp.next
        end_prev.next = None
        if B!=1:
            start_prev.next = self.reverse(start_rev)
        else:
            A= self.reverse(start_rev)
        start_rev.next = end_next
        return A
