// Example program
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include "../Helpers/helpers.h"

int *temp;

void merge(int* arr, int low_idx, int half_idx, int high_idx){   
    int i = 0, count = 0,
        // save the low and half indexes for later use
        left_idx = low_idx,
        right_idx = half_idx,
        // set booleans to evaluate whether any of the splitted sides
        // still has elements to be checked
        left_has = left_idx < half_idx, 
        right_has = right_idx < high_idx;

    // loop while there are elements in any of the sides
    while ( left_has || right_has ){
        if (left_has){
            if (arr[left_idx] <= arr[right_idx] || ! right_has){
                temp[count++] = arr[left_idx++];
                left_has = left_idx < half_idx;
            }
        }
        if (right_has){
            if (arr[right_idx] <= arr[left_idx] || ! left_has){
                temp[count++] = arr[right_idx++];
                right_has = right_idx < high_idx;
            }
        }
    }
    // copy results back to original arr
    for (i = 0; i < count; i++) arr[low_idx + i] = temp[i];
}

void recursiveMergeSort(int* arr, int low_idx, int high_idx){
    if ((high_idx - low_idx) < 2) { return; }

    int half_idx = (high_idx + low_idx + 1)/2;
    // left Part
    if (half_idx - low_idx > 1) {
        recursiveMergeSort(arr, low_idx, half_idx);
    } // right part
    if (high_idx - half_idx > 1) {
        recursiveMergeSort(arr, half_idx, high_idx);  
    }// merge
    merge(arr, low_idx, half_idx, high_idx);
}

void sort(int* arr, int size){
    temp = (int*) calloc(size, sizeof(int));
    recursiveMergeSort(arr, 0, size);
    free(temp);
}

int main(int argc, char *argv[]){
    if (argc < 1){
        printf("You have to enter the number of items to be generated!\n");
        exit(1);
    }

    int nr_items = strtol(argv[1], NULL, 10);
    int *arr = calloc(sizeof(int), nr_items);

    // generate array
    srand(time(NULL));
    for (int i = 0; i < nr_items; i++){
        arr[i] = rand() % nr_items;
    }

    printRangeInt(arr, 0, nr_items);
    
    // timing functions
    clock_t begin, end;
    begin = clock();
    sort(arr, nr_items);
    end = clock();

    printf("Done in %f\n", (double) (end - begin)/CLOCKS_PER_SEC);

    printRangeInt(arr, 0, nr_items);

    exit(0);
}
