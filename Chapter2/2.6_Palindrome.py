from LinkedList import LinkedList

def isPalindrome(ll):
	runner = cur = ll.head
	stack = []

	if runner is None:
		return True

	while(runner.next):
		stack.append(cur.value)
		cur = cur.next
		runner = runner.next.next
	
	if runner:
		cur = cur.next
	
	while cur:
		top = stack.pop()
		if top != cur.value:
			return False
		cur = cur.next
	return True

ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(isPalindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(isPalindrome(ll_false))
