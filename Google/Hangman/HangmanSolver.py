# Hangman Solver
from random import randint
from pprint import pprint

class HangmanSolver:

	def __init__(self, lexicon):
		self.word = lexicon.getWord(randint(0, lexicon.getWordCount() - 1))
		self.current = "_" * len(self.word)
		self.rightGuesses = set()
		self.allGuesses = set()
		self.winningGuesses = set(self.word)
		self.score = 0
		self.error = 0
		self.totalErrors = 0

	def updateCurrentAnswer(self, guess):
		s = [c if c in self.rightGuesses else "_" for c in self.word]
		self.current = ''.join(s)

	def checkGuess(self,guess):
		guess = guess.upper()
		if len(guess) != 1 or not guess.isalpha():
			return 0

		if guess in self.word:
			if guess not in self.rightGuesses:
				self.score += 1
				self.rightGuesses.add(guess)
				self.allGuesses.add(guess)
				self.updateCurrentAnswer(guess)
			return 1

		self.allGuesses.add(guess)
		self.error += 1
		self.totalErrors += 1
		return -1

	def checkState(self):
		if self.rightGuesses == self.winningGuesses:
			return 1
		elif self.error == 6:
			return -1
		else:
			return 0

	def makeAMove(self, guess):
		output = ""
		guessResult = self.checkGuess(guess)
		if guessResult == 1:
			output = "Right!"
		elif guessResult == 0:
			output = "Invalid input!"
		else:
			output = "Wrong!!"

		output += " Remaining guesses: " + str(6-self.error)

		# returns 1 on win, -1 on lose, 0 on keep playing
		return (self.checkState(), guessResult, output)

	def getCurrent(self):	
		return self.current

	def getAnswer(self):
		return self.word

	def getGuesses(self):
		return ''.join(self.allGuesses)

	def getErrors(self):
		return self.error