
//   Definition for singly-linked list.
#include <stdio.h>
#include<stdlib.h>
struct ListNode
{
    int val;
    struct ListNode *next;
};

typedef struct ListNode listnode;

listnode *listnode_new(int val)
{
    listnode *node = (listnode *)malloc(sizeof(listnode));
    node->val = val;
    node->next = NULL;
    return node;
}
int length(listnode *head)
{
    int len = 0;
    while (head != NULL)
    {
        head = head->next;
        len++;
    }
    return len;
}
listnode* insert_head(listnode* head,int val){
    listnode* new_node = listnode_new(val);
    new_node->next=head;
    head = new_node;
    return head;
}
void print(listnode *head)
{
    if (head == NULL)
    {
        return;
    }
    printf("The linked list is: ");
    while (head->next != NULL)
    {
        printf("%d ->", head->val);
        head = head->next;
    }
    printf("%d\n", head->val);
}
listnode* reverseList(listnode *A)
{
    listnode *prev = NULL;
    listnode *curr = A;
    listnode *next = A;
    while (curr != NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

listnode* create_list(listnode* head,int a[],int n){
    int i=0;
    for(i;i<n;i++){
        head = insert_head(head,a[i]);
    }
    return reverseList(head);
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