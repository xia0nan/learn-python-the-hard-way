__author__ = 'xiaonan'

import sys


dict = {
	"direction": ["north", "south", "east", "west", "down", "up", "left", "right", "back"],
	"verb": ["go", "stop", "kill", "eat"],
	"stop": ["the", "in", "of", "from", "at", "in"],
	"noun": ["door", "bear", "princess", "cabinet"]
}

sentence = []
input_string = "bear IAS princess"

def convert_number(s):
    try:
        if len(s) < 10:
        	return int(s)
        else:
        	return None
    except ValueError:
        return None


def scan(input_string):

	words = input_string.split()
	print words
	for word in words:
		founded = 0
		print word
		for key, value in dict.iteritems():
			print key
			print value
			if word in value:
				sentence.append((key, word))
				print "appended"
				founded = 1
				break
			elif convert_number(word):
				sentence.append(("number",convert_number(word)))
				founded = 1
				print "appended num"
				break

		if founded == 0:
			sentence.append(("error", word))
			print "append error"

	print sentence[:]
	return sentence


scan(input_string)