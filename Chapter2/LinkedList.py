from random import randint


class LinkedListNode:
	def __init__(self, value, nextNode=None, prevNode=None):
		self.value = value
		self.next = nextNode
		self.prev = prevNode

	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self, values=None):
		self.head = None
		self.tail = None
		if values is not None:
			self.add_multiple(values)

	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next

	def __str__(self):
		values = [str(x) for x in self]
		return ' -> '.join(values)

	def __len__(self):
		count = 0
		temp = self.head
		while temp:
			count += 1
			temp = temp.next
		return count

	def add(self, value):
		if self.head is None:
			self.tail = self.head = LinkedListNode(value)
		else:
			self.tail.next = LinkedListNode(value)
			self.tail = self.tail.next
		return self.tail

	def add_to_beginning(self, value):
		if self.head is None:
			self.tail = self.head = LinkedListNode(value)
		else:
			self.head = LinkedListNode(value, self.head)
		return self.head

	def add_multiple(self, values):
		for v in values:
			self.add(v)

	def generate(self, n, min_value, max_value):
		self.head = self.tail = None
		for i in range(n):
			self.add(randint(min_value, max_value))
		return self

	def deleteNodeWith(self, key):
		temp = self.head
		if temp is None:
			return
		if temp.data == key:
			self.head = temp.next
			temp = None
			return
		while(temp is not None):
			if temp == key:
				break
			prev = temp
			temp = temp.next
		if temp is None:
			return
		prev.next = temp.next
		temp = None

	def deleteNodeAt(self, position):
		temp = self.head
		if temp is None:
			return
		if position == 0:
			self.head = temp.next
			temp = None
			return
		for i in range(position-1):
			temp = temp.next
			if temp is None:
				break
		if temp is None:
			return
		next = temp.next.next
		temp.next = next
		temp = None

	def findMiddleNode(self):
		cur = self.head
		runner = cur
		if cur is not None:
			while(cur is not None and runner is not None):
				runner = runner.next.next
				cur = cur.next
		return temp

	def findNthNodefromEnd(self, n):
		cur = self.head
		runner = cur
		if cur is not None:
			steps = 0
			while(steps > n ):
				if(runner is None):
					return
				runner = runner.next
				steps += 1
			while(runner is not None):
				runner = runner.next
				cur = cur.next
		return cur

	def findNthNode(self):
		cur = self.head
		runner = cur
		if cur is not None:
			while(cur is not None and runner is not None):
				runner = runner.next.next
				cur = cur.next
		return temp

class DoublyLinkedList(LinkedList):
	def add(self, value):
		if self.head is None:
			self.tail = self.head = LinkedListNode(value, None, self.tail)
		else:
			self.tail.next = LinkedListNode(value)
			self.tail = self.tail.next
		return self
