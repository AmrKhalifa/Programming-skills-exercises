# def get_permutations (string):
#     l =[]
#     def _permute(prefix, suffix, result):
#         if len(suffix) == 0:
#             result.append(prefix)
#         else:
#             for i in range(len(suffix)):
#                 _permute(prefix + suffix[i], suffix[:i] + suffix[i+1:], result)
    
#     _permute("", string, l)

#     return l
        

# print(get_permutations('123'))


def get_permutes(st):
	permutes = []
	seq = [char for char in st]

	def swap(seq, i, j):
		seq[i], seq[j] = seq[j], seq[i]
		return seq

	left = 0
	right = len(st)
	
	def _permute(sequence, left, right):

		if left == right:
			permutes.append("".join(sequence))
		else: 
			for i in range(left, right):
				string = swap(sequence, left, i)
				_permute(string, left+1, right)
	
	_permute(seq, left, right)
	return permutes


print(get_permutes("ABCD"))