# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    palindrome.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/10 13:47:01 by kcheung           #+#    #+#              #
#    Updated: 2018/01/10 13:47:07 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def isPalindrome(string):
	table = [0 for _ in range(ord('z') - ord('a') + 1)]
	countodd = 0
	for c in string:
		x = getindex(c)
		if x != -1:
			table[x] += 1
			if table[x] % 2:
				countodd +=1
			else:
				countodd -=1
	return (countodd <= 1)

def getindex(c):
	a = ord('a')
	z = ord('z')
	A = ord('A')
	Z = ord('Z')
	val = ord(c)

	if a <= val <= z:
		return val - a
	elif A <= val <= z:
		return val - A
	else:
		return -1

if __name__ == "__main__":
	string1 = "taco cat"
	string2 = "tact coa"
	if(isPalindrome(string2)):
		print "Yes!"
	else:
		print "NO!"
