// Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

// Example:

// Given the following matrix:

// [
//     [ 1, 2, 3 ],
//     [ 4, 5, 6 ],
//     [ 7, 8, 9 ]
// ]
// You should return

// [1, 2, 3, 6, 9, 8, 7, 4, 5]

vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
	vector<int> result;
	int T = 0, B = A.size() - 1,
	    L = 0, R = A[0].size() - 1;
	enum Direction { RIGHT, DOWN, LEFT, UP };
	
    Direction dir = RIGHT;
	while(T <= B && L <= R){
	    if (dir == RIGHT){
	        for (int i = L; i <= R; i++) result.push_back(A[T][i]);
	        dir = DOWN;
	        T++;
	    } else if (dir == DOWN){
	        for (int i = T; i <= B; i++) result.push_back(A[i][R]);
	        dir = LEFT;
	        R--;
	    } else if (dir == LEFT){
	        for (int i = R; i >= L; i--) result.push_back(A[B][i]);
	        dir = UP;
	        B--;
	    } else if (dir == UP){
	        for (int i = B; i >= T; i--) result.push_back(A[i][L]);
	        L++;
	        dir = RIGHT;
	    }
	}
	
	return result;
}