#include <stdio.h>
#include "solution.h"

int main() {
    int input[4][4] = {{4,3,2,-1},{3,2,1,-1},{1,1,-1,-2},{-1,-1,-2,-3}};
    int **input1 = (int**)input;
    int input2[4] = {4,4,4,4};
    int result;
    result = countNegatives(input1,4,input2);
    printf("result is %d!\n",result);
    return 0;
}
