//
// Created by 82316 on 2021/6/15.
//

#ifndef C_SOLUTION_H
#define C_SOLUTION_H

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode {
         int val;
         struct TreeNode *left;
         struct TreeNode *right;
};
struct TreeNode* searchBST(struct TreeNode* root, int val);

#endif //C_SOLUTION_H
