#include "header.h"

/* 
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 

See "header.h" included in this folder for implementation of linked list.
Solution is referred from geeks for geeks.

 */
listnode *detectCycle(listnode *A)
{
    if (A == NULL || A->next == NULL)
        return NULL;

    listnode *slow = A->next;
    listnode *fast = A->next->next;
    while (slow != NULL && fast != NULL && fast->next != NULL)
    {
        if (slow == fast)
            break;
        slow = slow->next;
        fast = fast->next->next;
    }
    if (slow != fast)
        return NULL;

    slow = A;
    while (slow != fast)
    {
        slow = slow->next;
        fast = fast->next;
    }
    return slow;
}
int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    print(head);

    head->next->next->next->next = head->next->next->next;
    listnode *cycle_node = detectCycle(head);
    printf("the value of node starting the cycle is: %d\n", cycle_node->val);
    return 0;
}