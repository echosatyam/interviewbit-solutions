class Solution:
    def reverse(self,A):
        if A==None or A.next==None:
            return A
        prev=None
        curr =A
        while(curr!=None):
            next_ = curr.next
            curr.next=prev
            prev= curr
            curr=next_
        return prev
    def reorderList(self, A):
        if(A==None or A.next==None or A.next.next==None):
            return A
        slow = A
        fast = A
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
        second_part = slow.next
        slow.next=None
        second_part = self.reverse(second_part)
        temp= A
        while(temp!=None and second_part!=None):
            next_first = temp.next;
            next_second = second_part.next
            temp.next = second_part
            second_part.next = next_first
            temp = next_first
            second_part = next_second
        return A
        
        
