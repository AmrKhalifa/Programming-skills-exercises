class BinaryTree:
	class _Node:
		def __init__(self, value, left = None, right = None): 
			self.value = value 
			self.left = left 
			self.right = right

		def __str__(self):
			return "("+str(self.value)+")" 

	def __init__(self, root_value): 
		self.root = self._Node(root_value)

	def traverse(self, traversal = None): 
		if traversal == 'pre': 
			self._preorder()
			print(" ")
		if traversal == 'post': 
			self._postorder()
			print(" ")

		if traversal == 'in': 
			self._inorder()
			print(" ")


	def _preorder(self): 
		def _recursive_preorder(node, d = 0, arr = None): 
			if node:
				print('-'*d,'>', ''.join([str(item)+"." for item in arr]), node)
				arr.append(0)
				_recursive_preorder(node.left,d+3, arr)
				arr[-1] +=1 
				_recursive_preorder(node.right, d+3, arr)
				arr.pop() 
		_recursive_preorder(self.root, arr = [1])

	def _postorder(self): 
		def _recursive_postorder(node): 
			if node:
				_recursive_postorder(node.left)
				_recursive_postorder(node.right)
				print(node, end = '->')
		_recursive_postorder(self.root)


	def _inorder(self): 
		def _recursive_inorder(node): 
			if node:
				_recursive_inorder(node.left)
				print(node, end = '->')
				_recursive_inorder(node.right) 
				
		_recursive_inorder(self.root)

tree = BinaryTree(root_value = "chapter 1")
tree.root.left = tree._Node("section A")
tree.root.right = tree._Node("section B")
tree.root.left.left = tree._Node("subsection i")
tree.root.left.right = tree._Node("subsection ii")
tree.root.right.left = tree._Node("subsection i")
tree.root.right.right = tree._Node("subsection ii")

tree.traverse(traversal='pre')