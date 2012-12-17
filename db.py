from math import *

class Table :

	def __init__(self, name_attributes_types):
		self.name = name_attributes_types.pop(0)
		self.attributes = {}
		self.indices = None
		for x in name_attributes_types :
			splt = x.split()
			self.attributes[splt[0]] = splt[1]

	def __str__(self):
		return self.name

	def to_p(self):
		atr =""
		for x in self.attributes :
			atr += x + "\n"
		return "Nombre: %s \nAtributos: %s \nRecords: %s \nRecord Size: %skb\nRecordsPerBlock: %s\nIndices:%s" % ( self.name, atr, self.reg_count, self.reg_size, self.reg_bloq, str(self.indices))
		

	def insert_prop(self, prps):
		self.reg_count = int(prps[1])
		self.reg_size = int(prps[2])
		self.reg_bloq = int(prps[3])

	def get_type(self, attri) : 
		if ("varchar" in self.attributes[attri]) : 
			return "varchar" 
		else : 
			return self.attributes[attri] 

	def print_indices(self) :
		if self.indices :
			print(self.indices)

	def get_indices(self) :
		return self.indices

	def insert_ind(self, indcs) :
		indcs.pop(0)
		x = indcs.pop(0)
		self.indices = { x : indcs}
		self.indices[x][1] = int(self.indices[x][1])
		self.indices[x][2] = int(self.indices[x][2])

	def __contains__(self, key) :
		return ( key in self.attributes.keys() )



class Approval :

	math_op = [ "<", "=<", ">", "=>", "=" ]
	var_op = [ "like", "in"]
	tables_in_use = None
	last_used_select = None
	last_used_where = None

	def val_from(tables, from_sts) :
		if len(from_sts) == 0 : return False
		tabl_set = map(lambda x : x.name , tables)
		return ( len( list( set(tabl_set) & set(from_sts) ) ) == len(from_sts) )

	def val_select(tables_used, select_sts) :
		if len(select_sts)==0 : return False
		if len(select_sts)==1 and select_sts[0] != "*" :
			for x in select_sts :
				x  = x.split(".")
				table = [ tab for tab in tables_used if tab.name == x[0] ]
				if  len(table)==0 : return False   
				if (not x[1] in table[0]) or (not x[1] == "*") : return False  
		return True

	def get_type(tables, attri) :
		for x in tables : 
			if attri in x : 
				return x.get_type(attri)
		return None

	def val_where(tables_used, where_sts) :
		if len(where_sts) not in [ 3+(x*4) for x in range(0,5)] : return False 
		if ("and" not in where_sts) and (len(where_sts) > 3) : return False
		for x in range(0,where_sts.count("and")) : where_sts.remove("and")
		stat = [ where_sts[x:x+3] for x in range(0, ( len(where_sts)), 3)]
		for x in stat : 
			if  not ( (x[1] in Approval.math_op) or (x[1] in Approval.var_op) ) : return False
		#print("No more validation will be made for time essentials")
		#for st in stat : st[0] = st[0].split(".")
		#print(stat)
		Approval.last_used_where = stat
		return True

	def validate(sql, db) :
		#print("Sql statement presented: {0}".format(sql))
		if not  ( "select" in sql.lower() ) and ( "from" in sql.lower() ) : print("Reserved Words Select and From are not even present in sql statement!!!"); return False
		#print( "Select and From present on sql" )
		sql = ( sql.lower() ).split(" ")

		select_sts = []
		for x in range( (sql.index("select")+1), sql.index("from") ) :
			select_sts.append( sql[x].strip(",") )
		#print("Select statement: {0}".format(str(select_sts)))

		from_sts = []
		for x in range( (sql.index("from")+1), sql.index("where") ) :
			from_sts.append(sql[x])
		#print("From statement: {0}".format(str(from_sts)))

		where_sts = []
		for x in range( (sql.index("where")+1), len(sql) ) :
			where_sts.append(sql[x])
		#print("Where statement: {0}".format(str(where_sts)))

		if not Approval.val_from(db, from_sts) : print("Invalid From statement \n{0}".format(from_sts)); return False
		Approval.tables_in_use = [tg for tg in db if tg.name in from_sts]
		if not Approval.val_select(Approval.tables_in_use, select_sts) : print("Invalid Select statement \n{0}".format(select_sts)); return False
		if not Approval.val_where(Approval.tables_in_use, where_sts) : print("Invalid Where statement \n{0}".format(where_sts)); return False
		print("All validations passed, proceeding...")	
		Approval.last_used_select = select_sts

		return True



class Calculations :

	multiple = ["<",">",">=","<="]

	def cost(tables_used, statement) :
		current_table = list( filter( lambda x : x.name == statement[0].split(".")[0], tables_used ) )[0]
		index = statement[0].split(".")[1]
		if index in current_table.get_indices() :
			return Calculations.switch[current_table.get_indices()[index][0]](statement, current_table, index)
		else :
			return Calculations.linear_search(current_table)

	def linear_search(table) :
		return ( (table.reg_count/2) /table.reg_bloq)

	def binary_search(statement, table, index) :
		index_map = table.get_indices()[index]
		if table.reg_count == index_map[1] :
			return log( (table.reg_count/table.reg_bloq),2 ) + ceil( 1/table.reg_bloq )
		else :
			return log( (table.reg_count/table.reg_bloq),2 ) + ceil( (table.reg_count/index_map[1]) /table.reg_bloq ) - 1

	def primary_index(statement, table, index) :
		index_map = table.get_indices()[index]
		if (statement[1] in  Calculations.multiple) and (table.reg_count == index_map[1]) :
			return (index_map[2] + ( (table.reg_count/table.reg_bloq)/2 ) )
		else :
			return (index_map[2] + 1)

	def hash_index(statement, table, index) : 
		index_map = table.get_indices()[index]
		if  (statement[1] in Calculations.multiple) and (table.reg_count == index_map[1]) :
			return 1
		else :
			return (table.reg_count/table.reg_bloq)

	def clustering_index(statement, table, index) :
		index_map = table.get_indices()[index]
		if (statement[1] in Calculations.multiple):
			return index_map[2] +  ceil( ( (table.reg_count/index_map[1]) / table.reg_bloq ) )
		else :
			return index_map[2]

	switch = { "binary" : binary_search, "primary" : primary_index, "hash" : hash_index, "cluster" : clustering_index }
