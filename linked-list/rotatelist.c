#include "header.h"
listnode* rotateRight(listnode* A, int B) {
    int len =length(A);
    if(A==NULL || A->next==NULL|| B%len == 0){
        return A;
    }
    listnode* temp=A;
    listnode* prev=A;
    B = len-B%len;
    while(B--){
        prev =temp; 
        temp = temp->next;
    }
    listnode* head = temp;
    prev->next=NULL;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=A;
    return head;
    
}
int main()
{
    int a[] = {71,12,213,1,24,123,41,234,1};
    int n = sizeof(a) / sizeof(a[0]);
    listnode *head = NULL;
    head = create_list(head, a, n);
    print(head);
    head = rotateRight(head,1);
    print(head);
}