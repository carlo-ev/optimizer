class Unit :

	def __init__(self, name, *attrs):
		self.name = name
		self.attributes = attrs

	def __str__(self):
		return "%s : %s" % (self.name, str(self.attributes))

	def getContent(self):
		return self.attributes

	def contains(self, element):
		for x in self.attributes :
			if x == element :
				return 1
		return 0

