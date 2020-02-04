## English ruler code 
class EnglishRuler():
	def __init__(self, num_inches, major_length):
		self._num_inches = num_inches
		self._major_length = major_length

	def _draw_line(self, length, label = None):
		line = '-'*length
		if label is not None:
			line += ' '+ label
		print(line)

	def _draw_interval(self, center_length):
		# Base case 
		if center_length ==0:
			return 
		else:
			self._draw_interval(center_length-1)
			self._draw_line(center_length)
			self._draw_interval(center_length-1)

	def draw(self):
		self._draw_line(length = self._major_length, label = "0")

		for i in range(1, 1+self._num_inches):
			self._draw_interval(self._major_length-1)
			self._draw_line(self._major_length, label = str(i))

#ruler = EnglishRuler(3, 3)
#ruler.draw()

########################################################

l = list(range(1, 15))

def binary_search(seq, number):
	low = 0
	high = len(seq)-1

	def _look_for_element(low, high):
		if low > high:
			return False
		else:  
			mid = (low+high)//2
			if seq[mid] == number:
				return True

			elif number < seq[mid]: 
				return _look_for_element(low, mid-1)
			else:
				return _look_for_element(mid+1, high)

	return _look_for_element(low, high)


################################################


import os

def disk_usage(path):

	total = os.path.getsize(path) 
	if os.path.isdir(path): 
		for filename in os.listdir(path): 
			childpath = os.path.join(path, filename) 
			total += disk_usage(childpath) 
		print ( '{0:<7}'.format(total), path) 
	return total

print(disk_usage('../'))
