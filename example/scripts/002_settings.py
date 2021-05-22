class Settings():
	""" This is just variables stored as properties of a class.
		It still needs (allthough void) .inputs(), .output() and .build() and defines whatever else is handy.
		(It is nice, as in this case, to separate constants from methods.)
	"""

	def inputs(self):
		return None

	def output(self):
		return None

	def build(self):
		pass

	query = 'felines'
