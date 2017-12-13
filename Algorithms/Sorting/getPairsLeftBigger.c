// exercise problem in https://www.hackerearth.com/pt-br/practice/algorithms/sorting/merge-sort/tutorial/
#include <stdio.h>
#include <stdlib.h>
#include "../Helpers/helpers.h"

int pair_counter = 0;
    
void merge(int *arr, int *tmp, int start, int mid, int end){
    int counter = 0,
        leftp = start,
        rightp = mid,
        latest_leftv = arr[leftp];
    
    while(leftp < mid && rightp < end){
        if (arr[leftp] < arr[rightp]){
            tmp[counter++] = arr[leftp++];
        } else {
            tmp[counter++] = arr[rightp++];
            pair_counter += (mid - leftp);
        }
    }
    while (leftp < mid) tmp[counter++] = arr[leftp++];
    while (rightp < end) tmp[counter++] = arr[rightp++];
    
    for(int i = 0; i < counter; i++){
        arr[start + i] = tmp[i]; 
    }
}

void merge_sort(int *arr, int *tmp, int start, int end){
        if (end - start < 2) { return; }
        int mid = (start + end)/2;
        
        merge_sort(arr, tmp, start, mid);
        merge_sort(arr, tmp, mid, end);
        merge(arr, tmp, start, mid, end);
    }

void getPairs(int *arr, int size){
    int *tmp = (int*) calloc(sizeof(int), size);
    merge_sort(arr, tmp, 0, size);
    free(tmp);
}

int main(int argc, char *argv[]){
    int n = strtol(argv[1], NULL, 10);
    
    // scanf("%i", n);
    int *arr = (int*) calloc(sizeof(int), n);
    printf("%i\n", n);
    
    for (int i = 2; i < n + 2; i++){
        arr[i-2] = strtol(argv[i], NULL, 10);
    }
    printRangeInt(arr, 0, n);
    
    getPairs(arr, n);

    printf("nr of pairs: %i\n", pair_counter);

    free(arr);
    exit(0);
}
