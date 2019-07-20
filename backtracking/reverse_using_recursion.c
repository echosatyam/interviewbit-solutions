#include "header.h"
listnode *head = NULL;
listnode *reverseList_recursion(listnode *A)
{
    if (A->next == NULL)
    {
        head = A;
        return head;
    }
    reverseList_recursion(A->next);
    A->next->next = A;
    A->next = NULL;
    return head;
}
int main()
{   int a[] = {1, 2, 3, 4,4,5, 5, 6, 7,7,7,7,7,7,8};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    print(head);
    head=reverseList_recursion(head);
    print(head);
    return 0;
}
