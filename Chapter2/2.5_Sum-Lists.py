from LinkedList import LinkedList

def sum_list(ll_a, ll_b):
	result = LinkedList()
	val = convert(ll_a) + convert(ll_b)
	while(val):
		result.add(val % 10)
		val //= 10
	return result

def convert(ll):
	if ll.head is None:
		return 0
	cur = ll.head
	result = 0
	digplace = 1
	while(cur):
		result = result + cur.value * digplace
		cur = cur.next
		digplace  *= 10
	return result

def sum_list_followup(ll_a, ll_b):
	result = LinkedList()
	val = convert_Followup(ll_a) + convert_Followup(ll_b)
	while(val):
		result.add_to_beginning(val % 10)
		val //= 10
	return result

def convert_Followup(ll):
	if ll.head is None:
		return 0
	cur = ll.head
	result = 0
	while(cur):
		result = result * 10 + cur.value
		cur = cur.next
	return result

lla = LinkedList()
llb = LinkedList()

lla.generate(4,0,9)
llb.generate(3,0,9)
llresult = sum_list(lla, llb)
llresult2 = sum_list_followup(lla, llb)
# print(lla)
print(llb)
print(llresult)
print(llresult2)


