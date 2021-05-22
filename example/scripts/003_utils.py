class Utils():
	""" This is just methods stored as methods of a class.
		It still needs (allthough void) .inputs(), .output() and .build() and defines whatever else is handy.
		(It is nice, as in this case, to separate constants from methods.)
	"""

	def __init__(self):
		self.species = {'canines' : ['Doggy', 'Hyena'], 'felines' : ['Cheetah', 'Panther'], 'bugs' : ['Nullpointer']}

	def inputs(self):
		return None

	def output(self):
		return None

	def build(self):
		pass

	def list_animals(self, kind):
		return self.species[kind]
