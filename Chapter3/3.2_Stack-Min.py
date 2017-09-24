
class StackNode:
	def __init__(self, value=None, nextNode=None, minVal=None):
		self.value = value
		self.next = nextNode
		self.minVal = minVal

class StackMin:
	def __init__(self, values=None):
		self.top = None
		if values:
			self.push_multi(values)
	
	def isEmpty(self):
		return self.top == None

	def push(self, value):
		if self.isEmpty():
			self.top = StackNode(value, None, value)
		else:
			if value < self.top.minVal:
				self.top = StackNode(value, self.top, value)
			else:
				self.top = StackNode(value, self.top, self.min_global)

	def push_multi(self, values=None):
		if values:
			for v in values:
				self.push(v)
	
	def pop(self):
		if self.isEmpty():
			return "stack is empty"
		else:
			val = self.top.value
			self.top = self.top.next
			return val
	
	def min(self):
		if self.isEmpty():
			return "stack is empty"
		else:
			return self.top.minVal

	
	def printstack(self):
		if self.isEmpty():
			print "stack is empty"
		else:
			cur = self.top
			while cur:
				print "%d->" %cur.value,
				cur = cur.next
			print "NULL"

stack = StackMin([5,4,3,2,1])
stack.pop()
stack.pop()
stack.pop()
stack.push(3)
stack.pop()
print "min is:%r" %stack.min()
stack.printstack()


