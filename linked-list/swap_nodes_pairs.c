#include "header.h"
listnode *swap_node(listnode *A)
{
    if (A == NULL || A->next == NULL)
        return A;
    listnode *new_head = A->next;
    listnode *remaining = A->next->next;
    A->next->next=A;
    A->next = swap_node(remaining);
    return new_head;
}
int main()
{
    int a[] = {1, 2, 3, 4, 4, 5, 5, 6};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    print(head);
    head = swap_node(head);
    print(head);
    return 0;
}
