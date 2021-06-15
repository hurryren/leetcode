//
// Created by 82316 on 2021/6/15.
//
#include<stdio.h>
#include "solution.h"


// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/
// time 20210615
int countNegatives(int** grid, int gridSize, int *gridColSize){
    int result = 0;
    for(int i = 0; i< gridSize;i++){
        for(int j = 0; j< gridColSize[i]; j++){
             printf("%d\n",gridColSize[i]);
            if(grid[i][j] < 0){
                 printf("i=%d, j=%d\n",i,j);

                result += gridColSize[i] - j;
                break;
            }
        }
    }
    return result;
}

/*
 * 对于 c 语言来说，半路跳出短循环导致指令预测失败(指令缓存未命中)，
 * 可能反而导致时间变长。不过如果循环足够长，还是有意义的
 * */
