""" 
Given a singly linked list, modify the value of first half nodes such that :

1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …

 NOTE :
If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. So, if L = 5, the first half refers to first 2 nodes.
If the length L of linked list is even, then the first half implies at first L/2 nodes. So, if L = 4, the first half refers to first 2 nodes.
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,

You should return 4 -> 2 -> 3 -> 4 -> 5
as

for first node, 5 - 1 = 4
for second node, 4 - 2 = 2
Try to solve the problem using constant extra space.
 """

class Solution:
    def reverse(self, A):
        if(A == None or A.next == None):
            return A
        prev = None
        next_ = A
        current = A
        while(current != None):
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        return prev

    def subtract(self, A):
        if A == None or A.next == None:
            return A
        slow = A
        fast = A
        prev = A
        while fast != None and fast.next != None:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        second_half = slow
        if fast != None:
            prev = prev.next
            second_half = slow.next
        temp = A
        reversed_second = self.reverse(second_half)
        tracker = reversed_second
        while(reversed_second != None and temp != None):
            temp.val = reversed_second.val-temp.val
            reversed_second = reversed_second.next
            temp = temp.next
        prev.next = self.reverse(tracker)
        return A
