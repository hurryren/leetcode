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

# https://leetcode.com/problems/diameter-of-binary-tree/submissions/
# 20210616

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution002_1:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # print(self.min_length_of_tree(root))
        diameter = self.get_diameter(root)
        max_length = self.max_length_of_tree(root) -1

        return max(max_length,diameter)


    def get_diameter (self,root:TreeNode)->int:
        if root == None:
            return 0

        max_length = 0
        if root.left and root.left:
            max_length = self.max_length_of_tree(root.left) + self.max_length_of_tree(root.right)
            child_length = max(self.get_diameter(root.left),self.get_diameter(root.right))
            return max(max_length,child_length)
        return max_length


    def max_length_of_tree(self,root:TreeNode) -> int:
        if root:
            return 1 + max(self.max_length_of_tree(root.left),self.max_length_of_tree(root.right))
        else:
            return 0

    def min_length_of_tree(self,root:TreeNode) -> int:
        if root:
            return 1 + min(self.min_length_of_tree(root.left),self.min_length_of_tree(root.right))
        else:
            return 0

class Solution002_2:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.length = 0

        self.get_diameter(root)

        return self.length


    def get_diameter (self,root:TreeNode) -> int:
        if root == None:
            return 0

        left = self.get_diameter(root.left)
        right = self.get_diameter(root.right)
        if left + right > self.length:
            self.length = left + right

        return 1 + max(left , right)




"""
1. 大致思路是，如果一个节点拥有左右子节点，则分别获取左右节点的最大深度，两者相加则为当前节点的最长路径
    ，如果没有左右子节点，则根节点的的最大深度为最长路径
2. 测试用例不够，方法1有bug。方法2是从讨论区抄来的。和方法1相比，每个子节点不需要重复计算最大深度，
    而是由叶子节点递归上来，省下了很多重复的递归


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
