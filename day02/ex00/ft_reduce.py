def ft_reduce(function_to_apply, list_of_inputs):
	it = iter(list_of_inputs)
	try:
		value = next(it)
	except StopIteration:
		return
	for element in it:
		value = function_to_apply(value, element)
	return value