#!/usr/bin/python

import sys
import random

WORDFILE = 'diceware.wordlist.asc'
def getSpecialCharacter():
	#    1 2 3 4 5 6
	#F 1 ~ ! # $ % ^
	#o 2 & * ( ) - =
	#u 3 + [ ] \ { }
	#r 4 : ; " ' < >
	#t 5 ? / 0 1 2 3
	#h 6 4 5 6 7 8 9
	specialCharArray = [
		['~', '!', '#', '$',  '%',  '^' ],
		['&', '*', '(', ')',  '-',  '=' ],
		['+', '[', ']', '\\',  '{', '}' ],
		[':', ';', '"', '\'', '<',  '>' ],
		['?', '/', '0', '1',  '2',  '3' ],
		['4', '5', '6', '7',  '8',  '9' ]
		]
	x,y = random.randint(0,5), random.randint(0,5)
	return specialCharArray[x][y]

def getRandomWordCode():
	s = ''
	for x in range(5):
		s += str(random.randint(1,6))
	return s

def parseWordList():
	infile = open(WORDFILE, 'r')
	wordlist = infile.readlines()

	wordmap = {}

	for wordline in wordlist:
		code, word = wordline.rstrip().split('\t')
		wordmap[code] = word
	
	return wordmap

def getRandomWord():
	return words[getRandomWordCode()]

def getPassphrase(phraseLength = 5):
	passphrase = ''
	for x in range(phraseLength):
		passphrase += getRandomWord() + ' '
	return passphrase.rstrip()

def getPassword(maxLength = 12):
	password = ''
	while len(password) < maxLength:
		password += getRandomWord()
		password += getSpecialCharacter()
	return password[:maxLength]
	
words = parseWordList()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		try:
			print getPassphrase(int(sys.argv[1]))
		except TypeError:
			print "Invalid phrase length: dw.py [length]"
	else:
		print getPassphrase()


 
