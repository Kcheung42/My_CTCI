def rotate(matrix):
	"""docstring for rotate"""
	n = len(matrix)
	for l in range(n // 2):
		first = l
		last = n - l - 1
		for i in range(first, last):
			offset = i - first
			top = matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] = matrix[last][last-offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = top
	return True

def printm(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(n):
			print "[%.2d]" %matrix[i][j],
		print "\n"

if __name__ == "__main__":

	m = (
		[1,2,3,4],
		[5,6,7,8],
		[9,12,11,12],
		[13,14,15,16]
		)
	n = len(m)
	print "n:%d" %n
	printm(m)
	print(rotate(m))
	printm(m)

