# 86848406

class LinkedList:

	def __init__(self, x=None):
		self.value = x
		self.next_item = None
		self.previous_item = None


class Deque:
	def __init__(self, n):
		self.max_m = n
		self.size = 0

	def is_empty(self):
		return self.size == 0

	def push_back(self, value):
		if self.size == self.max_m:
			return 'error'
		if self.is_empty():
			self.head = LinkedList(value)
			self.tail = LinkedList(value)
			self.size += 1
			return
		elif self.size == 1:
			self.tail = LinkedList(value)
			self.head.next_item = self.tail
			self.tail.previous_item = self.head
			self.size += 1
			return
		item = self.tail
		self.tail = LinkedList(value)
		self.tail.previous_item = item
		item.next_item = self.tail
		self.size += 1
		return

	def push_front(self, value):
		if self.size == self.max_m:
			return 'error'
		if self.is_empty():
			self.head = LinkedList(value)
			self.tail = LinkedList(value)
			self.size += 1
			return
		elif self.size == 1:
			self.head = LinkedList(value)
			self.head.next_item = self.tail
			self.tail.previous_item = self.head
			self.size += 1
			return
		item = self.head
		self.head = LinkedList(value)
		self.head.next_item = item
		item.previous_item = self.head
		self.size += 1
		return


	def pop_front(self):
		if self.is_empty():
			return 'error'
		item = self.head.value
		self.head = self.head.next_item
		self.size -= 1
		return item

	def pop_back(self):
		if self.is_empty():
			return 'error'
		item = self.tail.value
		self.tail = self.tail.previous_item
		self.size -= 1
		return item


if __name__ == '__main__':
	quantity_of_functions = int(input())
	max_size_deque = int(input())
	deque = Deque(max_size_deque)
	result = []
	for _ in range(quantity_of_functions):
		raw = input().split()
		if len(raw) > 1:
			if raw[0] == 'push_back':
				answer = deque.push_back(int(raw[1]))
				if answer is not None:
					result.append(answer)
			else:
				answer = deque.push_front(int(raw[1]))
				if answer is not None:
					result.append(answer)
		elif raw[0] == 'pop_front':
			result.append(deque.pop_front())
		else:
			result.append(deque.pop_back())

	for item in result:
		print(item)

