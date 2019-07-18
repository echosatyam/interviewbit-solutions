/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 * 
 * typedef struct ListNode listnode;
 * 
 * listnode* listnode_new(int val) {
 *     listnode* node = (listnode *) malloc(sizeof(listnode));
 *     node->val = val;
 *     node->next = NULL;
 *     return node;
 * }
 */
/**
 * @input A : Head pointer of linked list 
 * @input B : Head pointer of linked list 
 * 
 * @Output head pointer of list.
 */
#include "header.h"
listnode *mergeTwoLists(listnode *A, listnode *B)
{
    if (A == NULL)
        return B;
    if (B == NULL)
        return A;
    listnode *head = A;
    if (A->val > B->val)
    {
        head = B;
        B = B->next;
    }
    else
        A = A->next;

    listnode *tempa = A;
    listnode *tempb = B;
    listnode *store;
    listnode *curr = head;
    while (tempa != NULL || tempb != NULL)
    {
        if (tempa != NULL && tempb != NULL)
        {
            if (tempa->val <= tempb->val)
            {
                curr->next = tempa;
                curr = curr->next;
                tempa = tempa->next;
            }
            else
            {
                curr->next = tempb;
                curr = curr->next;
                tempb = tempb->next;
            }
        }
        else if (tempa != NULL && tempb == NULL)
        {
            curr->next = tempa;
            curr = curr->next;
            tempa = tempa->next;
        }
        else if (tempa == NULL && tempb != NULL)
        {
            curr->next = tempb;
            curr = curr->next;
            tempb = tempb->next;
        }
    }

    return head;
}
int main()
{
    int a[] = {1, 2, 3, 4, 51, 61, 71};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head1 = NULL;
    head1 = create_list(head1, a, n);
    print(head1);
    int b[] = {11, 21, 32, 42, 52, 62, 72, 106, 200};
    n = sizeof(b) / sizeof(b[0]);
    listnode *head2 = NULL;
    head2 = create_list(head2, b, n);
    print(head2);

    listnode *head = mergeTwoLists(head1, head2);
    printf("Merged: ");
    print(head);
}