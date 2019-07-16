#include <stdio.h>
#include "header.h"
listnode *deleteDuplicates(listnode *A)
{
    if (A == NULL)
    {
        return NULL;
    }
    listnode *temp = A;
    while (temp->next != NULL)
    {
        if (temp->val == temp->next->val)
        {
            listnode *curr = temp->next->next;
            free(temp->next);
            temp->next = curr;
        }
        else
        {
            temp = temp->next;
        }
    }
    return A;
}
int main()
{   int a[] = {1, 2, 3, 4,4,5, 5, 6, 7,7,7,7,7,7,8};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    print(head);
    head=deleteDuplicates(head);
    print(head);
    return 0;
}
