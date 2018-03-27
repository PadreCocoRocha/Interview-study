from pprint import pprint
from collections import defaultdict

 # my first version
def findSubstring(S: str, D: set) -> str: 
	longest = ''
	for word in D:
		counter, index = 0, -1
		for char in word:
			index = S.find(char, index + 1)
			if index > -1:
				counter += 1
			else:
				break
		if len(word) == counter and counter > len(longest):
			longest = word

	return longest

# optimization 1: preprocess S:
def findSubstringOpt1(S: str, D: set) -> str:
	charsContainedInS = defaultdict(list)
	for i, c in enumerate(S):
		charsContainedInS[c].append(i)

	longest = ''
	for word in D:
		counter, index = 0, -1
		for c in word:
			if c in charsContainedInS:
				counter += 1
				for idx in charsContainedInS[c]:
					if idx > index:
						index = idx
						break
			else:
				break
		if len(word) == counter and counter > len(longest):
			longest = word

	return longest

# optimization 2: sort words
def findSubstringOpt2(S: str, D: set) -> str:
	charsContainedInS = defaultdict(list)
	for i, char in enumerate(S):
		charsContainedInS[char].append(i)

	for word in sorted(D, key=lambda x: len(x), reverse=True):
		counter, index = 0, -1
		for char in word:
			if char in charsContainedInS:
				counter += 1
				for idx in charsContainedInS[char]:
					if idx > index:
						index = idx
						break
			else:
				break
		if len(word) == counter:
			return word

	return ''

# optimization 3: Use a trie to process every word at once
def findSubstringOpt3(S: str, D: set) -> str:
	myTrie = defaultdict(list)

	# Map words by first letter and first index
	for word in D: myTrie[word[0]].append((word, 0))

	foundMatches = []
	# for every character in S, remap words
	for char in S:
		pprint([myTrie, foundMatches])
		if char in myTrie:
			for tupl in myTrie.pop(char):
				word, index = tupl[0], tupl[1] + 1
				if index < len(word):
					myTrie[word[index]].append((word, index))
				elif index == len(word):
					foundMatches.append((word, index))

	return max(foundMatches, key=lambda x: x[1])[0]

S = "abppplee"
D = ["able", "ale", "apple", "bale", "kangaroo"]

# print(findSubstring(S,D)) # O(len(S) x len	(m))
# print(findSubstringOpt1(S,D)) # O(len(S) + len(D)*longest(S))
# print(findSubstringOpt2(S,D)) # O(len(S) + len(D)*longest(S)), best case is O(nlogn~), n = len(D)
print(findSubstringOpt3(S,D)) # O(len(S) + L) , L = nr of characters in D