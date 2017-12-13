// Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

// For example:

// Given the array [-2,1,-3,4,-1,2,1,-5,4],

// the contiguous subarray [4,-1,2,1] has the largest sum = 6.

// For this problem, return the maximum sum.

int Solution::maxSubArray(const vector<int> &A) {
    int currMax, totalMax;
    currMax = totalMax = A[0];
    for (auto &num: A){
    	// if the current sum + the next number is smaller than the current sum
    	// then we should stop summing and start a new current sum, 
    	// because the max sum for now has been achieved
        currMax = max(currMax + num, num);
        totalMax = max(currMax, totalMax);
    }
    return totalMax;
}
