
//   Definition for singly-linked list.
#include <stdio.h>
#include "header.h"

listnode *getIntersectionNode(listnode *A, listnode *B)
{
    int a = length(A);
    int b = length(B);
    if (a == 0 || b == 0)
    {
        return NULL;
    }
    if (a < b)
    {
        listnode *temp = B;
        B = A;
        A = temp;
        int tempi = b;
        b = a;
        a = tempi;
    }
    int diff = a - b;
    while (diff--)
    {
        A = A->next;
    }
    while (A != NULL && B != NULL)
    {
        if (A == B)
        {
            return A;
        }
        A = A->next;
        B = B->next;
    }
    return NULL;
}
listnode *join_list(listnode *A, listnode *B)
{
    listnode *temp1 = A;
    while (temp1->next != NULL)
    {
        temp1 = temp1->next;
    }
    temp1->next = B;
    return A;
}
int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    print(head);

    int c[] = {76, 12, 124, 1, 41, 1, 12};
    n = sizeof(c) / sizeof(c[0]);
    listnode *A = NULL;
    A = create_list(A, c, n);

    int b[] = {214, 12, 214, 1, 12, 14, 12, 2};
    n = sizeof(b) / sizeof(b[0]);
    listnode *B = NULL;
    B = create_list(B, b, n);

    A = join_list(A, head);
    B = join_list(B, head);
    print(A);
    print(B);

    listnode *merged = getIntersectionNode(A, B);
    print(merged);

    return 0;
}