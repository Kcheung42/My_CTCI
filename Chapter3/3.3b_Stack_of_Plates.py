class SetOfStacks:
	def __init__(self, capacity):
		self.capacity = capacity
		self.stacks = []

	def is_empty(self):
		return self.size == 0

	def push(self, value):
		if len(self.stacks) == 0 or (len(self.stacks[-1]) == self.capacity):
				self.stacks.append([])
		self.stacks[-1].append(value)

	def pop(self):
		if len(self.stacks) == 0:
			return
		v = self.stacks[-1].pop()
		if len(self.stacks[-1]) == 0:
			self.stacks.pop()
		return v

	# Not rolling over version. Allows some stack not to be at full capacity
	def popAt(self, index):
		if index < 1 or index > len(self.stacks) or len(self.stacks[index-1]) == 0:
			return self.stacks[index - 1].pop()


plates = SetOfStacks(5)
plates.push(1)
plates.push(2)
plates.push(3)
plates.push(4)
plates.push(5)
plates.push(6)
plates.push(6)
plates.push(8)
plates.push(9)
plates.pop()
plates.pop()

plates.popAt(2)
plates.popAt(2)

for p in plates.stacks:
	print p
