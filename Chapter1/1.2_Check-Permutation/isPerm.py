
def isPerm(str1, str2):
	if len(str1) != len(str2):
		return False
	str1 = sorted(str1)
	str2 = sorted(str2)
	for i in range(len(str1)):
		if(str1[i] != str2[i]):
			return False
	print "%r" % str1
	print "%r" % str2
	return True

# def partition(alist, start, end):
# 	pivot = alist[end]
# 	p_idx = start
# 	for i in range(end-1):
# 		print "this is c %r" % alist[i]
# 		if alist[i] < pivot:
			# alist[p_idx], alist[i] = alist[i], alist[p_idx]
			# p_idx += 1
	# alist[p_idx], alist[end] = alist[end], alist[p_idx]

# def qsort_helper(alist, start, end):
# 	if start < end: 
# 		pivot = partition(alist, start, end)
# 		qsort_helper(alist, start, pivot - 1)
# 		qsort_helper(alist, pivot + 1, end)
#
# def quicksort(alist):
# 	qsort_helper(alist, 0, len(alist)-1)
#
if __name__ == "__main__":
	
	alist = "kjaiwnaid"
	alist = sorted(alist)
	# quicksort(alist);
	if isPerm("abcdd", "dcbag"):
		print "yes"
	else:
		print "no"
	# print "list is %r" % alist
