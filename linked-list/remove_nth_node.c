#include "header.h"
listnode* removeNthFromEnd(listnode* A, int B) {
    if(A==NULL || B==0)
        return A;
    int len = length(A);
    if(B>len || len==1)
        return A->next;
    int n = len-B;
    listnode* prev= A;
    listnode* temp = A;
    while(n--){
        prev = temp;
        temp=temp->next;
    }
    prev->next=temp->next;
    return A;
}
int main()
{
    int a[] = {71};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    head = removeNthFromEnd(head,1);
    print(head);
}