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


