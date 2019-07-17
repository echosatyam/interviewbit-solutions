#include "header.h"
int lPalin(listnode *A)
{
    listnode *slow_ptr = A;
    listnode *fast_ptr = A;
    while (fast_ptr != NULL && fast_ptr->next!=NULL){
        
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }
    listnode *prev = NULL;
    listnode *curr = slow_ptr;
    listnode *next = slow_ptr;

    while (curr != NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    slow_ptr = prev;
    listnode *temp = A;
    while (slow_ptr != NULL && temp != NULL)
    {
        if (slow_ptr->val != temp->val)
        {
            return 0;
        }
        slow_ptr = slow_ptr->next;
        temp = temp->next;
    }
    return 1;
}
int main()
{
    int a[] = {1, 2, 1};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    int x = lPalin(head);
    printf("the result is : %d", x);
}