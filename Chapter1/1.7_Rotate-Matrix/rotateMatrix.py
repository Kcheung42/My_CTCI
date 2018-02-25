def rotate(m):
	"""docstring for rotate"""
	n = len(m)
	for l in range(n // 2):
		first = l
		last = n - l - 1
		print("first:{} last:{}".format(first, last))
		for i in range(first, last):
			offset = i - first
			top = m[first][i]
			m[first][i] = m[last-offset][first]
			m[last-offset][first] = m[last][last-offset]
			m[last][last-offset] = m[i][last]
			m[i][last] = top
	return True

def printm(m):
	n = len(m)
	for i in range(n):
		for j in range(n):
			print("[%.2d]" %m[i][j],  end="")
		print("\n")

if __name__ == "__main__":

	m = (
		[1,2,3,4],
		[5,6,7,8],
		[9,12,11,12],
		[13,14,15,16]
		)
	n = len(m)
	print("n:%d" %n)
	printm(m)
	print(rotate(m))
	printm(m)

