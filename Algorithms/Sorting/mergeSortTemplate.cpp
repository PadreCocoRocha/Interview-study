// Example program
#include <iostream>
#include <string>

using namespace std;

template <typename T>

class mergeSort{
    private:
        T *temp;
    
    public:        
        void sort(T *Array){                       
            T *lp = Array,
              *hp = Array + sizeof(Array)/sizeof(T);
            
            temp = (T*) calloc(sizeof(Array), 1);
            recursiveMergeSort(lp, hp);
            free(temp);
        }
        
        void recursiveMergeSort(T* lp, T* hp){
            if ((hp - lp) < 2) { return; }
            T* sum = (T*) 0x01;
            T* halfp = (hp + lp + sum)/2;
            
            // left Part
            recursiveMergeSort(lp, halfp);
            
            // right part
            recursiveMergeSort(halfp, hp);
            
            // merge
            merge(lp, halfp, hp);
        }
        
        void merge(T* lp, T* halfp, T* hp){
            
            T *leftp = lp,
              *rightp = halfp;
            int count = 0;
            
            while(leftp < halfp || rightp < hp){
                if (leftp < halfp && *leftp <= *rightp){
                    temp[count] = *leftp;
                    leftp++; 
                    count++;
                }
                if (rightp < hp && *rightp <= *leftp){
                    temp[count] = *rightp;
                    rightp++; 
                    count++;
                }
            }
            
            copy(temp, temp + count, lp);            
        }
};

int main()
{
    int arr[] = {3, 4, 1, 2, 3};
    mergeSort<int> myObj;
    myObj.sort(arr);
    
    for (auto &i: arr){
        cout << i;
    }
}
