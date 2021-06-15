# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/
# time 20210615

class Solution1(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    num += 1

        return num

class Solution2(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    num += n-j
                    break

        return num

class Solution3(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        num = 0;
        for item in grid:
            num = num+  self.findNegatives(item,n)
        return num

    def findNegatives(self,gridLine,n):
        if len(gridLine) == 0:
            return int(0)
        if gridLine[-1] >= 0:
            # print(gridLine[-1])
            return int(0)
        if gridLine[0] < 0:
            return n
        if n <= 4:
            for item in gridLine:
                if item < 0:
                    return int(n - gridLine.index(item))
        else:
            return int(self.findNegatives(gridLine[:int(n/2)], int(n/2)) + self.findNegatives(gridLine[int(n/2):], n - int(n/2)))



"""
1. 可以直接 for item in grid:
2. 每一行都是从大到小排列，所以遇到负数可以跳出循环，
3. 从2的思路优化,实际运行时间从 99% 变成 41%，经典负优化
总结：没弄明白这道题和二叉树的关系，指的是二分查找吗？
"""

if __name__ == "__main__":
    # input = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    input = [[3,2],[1,0]]
    solution = Solution3()
    result = solution.countNegatives(input)
    print(result)
