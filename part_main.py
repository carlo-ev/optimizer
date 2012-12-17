import math
from db import *
from easygui import * 
import files as fl


# msgbox(msg="Proyecto Base de Datos 2 \n Optimizador SQL", title="Sql Optimizer by CMEV 2012", ok_button="Continue")

db = fl.read_indices( fl.read_add_stats( fl.crt_tables( fl.read_tables() ) ) )
#show=""
#for x in db :
#	show += str(x) + "\n\n"

#textbox(msg="Selected Data to Work with:",title="Sql Optimizer by CMEV 2012 Data Base", text=(show + "\n\n\n\n****Changes Will not be saved!!!****"))


#for x in db :
#	x.print_indices()


sql = enterbox(msg="Insert sql Statment to be optimized: ", title="Sql Optimizer by CMEV 2012 SQL Input")


Approval.validate(sql, db)
tables_used = Approval.tables_in_use
select = Approval.last_used_select
where  = Approval.last_used_where
print(tables_used)
print(select)
print(where)

for statement in where :
	print(statement)
	print("The cost in blocks of this statement is {0}".format( ceil(Calculations.cost(tables_used, statement)) ) )

''' def statements(lst_sts) :
	lst = lst_sts.split("and")
	lst =  lst.split(" ")
	for x in range(0, len(lst), 3) :
		for
		'''  