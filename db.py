class Unit :

	def __init__(self, stats):
		print(stats)
		self.name = stats.pop(0)
		self.attributes = stats

	def __str__(self):
		return "Nombre: %s \nAtributos: %s" % (self.name, str(self.attributes))

	def getContent(self):
		return self.attributes

	def contains(self, element):
		for x in self.attributes :
			if x == element :
				return 1
		return 0

