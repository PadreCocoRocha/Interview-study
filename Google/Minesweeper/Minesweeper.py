import numpy as np
from pprint import pprint
from random import randint

MINE = 9

class Matrix:

	def __init__(self, rows, cols, bombs):
		self.cols = cols
		self.rows = rows

		size = rows*cols
		(place,start,n) = (9,0,bombs) if bombs < size/2 else (0,9,size-bombs)

		# initialize matrix
		# self.matrix = np.full((rows,cols), start)
		self.matrix = [[start for i in range(cols)] for i in range(rows)]

		# Fill with zeroes or bombs (9)
		counter = 0
		while counter < n:
			pos = (randint(0,rows-1),randint(0,cols-1))
			if self.matrix[pos[0]][pos[1]] != place:
				self.matrix[pos[0]][pos[1]] = place
				counter += 1

		# pprint(self.matrix)
		self.fillValues()
		self.printGraphs()


	def fillValues(self):
		for row in range(self.rows):
			# Not in the top or bottom border
			ntb, nbb = row != 0, row != self.rows-1
			for col in range(self.cols):
				if self.matrix[row][col] == 9: continue

				# Not in the left or right border
				nlb, nrb = col != 0, col != self.cols-1
						
				n = sum([# left column
						nlb and self.matrix[row][col-1] == 9,
						nlb and nbb and self.matrix[row+1][col-1] == 9,
						nlb and ntb and self.matrix[row-1][col-1] == 9,
						# upper value
						ntb and self.matrix[row-1][col] == 9,
						# right column
						nrb and self.matrix[row][col+1] == 9,
						nrb and nbb and self.matrix[row+1][col+1] == 9,
						nrb and ntb and self.matrix[row-1][col+1] == 9,
						# bottom value
						nbb and self.matrix[row+1][col] == 9 ])

				self.matrix[row][col] = n

	def printGraphs(self):
		graph = []
		for row in range(self.rows):
			string = ' '.join(str(i) for i in self.matrix[row])
			string = string.replace('9','*').replace('0',' ')
			graph.append(string)

		pprint(graph)

Matrix(47,38,300)