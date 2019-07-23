#include "header.h"
treenode* head = NULL;
treenode* arrayToBST(const int* A,int low, int high){
    if( low <=high){
        int mid = (int)(high+low)/2;
        // printf("%d",A[mid]);
        treenode* node = treenode_new(A[mid]);
        if(head == NULL){
            head =node;
        }
        node->left = arrayToBST(A,low,mid-1);
        node->right = arrayToBST(A,mid+1,high);
        return node;
    }
    return NULL;
}


treenode* sortedArrayToBST(const int* A, int n1) {
    // printf("%d",n1);
    arrayToBST(A,0,n1-1);
    return head;
}