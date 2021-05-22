import json

class ImportSomething():
	""" This is a typical input script. It isolates import details, paths, versions, etc. to provide necessary data.
		You can have one for all the input files, inputs() can return a list.
		It generates some output **one file** whose name is returned by output()
	"""

	def inputs(self):
		return './input/example.csv'

	def output(self):
		return './data/this_project.json'

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
