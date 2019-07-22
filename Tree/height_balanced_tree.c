#include "header.h"

int max(A, B)
{
    return A > B ? A : B;
}
int depth(treenode *A)
{
    if (A == NULL)
        return 0;
    return 1 + max(depth(A->right), depth(A->left));
}
int isBalanced(treenode *A)
{
    if (A == NULL)
        return 1;
    if (abs(depth(A->left) - depth(A->right)) > 1)
        return 0;
    int right = isBalanced(A->right);
    int left = isBalanced(A->left);
    return left && right;
}
