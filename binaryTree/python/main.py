from typing import List
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# time 20210616




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution001_1:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            else:
                left = self.searchBST(root.left,val)
                right = self.searchBST(root.right,val)
                if left:
                    return left
                elif right:
                    return right
                else:
                    return None
        else:
            return None
class Solution001_2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            elif root.val < val:
                return self.searchBST(root.right,val)
            else:
                return self.searchBST(root.left,val)
        else:
            return None

class Solution001_3:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val == val:
            root = root.left if root.val > val else root.right
        return root

"""
1. 忽略了二叉搜索树的条件
2. 写法上可以更简洁一点儿
3. 这种写法是从讨论区发现的，和第二种相比，时间和空间上无差别。
    但一个是递归，一个是遍历。递归需要额外的出栈入栈，遍历应该不需要要，
    为啥运行时间一样呢？



"""

if __name__ == "__main__":
    # input = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
    input = [[1, 1, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1]]
    solution = Solution2_2()
    result = solution.kWeakestRows(input, 3)
    print(result)
