class Table :

	def __init__(self, name_attributes_types):
		self.name = name_attributes_types.pop(0)
		self.attributes = {}
		self.indices = None
		for x in name_attributes_types :
			splt = x.split()
			self.attributes[splt[0]] = splt[1]

	def __str__(self):
		atr =""
		for x in self.attributes :
			atr += x + "\n"
		return "Nombre: %s \nAtributos: %s \nRecords: %s \nRecord Size: %skb\nRecordsPerBlock: %s" % ( self.name, atr, self.reg_count, self.reg_size, self.reg_bloq)

	def insert_prop(self, prps):
		self.reg_count = prps[1]
		self.reg_size = prps[2]
		self.reg_bloq = prps[3]

	def print_indices(self) :
		if self.indices :
			print(self.indices)

	def insert_ind(self, indcs) :
		self.indices = { indcs.pop(0) : indcs}

	def __contains__(self, key) :
		return ( key in self.attributes.keys() )



class Optimizer :

	def val_from(tables, from_sts) :
		print(from_sts)
		from_sts.pop(0)
		tabl_set = map(lambda x : x.name , tables)
		return ( len( list( set(tables_set) & set(from_sts) ) ) == len(from_sts) )


	def tables_in_use(tables, from_sts) :
		

	def validate(sql, db) :
		if ( "select" in sql.lower() ) & ( "From" in sql.lower() ) :
			print( "Select and From present on sql" )
			sql = ( sql.lower() ).split(" ")
			print(sql)
			select_sts = []
			for x in range( sql.index("select"), sql.index("from") ) :
				select_sts.append( sql[x].strip(",") )

			from_sts = []
			for x in range( sql.index("from"), sql.index("where") ) :
				from_sts.append(sql[x])

			where_sts = []
			for x in range( sql.index("where"), len(sql) ) :
				where_sts.append(sql[x])

			print(select_sts)
			print(from_sts)
			print(where_sts)
			print( slct_val(db, select_sts) )
			print( frm_val(db, from_sts) )

			if val_from(db, from_sts) :
				

		else :
			False
