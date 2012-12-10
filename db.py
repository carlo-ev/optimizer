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

	def get_type(self, attri) : 
		return if "varchar" in self.attributes[attri] : "varchar" else : self.attributes[attri]

	def print_indices(self) :
		if self.indices :
			print(self.indices)

	def insert_ind(self, indcs) :
		self.indices = { indcs.pop(0) : indcs}

	def __contains__(self, key) :
		return ( key in self.attributes.keys() )



class Optimizer :

	math_op = [ "<", "=<", ">", "=>", "=" ]
	var_op = [ "like", "in"]

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

		def get_table(tables, attri) :
			for x in tables : if attri in x : return x

	def val_where(tables_used, where_sts) :
		print(where_sts)
		if len(where_sts) not in [ 3+(x*4) for x in range(0,5)] : return False 
		if "and" not in where_sts : return False
		for x in range(0,where_sts.count("and")) : where_sts.remove("and")
		print(where_sts)
		stat = [ where_sts[x:x+3] for x in range(0, ( len(where_sts)), 3)]
		print(stat) 
		for x in stat : if ( (x[1] not in math_op) or (x[1] not in var_op) ) : return False
		for st in stat :
			if (st[] )


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
				if( Optimizer.val_select(set_tables, select_sts) ) :
					print("Select and From are OK continuing with Where")
					Optimizer.val_where(set_tables, where_sts)
			print(select_sts)
			print(from_sts)
			print(where_sts)
			

		else :
			print("Select/From Statement(s) not present in the SQL!!!!")
