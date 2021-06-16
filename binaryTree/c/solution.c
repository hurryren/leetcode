//
// Created by 82316 on 2021/6/16.
//
#include<stdio.h>
#include "solution.h"


// https://leetcode.com/problems/search-in-a-binary-search-tree/
// time 20210616
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* searchBST(struct TreeNode* root, int val){
    if(root){
        if (root->val == val){
            return root;
        }else if(root->val < val){
            return searchBST(root->left,val);
        }else{
            return searchBST(root->right,val);
        }
    }else{
        return NULL;
    }


}



// https://leetcode.com/problems/diameter-of-binary-tree/submissions/
// 20210616

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int get_diameter(struct TreeNode* root, int * max_length);

int diameterOfBinaryTree(struct TreeNode* root){
    int max_length = 0;
    get_diameter(root,&max_length);
    return max_length;
}

int get_diameter(struct TreeNode* root, int * max_length){
    if(root == NULL){
        return 0;
    }
    int left = get_diameter(root->left,max_length);
    int right = get_diameter(root->right,max_length);

    if (left + right > *max_length){
        *max_length = left + right;
    }

    if (left > right){
        return 1 + left;
    }else{
        return 1 + right;
    }
}

/*
 * 学到一个宏
 * #define MAX(a, b) ((a) > (b) ? : (a) : (b))
 * */
#define MAX(a, b) ((a) > (b) ? : (a) : (b))
