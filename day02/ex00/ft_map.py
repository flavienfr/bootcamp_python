def ft_map(function_to_apply, list_of_inputs):
	new_lst = []
	for elem in list_of_inputs:
		if function_to_apply(elem):
			new_lst.append(elem)
	return new_lst
