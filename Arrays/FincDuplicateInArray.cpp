// Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

// Sample Input:

// [3 4 1 4 1]
// Sample Output:

// 1
// If there are multiple possible answers ( like in the sample case above ), output any one.

// If there is no duplicate, output -1

int Solution::repeatedNumber(const vector<int> &A) {
    int a, b;
    a = b = 0;
    
    for (int i = 1; i < A.size(); i++) a = a ^ i;
    for (auto const& num : A) b = b ^ num;
    
    return a^b;
}
