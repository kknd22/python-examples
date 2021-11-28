class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None

class LList:
	def __init__(self, head=None):
		self.head = head
	def insertAt(self, n, i):
		ii = 0
		nn = self.head
		while nn and ii < i:
			nn = nn.next
			ii += 1
		if i == ii:
			if nn:
				oldNext = nn.next
				nn.next = n
				n.next = oldNext
			else:
			    self.head = n
	def search(self, val):
		n = self.head
		while n != None :
			if n.val == val:
			  return True
			n = n.next
		return False
			
	def printList(self):
		n = self.head
		while n != None :
			print(n.val)
			n = n.next
			
			
ll = LList()
ll2 = LList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n11 = Node(11)
n00 = Node(00)

ll.head = n1
n1.next = n2
n2.next = n3

ll.insertAt(n11, 1)
ll.printList()

print('---------')

ll2.insertAt(n00, 0)
ll2.printList()
print('---------')
print(ll.search(3))