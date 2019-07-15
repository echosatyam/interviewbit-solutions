#include <stdio.h>
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

listnode *deleteDuplicates(listnode *A)
{
    if (A == NULL)
    {
        return;
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
{
    return 0;
}
