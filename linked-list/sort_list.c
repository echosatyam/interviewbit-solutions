#include "header.h"
void mergeSort(listnode **A);
void front_back_split(listnode *A, listnode **front, listnode **back);
listnode *SortedMerge(listnode *a, listnode *b)
{
    listnode *result = NULL;

    if (a == NULL)
        return (b);
    else if (b == NULL)
        return (a);

    if (a->val <= b->val)
    {
        result = a;
        result->next = SortedMerge(a->next, b);
    }
    else
    {
        result = b;
        result->next = SortedMerge(a, b->next);
    }
    return (result);
}
listnode *sortList(listnode *A)
{
    if (A == NULL || A->next == NULL)
        return A;
    mergeSort(&A);
    return A;
}
void mergeSort(listnode **A)
{
    if (*A == NULL || (*A)->next == NULL)
        return;
    listnode *front;
    listnode *back;
    front_back_split(*A, &front, &back);
    mergeSort(&front);
    mergeSort(&back);
    *A = SortedMerge(front, back);
}
void front_back_split(listnode *source, listnode **frontRef, listnode **backRef)
{
    listnode *fast, *slow;
    slow = source;
    fast = source->next;

    /* Advance 'fast' two nodes, and advance 'slow' one node */
    while (fast != NULL)
    {
        fast = fast->next;
        if (fast != NULL)
        {
            slow = slow->next;
            fast = fast->next;
        }
    }

    *frontRef = source;
    *backRef = slow->next;

    slow->next = NULL;
}
int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    print(head);
    head = sortList(head);
    print(head);
    return 0;
}