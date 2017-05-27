#!/usr/bin/python
#Given code establishing the Node class
class Node:
	def __init__(self, data):
		self.right = None
		self.left = None
		self.data = data
	def __repr__(self):
		return str(self.data)


#QUESTION 1 : Print a Binary tree, using pre-order traversal: root, left, right
def preorder(node):
	if node != None:
		print node
		preorder(node.left)
		preorder(node.right)

#QUESTION 2: Print a Binary tree, using in-order traversal: left, root, right
def inorder(node):
	if node != None:
		inorder(node.left)
		print node
		inorder(node.right)

#QUESTIONS 3: Print a Binary tree, using post-order traversal left, right, root
def postorder(node):
	if node != None:
		postorder(node.left)
		postorder(node.right)
		print node

#QUESTION 4: Determine is a tree is a valid BST. Will return T or F
#Is it a BST?
#Given a Binary Tree, check if it is a BST. A valid BST doesn't have to be complete or balanced.
# Duplicate elements are not allowed in a BST.
#Solutions:  O(N) time
# https://discuss.leetcode.com/topic/4659/c-in-order-traversal-and-please-do-not-rely-on-buggy-int_max_min-solutions-any-more

#Got false for the initial example then corrected to valid BST to test again
def is_valid_BST(node):

	# Check left branch for any elements greater than or equal to current element
	if node.left != None and node.left.data < node.data:
		if is_valid_BST(node.left) == False:
			return False
	elif node.left != None:
		return False

	# Check right branch for any elements less than or equal to current element
	if node.right != None and node.right.data > node.data:
		if is_valid_BST(node.right) == False:
			return False
	elif node.right != None:
		return False

	return True


#QUESTION 5: Print each level of a tree one level on each line
# Example output for the tree in test below
# 					4
# 		2 						10
# 	1 		3				7
# 						6

#Main function that prints all levels
def print_levels(node):
	d = tree_depth(node)
	for i in range(1, d + 1):
		print print_level(node, i)


#Will print all elements in a given level
def print_level(node, level):
	s = ""
	if node == None:
		return ""
	if level == 1:
		s = s + str(node.data) + " "
	elif level > 1:
		s = s + print_level(node.left, level - 1)
		s = s + print_level(node.right, level - 1)

	return s

#Will get tree depth
def tree_depth(node):
	if node == None:
		return 0

	l = tree_depth(node.left)
	r = tree_depth(node.right)

	if l > r:
		return l + 1
	else:
		return r + 1

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

	nodeA.left = nodeD
	nodeA.right = nodeE
	nodeD.left = nodeC
	nodeD.right = nodeB
	nodeE.left = nodeF
	nodeF.left = nodeG

	#Uncomment one at a time to test your method
	#preorder(nodeA)
	#inorder(nodeA)
	#postorder(nodeA)
	#print is_valid_BST(nodeA)
	#print tree_depth(nodeA)
	print_levels(nodeA)


#Executing test method
test()


