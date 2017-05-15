#Given code establishing the Node class
class Node:
	def __init__(self, data):
		self.right = None
		self.left = None
		self.data = data
	def __repr__(self):
		return str(self.data)


#QUESTION 1 : Print a Binary tree, using pre-order traversal 
def preorder(node):


#QUESTION 2: Print a Binary tree, using in-order traversal 
def inorder(node):


#QUESTIONS 3: Print a Binary tree, using post-order traversal 
def postorder(node):


#QUESTION 4: Determine is a tree is a valid BST. Will return T or F
#Is it a BST?
#Given a Binary Tree, check if it is a BST. A valid BST doesn't have to be complete or balanced. Duplicate elements are not allowed in a BST.
#Solutions:  O(N) time https://discuss.leetcode.com/topic/4659/c-in-order-traversal-and-please-do-not-rely-on-buggy-int_max_min-solutions-any-more
def is_valid_BST(node):


#QUESTION 5: Print each level of a tree one level on each line
# Example output for the tree in test below
# 4
# 3 10
# 1 2 7
# 6

def print_levels(node):

#Use this method to call/other methods in the console
def test():
	#Instantiate our Binary Tree
	nodeA = Node(4)
	nodeB = Node(3)
	nodeC = Node(1)
	nodeD = Node(2)
	nodeE = Node(10)
	nodeF = Node(7)
	nodeG = Node(6)

	nodeA.left = nodeB
	nodeA.right = nodeE
	nodeB.left = nodeC
	nodeB.right = nodeD
	nodeE.left = nodeF
	nodeF.left = nodeG

	Uncomment one at a time to test your method
	#preorder(nodeA)
	#inorder(nodeA)
	#postorder(nodeA)


#Executing test method
test()


