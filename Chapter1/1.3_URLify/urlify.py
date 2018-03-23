def urlify(string, length):
	'''function replaces single spaces with %20 and removes trailing spaces'''
	new_index = len(string)

	for i in reversed(range(length)):
		if string[i] == ' ':
			string[new_index - 3:new_index] = '%20'
			new_index -= 3
		else:
			# Move characters
			string[new_index - 1] = string[i]
			new_index -= 1
	return string

if __name__ == "__main__":
	string = list('much ado about nothing      ')
	print "len is %d" % len(string)
	print "new string is %r" % urlify(string,22)
