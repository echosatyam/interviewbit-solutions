#include"header.h"

int min(A,B){
    return A<B?A:B;
}
int minDepth(treenode* A) {
    if(A==NULL)
        return 0;
    if (A->left==NULL && A->right==NULL)
        return 1;
    if (A->left==NULL)
        return 1+ minDepth(A->right);
    if(A->right==NULL)
        return 1 + minDepth(A->left);
    return 1 + min(minDepth(A->right),minDepth(A->left));
}
