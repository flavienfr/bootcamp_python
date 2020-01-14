class Evaluator:
	def zip_evaluate(coefs, words):
		if len(words) != len(coefs):
			return -1
		outputA = list(zip(words, coefs))
		return sum(len(tp[0]) * tp[1] for tp in outputA)

	def enumerate_evaluate(coefs, words):
		''' Bull shit, how to use it ?'''
		if len(words) != len(coefs):
			return -1
		outputA = list(enumerate(coefs))
		tmp = 0
		for tp in outputA:
			tmp += len(words[tp[0]]) * tp[1]
		return tmp

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))