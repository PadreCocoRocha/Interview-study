/* 
    Helper functions file
*/
#include <stdio.h>
#include "helpers.h"

void printRangeInt(int* arr, int start, int stop){
    if (start >= stop) return;
    printf("[");
    while (start < stop){
        char c = (start != (stop - 1)) ? ',' : ']';
        printf("%i%c", arr[start++], c);
    }
    printf("\n");
}

void printRangeChar(char* arr, int start, int stop){
    if (start >= stop) return;
    printf("[");
    while (start < stop){
        char c = (start != (stop - 1)) ? ',' : ']';
        printf("%c%c", arr[start++], c);
    }
    printf("\n");
}
