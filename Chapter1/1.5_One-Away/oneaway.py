def oneAway(s1, s2):
	len1 = len(s1)
	len2 = len(s2)
	if s1 == s2:
		return True
	elif (len1 + 1 == len2):
		return one_edit_insert(s1,s2)
	elif (len1 - 1 == len2):
		return one_edit_insert(s2,s1)
	elif (len1 == len2):
		return one_edit_replace(s1, s2)

def one_edit_replace(s1, s2):
	trigger = False
	i, j = 0, 0
	while i < len(s1):
		if s1[i] != s2[i]:
			if trigger:
				return False
			else:
				trigger = True
		i += 1
		j += 1
	return True

def one_edit_insert(s1, s2):
	trigger = False
	i, j = 0, 0;
	while i < len(s1) and j < len(s2):
		if s1[i] != s2[j]:
			if trigger:
				return False
			else:
				trigger = True
				j += 1
		else:
			i += 1
			j += 1
	return True

if __name__ == "__main__":
	if oneAway("pare", "palr"):
		print "true"
	else:
		print "false"
