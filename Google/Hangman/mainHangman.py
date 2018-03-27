from HangmanLexicon import HangmanLexicon
from HangmanSolver import HangmanSolver

if __name__ == '__main__':

	solver = HangmanSolver(HangmanLexicon())
	curr = solver.getCurrent()

	result = 0
	print("Current puzzle (%i letters): %s" %(len(curr), curr))
	while (result == 0):
		guess = raw_input("Guess a letter: ")
		result, _, output = solver.makeAMove(guess)
		print(output) #print output
		print(solver.getCurrent()) #print current answer

	if result == 1: print("Congratulations, you won! =D")
	else: 
		print("That's a shame, you lost! =/")
		print("Answer was %s" %solver.getAnswer())
