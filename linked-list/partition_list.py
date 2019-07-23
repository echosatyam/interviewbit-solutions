""" 
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
 """

class Solution:
    def __init__(self):
        self.left_head =None
        self.right_head=None
    def partition(self, A, B):
        if(A==None or A.next==None):
            return A
        temp = A
        left_rem=None
        right_rem = None
        while(temp!=None):
            if(temp.val<B):
                left_rem = temp
                self.left_head = ListNode(temp.val)
                break
            temp=temp.next
        temp = A
        while(temp!=None):
            if(temp.val>=B):
                right_rem = temp
                self.right_head = ListNode(temp.val)
                break
            temp=temp.next
        right = self.right_head
        left = self.left_head
        temp = A
        while(temp!=None):
            if(temp==left_rem or temp ==right_rem):
                temp=temp.next
                continue
            if(temp.val<B):
                left.next = ListNode(temp.val)
                left=left.next
            else:
                right.next = ListNode(temp.val)
                right=right.next
            temp = temp.next
        if(self.left_head==None):
            return self.right_head;
        temp = self.left_head
        while(temp.next!=None):
            temp=temp.next
        temp.next = self.right_head
        return self.left_head
        
                