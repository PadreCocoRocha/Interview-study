// Find out the maximum sub-array of non negative numbers from an array.
// The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

// Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

// Example:

// A : [1, 2, 5, -7, 2, 3]
// The two sub-arrays are [1, 2, 5] [2, 3].
// The answer is [1, 2, 5] as its sum is larger than [2, 3]
// NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
// NOTE 2: If there is still a tie, then return the segment with minimum starting index

vector<int> Solution::maxset(vector<int> &A) {
    int currSum = -1,
        currStart = 0,
        currEnd = -1,
        maxSum = -1,
        maxStart = 0,
        maxEnd = -1,
        arrayLength = A.size();
    
    vector<int> result;
    
    for (int i = 0; i < arrayLength; i++){
        if (A[i] >= 0){
            if (currSum < 0){
                currStart = i;
                currEnd = i;
                currSum = 0;
            } else currEnd = i; 
            
            currSum += A[i];
            bool currVectorIsBigger = (maxEnd - maxStart) < (currEnd - currStart);
            
            if ((currSum > maxSum) || (currSum == maxSum && currVectorIsBigger)){
                maxSum = currSum;
                maxEnd = currEnd;
                maxStart = currStart;
            } 
        } else currSum = -1;
    }
    
    for (int i = 0; i < (maxEnd - maxStart) + 1; i++){
        result.push_back(A[maxStart + i]);
    }
    
    return result;
}
