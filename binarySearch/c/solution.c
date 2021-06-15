//
// Created by 82316 on 2021/6/15.
//
#include<stdio.h>
#include "solution.h"

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
