#include "header.h"
int isSameTree(treenode *A, treenode *B)
{
    if (A == NULL && B == NULL)
        return 1;
    if (A == NULL || B == NULL || (A->val != B->val))
        return 0;
    return isSameTree(A->left, B->left) && isSameTree(A->right, B->right);
}