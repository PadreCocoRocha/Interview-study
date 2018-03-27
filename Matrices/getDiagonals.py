from sys import argv
from random import randint
from pprint import pprint

def diagonals(matrix, _reversed=False):
	M, N = len(matrix), len(matrix[0])

	return [[matrix[p-d+M-1 if not _reversed else d-p][p] \
			for p in range(max(0, d-M+1), min(d, N-1)+1)] \
			for d in range(0, M+N-1)]

if __name__ == '__main__':

	M, N = int(argv[1:3]) if len(argv) == 3 else randint(3,20), randint(3,20)

	matrix = [[randint(0,9) for i in range(N)] for i in range(M)]


	for row in matrix: pprint(row)
	print()
	for row in diagonals(matrix): pprint(row)
	for row in diagonals(matrix,True): pprint(row)