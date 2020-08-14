#!usr/bin/env python3

def evalPostfix(exp):
	'''
	Evaluate the given postfix expression
	:param: exp: String, postfix expression to evaluate
	rtype: Number (integer / float)
	'''
	stack = []
	for el in exp:
		if el.isnumeric():
			stack.append(el)
		else:
			val1 = stack.pop()
			val2 = stack.pop()
			stack.append(str(eval(val2 + el + val1)))
	# return the last element of the stack: evaluated solution
	return stack.pop()

exp = '53+62/*35*+'
# exp = '231*+9-'
print('Value of {} is {}'.format(exp, evalPostfix(exp)))