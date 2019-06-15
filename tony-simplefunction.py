def repeat(s, exclaim):
	result = s * 3
	if exclaim:
		result = result + '!!!'
	return result

	def main():
		if name == 'Tony':
			print (repeat(name) + '!!!')
		else:
			print (repeat(name))
