#include "header.h"
treenode* invertTree(treenode* A) {
    if(A== NULL)
        return A;
    treenode* left = A->left;
    A->left =invertTree(A->right);
    A->right = invertTree(left);
    return A;
}
