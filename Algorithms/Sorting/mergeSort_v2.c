// Example program
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include "../Helpers/helpers.h"

static int *tmp;

void merge(int* arr, int low_idx, int half_idx, int high_idx){   
    int i = 0, count = 0,
        left_idx = low_idx,
        right_idx = half_idx;

    // loop while there are elements in any of the sides
    while (left_idx < half_idx && right_idx < high_idx){
        if (arr[left_idx] <= arr[right_idx]){
            tmp[count++] = arr[left_idx++];
        } else {
            tmp[count++] = arr[right_idx++];
        }
    }
    /* handle remaining elements in each side */
    while (left_idx < half_idx) tmp[count++] = arr[left_idx++];
    while (right_idx < high_idx) tmp[count++] = arr[right_idx++];

    // copy results back to original arr
    for (i = 0; i < count; i++) arr[low_idx + i] = tmp[i];
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
    tmp = (int*) calloc(size, sizeof(int));
    recursiveMergeSort(arr, 0, size);
    free(tmp);
}

int main(int argc, char *argv[]){
    if (argc < 1){
        printf("You have to enter the number of items to be generated!\n");
        exit(1);
    }

    clock_t begin, end;
    int nr_items = strtol(argv[1], NULL, 10);
    int *arr = calloc(sizeof(int), nr_items);

    // generate array
    srand(time(NULL));
    begin = clock();
    for (int i = 0; i < nr_items; i++){
        arr[i] = rand() % nr_items;
    }
    end = clock();
    printf("Done array generation in %f\n", (double) (end - begin)/CLOCKS_PER_SEC);

    // printRangeInt(arr, 0, nr_items);
    
    // timing functions
    begin = clock();
    sort(arr, nr_items);
    end = clock();

    printf("Done in %f\n", (double) (end - begin)/CLOCKS_PER_SEC);

    // printRangeInt(arr, 0, nr_items);
    
    free(arr);
    exit(0);
}
