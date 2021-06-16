from typing import List
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/
# time 20210615


class Solution1_1(object):
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


class Solution1_2(object):
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


class Solution1_3(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        num = 0
        for item in grid:
            num = num + self.findNegatives(item, n)
        return num

    def findNegatives(self, gridLine, n):
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


# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# time 20210616

class Solution2_1:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        # soldier = []
        result = [[] * (m+1) for _ in range(n+1)]
        print(result)
        print(mat)
        for i in range(m):
            # soldier.append(self.num_soldiers(item, n))
            t = self.num_soldiers(mat[i], n)
            print(t)
            result[self.num_soldiers(mat[i], n)].append(i)

        temp = []
        for i in range(n+1):
            temp = temp + result[i]

        print(temp)
        print(result)
        return temp[:k]
        # for i in range(k):

        # return soldier

    def num_soldiers(self, mat_rows: List[int], n: int) -> int:
        if len(mat_rows) == 0:
            return 0
        else:
            if(mat_rows[0] == 0):
                return 0
            elif mat_rows[-1] == 1:
                return n
            else:
                for i in range(n):
                    if(mat_rows[i] == 0):
                        return i


class Solution2_2:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        # soldier = []
        result = [[] * (m+1) for _ in range(n+1)]
        print(result)
        print(mat)
        for i in range(m):
            # soldier.append(self.num_soldiers(item, n))
            if len(mat[i]) == 0:
                t = 0
            else:
                if(mat[i][0] == 0):
                    t = 0
                elif mat[i][-1] == 1:
                    t = n
                else:
                    for j in range(n):
                        if(mat[i][j] == 0):
                            t = j
                            break
            # t = self.num_soldiers(mat[i], n)
            print(t)
            result[t].append(i)

        temp = []
        for i in range(n+1):
            temp = temp + result[i]

        print(temp)
        print(result)
        return temp[:k]
        # for i in range(k):

        # return soldier


"""
1. 需要稳定排序，现在用的算是桶排序，但是之后还是需要遍历一次得到排序结果。
并且在python中list空间是否预先分配对空间使用个运行时间影响很大。
# result = [[] * (m+1) for _ in range(n+1)]
将该行代码中的 m+1 改为 1 的时候，运行时间增加了4ms，memory减少了0.1MB
但是
        time    73.06%->48.62%
        memory  46.12%->74.68.62%
改进方向，获取1的个数的时候，不要用函数，能少不少开销
另外就是排序算法，

2. 好像也没啥用，等排序算法掌握娴熟了再回来看看
3. TODO
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
