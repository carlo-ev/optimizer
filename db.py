class Table :

	def __init__(self, name_attributes_types):
		self.name = name_attributes_types.pop(0)
		self.attributes = {}
		for x in name_attributes_types :
			splt = x.split()
			self.attributes[splt[0]] = splt[1]

	def __str__(self):
		return "Nombre: %s \nAtributos: %s \nRecords: %s \nRecord Size: %skb\nRecordsPerBlock: %s" % (self.name, str(self.attributes.keys()), self.reg_count, self.reg_size, self.reg_bloq)

	def contains(self, element):
		for x in self.attributes :
			return element  in x.key
	
	def insert_prop(self, prps):
		self.reg_count = prps[1]
		self.reg_size = prps[2]
		self.reg_bloq = prps[3]
