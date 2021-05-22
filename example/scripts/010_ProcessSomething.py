import json

class ProcessSomething():
	""" This is a typical script. We put everything (or part of what) we just did together to compute something and store it.
	"""

	def inputs(self):
		return ImportSomething.output()

	def output(self):
		return './data/selected.json'

	def build(self):
		with open(self.inputs()) as f:
			txt = f.read().splitlines()

		data = []

		for i, row in enumerate(txt):
			col  = row.split(',')
			item = {}

			if i == 0:
				names = col
			else:
				for key, val in zip(names, col):
					item[key] = val
				data.append(item)

		with open(self.output(), 'w') as f:
			json.dump(data, f)
