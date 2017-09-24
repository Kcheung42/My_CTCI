#assume 128  ASCII characters

def is_Unique(string):
	if len(string) > 128:
		return False

	char_set = [False for _ in range(128)]
	for char in string:

		#ord function returns ascii value of char
		val = ord(char)
		# print "this is val %d" % val
		if char_set[val]:
			return False
		char_set[val] = True
	return True

# if __name__ == "__main__":
# 	test
#
# 	string = "abcdef!"
# 	if(isUnique(string)):
# 		print "True"
# 	else:
# 		print "false"
