import string

def text_analyzer(text=''):
	if not text:
		text = input()
	print('The text contains', len(text), 'characters:')
	print("-", sum(1 for c in text if c.isupper()), "upper letters")
	print("-", sum(1 for c in text if c.islower()), "lower letters")
	print("-", sum(1 for c in text if c in string.punctuation), "punctuation marks")
	print("-", sum(1 for c in text if c == ' '), "spaces")
