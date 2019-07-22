#include "header.h"

int max(A,B){
    return A>B?A:B;
}
int maxDepth(treenode* A) {
    if(A==NULL)
        return 0;
    return 1+ max(maxDepth(A->right),maxDepth(A->left));
}
