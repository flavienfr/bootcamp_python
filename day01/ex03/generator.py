from random import shuffle

def gen_error():
	print('ERROR')
	exit()

def generator(text, sep=" ", option='None'):
	opt = ['shuffle','unique','ordered', 'None']
	if not any(option in elem for elem in opt):
		gen_error()
	if not isinstance(text, str) or not isinstance(sep, str):
		gen_error()
	new_txt = text.split(sep)
	if option == 'ordered':
		new_txt.sort(key=str.lower)
	elif option == 'unique':
		new_txt = sorted(set(new_txt))
	elif option == 'shuffle':
		shuffle(new_txt)
	return new_txt

#text = "Le Lorem Ipsum est simplement du faux texte."
#for word in generator(text, sep=" ", option="ordered"):
#	print(word)
