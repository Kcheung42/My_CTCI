
def swap(a, b):
	"""docstring for swap"""
	a,b = b,a
	
def rotate(matrix):
	"""docstring for rotate"""
	n = len(matrix)
	layers = n/2

	for lay in range(layers):

		for i in range(n - 1):
			x , y = lay, lay+i
			print"x:%d, y:%d" %(x,y)
			x2,y2 = x+(n-1-i), y + (-i)
			print"x2:%d, y2:%d" %(x2,y2)
			matrix[x][y] , matrix[x2][y2] = matrix[x2][y2] , matrix[x][y]
			x,y = x2,y2
			x2,y2 = x+(i), y + (n-1-i)
			print"x2:%d, y2:%d" %(x2,y2)
			matrix[x][y] , matrix[x2][y2] = matrix[x2][y2] , matrix[x][y]
			x,y = x2,y2
			x2,y2 = x+(-1 * (n-1-i)), y + (i)
			print"x2:%d, y2:%d" %(x2,y2)
			matrix[x][y] , matrix[x2][y2] = matrix[x2][y2] , matrix[x][y]
		n -= 2

def printm(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(n):
			print "[%.2d]" %matrix[i][j],
		print "\n"

if __name__ == "__main__":

	m = ([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16])
	printm(m)
	rotate(m)
	printm(m)

