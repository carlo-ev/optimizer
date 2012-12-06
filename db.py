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
		if len(from_sts) == 0 : return False
		tabl_set = map(lambda x : x.name , tables)
		return ( len( list( set(tabl_set) & set(from_sts) ) ) == len(from_sts) )

	def val_select(tables_used, select_sts) :
		print(select_sts)
		if len(select_sts)==0 : return False
		if len(select_sts)==1 and select_sts[0] != "*" :
			for x in select_sts :
				x  = x.split(".")
				print(x)
				table = [ tab for tab in tables_used if tab.name == x[0] ]
				print(table)
				if  len(table)==0 : return False   
				if (not x[1] in table[0]) or (not x[1] == "*") : return False  
		return True

	def validate(sql, db) :
		if ( "select" in sql.lower() ) and ( "from" in sql.lower() ) :
			print( "Select and From present on sql" )
			sql = ( sql.lower() ).split(" ")
			print(sql)
			select_sts = []
			for x in range( (sql.index("select")+1), sql.index("from") ) :
				select_sts.append( sql[x].strip(",") )

			from_sts = []
			for x in range( (sql.index("from")+1), sql.index("where") ) :
				from_sts.append(sql[x])

			where_sts = []
			for x in range( (sql.index("where")+1), len(sql) ) :
				where_sts.append(sql[x])

			if Optimizer.val_from(db, from_sts) :
				set_tables = [tg for tg in db if tg.name in from_sts]
				print( Optimizer.val_select(set_tables, select_sts) )
			print(select_sts)
			print(from_sts)
			print(where_sts)
			

		else :
			print("Select/From Statement(s) not present in the SQL!!!!")
