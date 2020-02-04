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

ruler = EnglishRuler(3, 3)
ruler.draw()