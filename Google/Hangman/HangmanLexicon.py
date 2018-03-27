# File: HangmanLexicon.java -> .ypy
# -------------------------
# This file contains a stub implementation of the HangmanLexicon
# class that you will reimplement for Part III of the assignment.

class HangmanLexicon:
	# Returns the number of words in the lexicon.
	def getWordCount(self):
		return 10;

	# Returns the word at the specified index.
	def getWord(self, index):
		options =  {
			0: "BUOY",
			1: "COMPUTER",
			2: "CONNOISSEUR",
			3: "DEHYDRATE",
			4: "FUZZY",
			5: "HUBBUB",
			6: "KEYHOLE",
			7: "QUAGMIRE",
			8: "SLITHER",
			9: "ZIRCON"
		}
		return options.get(index, "Invalidindex")