#include "header.h"

treenode* Find(treenode* root,int B ){
    if(root==NULL || root->val==B)
        return root;
    else if (root->val<B)
        return Find(root->right,B);
    else
        return Find(root->left,B);
}

treenode* FindMin(treenode* root){
    if (root==NULL)
        return root;
    treenode* temp = root;
    while(temp->left!=NULL)
        temp =temp->left;
    return temp;
}
treenode* getSuccessor(treenode* A, int B) {
    treenode* current = Find(A,B);
    if(current->right!=NULL)
        return FindMin(current->right);
    treenode* successor = NULL;
    treenode* ancestor = A;
    while(ancestor!=current){
        if(current->val < ancestor->val) {
            successor = ancestor;
            ancestor = ancestor->left;
        }  
        else
            ancestor = ancestor->right;
    }
    return successor;
} 