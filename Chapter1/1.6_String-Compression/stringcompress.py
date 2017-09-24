def compress(string):
	n = len(string)
	compress = []
	countConsecutive = 0
	for i in range(n):
		countConsecutive += 1
		if (i + 1 >= n) or (string[i] != string[i+1]):
			compress.append(string[i])
			compress.append(countConsecutive)
			countConsecutive = 0;
	return(compress if len(compress) < n else string)


if __name__ == "__main__":
	comp = compress("aabccccaaaccaa")
	print "%s" % comp
