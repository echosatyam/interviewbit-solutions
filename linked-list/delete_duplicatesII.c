#include "header.h"
listnode *deleteDuplicates(listnode *A)
{
    if (A == NULL || A->next == NULL)
        return A;
    listnode *head = NULL;
    listnode *temp, *prev;
    if (A->next->val != A->val)
    {
        head = A;
    }
    else
    {
        temp = A->next;
        prev = A;

        while (temp->next != NULL && (temp->val == temp->next->val || temp->val == prev->val))
        {
            prev = temp;
            temp = temp->next;
        }
        if (prev->val != temp->val)
            head = temp;
        if (head == NULL || head->next == NULL)
            return head;
    }
    temp = head->next;
    listnode *counter = head;
    prev = head;
    while (temp->next != NULL)
    {

        while (temp->next != NULL && (temp->val == temp->next->val || temp->val == prev->val))
        {
            prev = temp;
            temp = temp->next;
        }
        if (temp->next == NULL && prev->val != temp->val)
        {
            counter->next = temp;
            return head;
        }
        if (temp->next == NULL && prev->val == temp->val)
        {
            counter->next = NULL;
            return head;
        }
        counter->next = temp;
        counter = counter->next;
        temp = temp->next;
    }

    return head;
}
int main()
{
    int a[] = {1,2,3,4,5,6,7,8,9,10,11};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    print(head);
    head = deleteDuplicates(head);
    print(head);
    return 0;
}