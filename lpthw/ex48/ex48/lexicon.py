__author__ = 'xiaonan'
dict = {
	"direction": ["north", "south", "east", "west", "down", "up", "left", "right", "back"],
	"verb": ["go", "stop", "kill", "eat"],
	"stop": ["the", "in", "of", "from", "at", "in"],
	"noun": ["door", "bear", "princess", "cabinet"]
}

def convert_number(s):
    try:
        if len(s) < 10:
        	return int(s)
        else:
        	return None
    except ValueError:
        return None

def scan(input_string):
	sentence = []
	words = input_string.split()
	
	for word in words:
		founded = 0
		for key, value in dict.iteritems():
			if word in value:
				sentence.append((key, word))
				founded = 1
				break
			elif convert_number(word):
				sentence.append(("number",convert_number(word)))
				founded = 1
				break
		if founded == 0:		
			sentence.append(("error", word))
			
	return sentence